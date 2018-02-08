# -*- coding: utf-8 -*-

import logging, base64, os
from openerp import api, models, fields, exceptions, _

_logger = logging.getLogger(__name__)

class PointecPointec(models.Model):
    _name = 'pointec.pointec'

    def validate_invoice(self, cr, uid, ids, context=None):
        self.pool.get('account.invoice').signal_workflow(cr, uid, ids, "invoice_open");
        return True;

    def process_reconciliation(self, cr, uid, id, mv_line_dicts, context=None):
        self.pool.get('account.bank.statement.line').process_reconciliation(cr, uid, id, mv_line_dicts, context=context);
        return True
