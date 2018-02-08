# -*- coding: utf-8 -*-

import logging
from openerp import api, models, fields, exceptions, _

_logger = logging.getLogger(__name__)

class AccountInvoice(models.Model):
    _inherit = 'account_invoce'
