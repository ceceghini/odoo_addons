# -*- coding: utf-8 -*-

import logging
from openerp import api, models, fields, exceptions, _
from openerp.osv import fields, osv

_logger = logging.getLogger(__name__)

class AccountBankStatementLine(osv.osv):
    _inherit = 'account.bank.statement.line'

    _columns = {
        'invoice_id': fields.many2one('account.invoice', "Invoice")
    }
