# -*- coding: utf-8 -*-
from openerp import tools
from openerp.osv import fields, osv

class SaleReport(osv.osv):
    _inherit = 'sale.report'

    _columns = {
        'mese': fields.selection([
            ('01', 'Gennaio'),
            ('02', 'Febbraio'),
            ('03', 'Marzo'),
            ('04', 'Aprile'),
            ('05', 'Maggio'),
            ('06', 'Giugno'),
            ('07', 'Luglio'),
            ('08', 'Agosto'),
            ('09', 'Settembre'),
            ('10', 'Ottobre'),
            ('11', 'Novembre'),
            ('12', 'Dicembre'),
            ], 'Mese', readonly=True),
        'shop_id':fields.many2one('sale.shop', 'Shop', readonly=True),
        'margin': fields.float('Margine', readonly=True),
        'purchase_price': fields.float('Prezzo acquisto', readonly=True),
        'is_company': fields.selection([
            (1, "Azienda"),
            (0, "Privato"),
            ], "Azienda", readonly=True),
    }

    def _select(self):
        return super(SaleReport,self)._select() + ", to_char(s.date_order, 'MM') as mese, s.shop_id, b.is_company, sum(l.margin) as margin, sum(l.purchase_price * l.product_uom_qty) as purchase_price"

    def _from(self):
        return super(SaleReport,self)._from() + " join res_partner b on s.partner_id = b.id"

    def _group_by(self):
        return super(SaleReport,self)._group_by() + ", to_char(s.date_order, 'MM'), s.shop_id, b.is_company"
