# -*- coding: utf-8 -*-

import logging, base64, os
from openerp import api, models, fields, exceptions, _

_logger = logging.getLogger(__name__)

class PointecCron(models.Model):
    _name = 'pointec.cron'

    def daily(self, cr, uid, context=None):

        self.pool.get('pointec.cron').auto_invoice(cr, uid, context);
        self.pool.get('pointec.cron').validate_invoice_out(cr, uid, context);
        self.pool.get('pointec.cron').send_invoice(cr, uid, context);
        self.pool.get('pointec.cron').validate_invoice_in(cr, uid, context);
        self.pool.get('pointec.cron').uploadpdf_invoice(cr, uid, context);

    def auto_invoice(self, cr, uid, context=None):

        _logger.info("Recupero ordini da fatturare");

        # Recupero ordini da fatturare
        sale_orders_ids = self.pool.get('sale.order').search(cr, uid, [
            ('state', '=', "manual"),
        ])

        _logger.info("Ordini recuperati [%s]", len(sale_orders_ids));

        # Creazione fatture
        if len(sale_orders_ids)>0:
            _logger.info("Creazione fatture");
            self.pool.get('sale.order').action_invoice_create(cr, uid, sale_orders_ids, context=context)
            _logger.info("Creazione fatture completata");

    def validate_invoice_out(self, cr, uid, context=None):

        partner_bank = {
            1 : 4,      # Contrassegno
            2 : 1,      # Bonifico bancario
            3 : 2,      # Paypal
            4 : 3       # Payplug
        }

        _logger.info("Recupero fatture da validare");

        # Recupero fatture da validare
        account_invoice_ids = self.pool.get('account.invoice').search(cr, uid, [
            ('state', '=', "draft"),
            ('type', '=', "out_invoice"),
        ])

        _logger.info("Fatture recuperate [%s]", len(account_invoice_ids));

        # Loop fra tutte le fatture
        for account_invoice_id in account_invoice_ids :

            # Recupero la fattura
            account_invoice = self.pool.get('account.invoice').browse(cr, uid, account_invoice_id, context=context)
            sale_order = account_invoice.sale_ids[0]

            # Impostazione del conto corrente bancario
            partner_bank_id = partner_bank[sale_order.payment_method_id.id]

            # Impostazione journal_id
            if account_invoice.partner_id.is_company:
                journal_id = 15
            else:
                journal_id = 16

            # Modifica fattura
            data = {
                "partner_bank_id": partner_bank_id,
                "journal_id": journal_id
            }

            _logger.info("Modifica fattura [%s] %s", account_invoice_id, data);

            self.pool.get('account.invoice').write(cr, uid, account_invoice_id, data);

        # Validazione delle fatturare
        if len(account_invoice_ids)>0:
            _logger.info("Validazione fatture");
            self.pool.get('account.invoice').signal_workflow(cr, uid, account_invoice_ids, "invoice_open");
            _logger.info("Validazione fatture completata");

    def validate_invoice_in(self, cr, uid, context=None):

        partner_bank = {
            1 : 4,      # Contrassegno
            2 : 1,      # Bonifico bancario
            3 : 2,      # Paypal
            4 : 3       # Payplug
        }

        _logger.info("Recupero fatture da validare");

        # Recupero fatture da validare
        account_invoice_ids = self.pool.get('account.invoice').search(cr, uid, [
            ('state', '=', "draft"),
            ('type', '=', "in_invoice"),
        ])

        _logger.info("Fatture recuperate [%s]", len(account_invoice_ids));

        # Validazione delle fatturare
        if len(account_invoice_ids)>0:
            _logger.info("Validazione fatture");
            self.pool.get('account.invoice').signal_workflow(cr, uid, account_invoice_ids, "invoice_open");
            _logger.info("Validazione fatture completata");

    def send_invoice(self, cr, uid, context=None):

        _logger.info("Recupero fatture da mandare email");

        # Ricerca fatture da inviare
        account_invoice_ids = self.pool.get('account.invoice').search(cr, uid, [
            ('state', '=', "open"),
            ('type', '=', "out_invoice"),
            ('journal_id', '=', 15),
            ('sent', '=', False),
        ])

        _logger.info("Fatture recuperate [%s]", len(account_invoice_ids));

        # Loop fra tutte le fatture
        for account_invoice_id in account_invoice_ids :
            # Invio email
            self.pool.get('email.template').send_mail(cr, uid, 4, account_invoice_id, True);

            # Imposto la fattura come spedita
            data = {
                "sent": True,
            }

            self.pool.get('account.invoice').write(cr, uid, account_invoice_id, data);

    def uploadpdf_invoice(self, cr, uid, context=None):

        path = "/opt/files/fatture/"

        _logger.info("Recupero fatture da caricare il pdf");

        account_invoice_ids = self.pool.get('account.invoice').search(cr, uid, [
            ('type', '=', "in_invoice"),
            ('reference', '!=', False),
        ])

        _logger.info("Fatture recuperate [%s]", len(account_invoice_ids));

        # Loop fra tutte le fatture
        for account_invoice_id in account_invoice_ids :

            # Recupero la fattura
            account_invoice = self.pool.get('account.invoice').browse(cr, uid, account_invoice_id, context=context)

            source = path + account_invoice.reference
            filename = account_invoice.number.replace("/", "-") + ".pdf"

            pdf = open(source, 'rb').read()

            self.pool.get('ir.attachment').create(cr, uid, {
                'name': filename,
                'type': 'binary',
                'datas': base64.encodestring(pdf),
                'res_model': 'account.invoice',
                'res_id': account_invoice_id,
                'mimetype': 'application/x-pdf'
            })

            os.remove(source)

            # Modifica fattura
            data = {
                "reference": ""
            }

            _logger.info("Modifica fattura [%s] %s", account_invoice_id, data);

            self.pool.get('account.invoice').write(cr, uid, account_invoice_id, data);
