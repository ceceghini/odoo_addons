# -*- coding: utf-8 -*-
#    Copyright (C) 2010-2017 Associazione Odoo Italia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#


from openerp import SUPERUSER_ID


def set_default_splitmode(cr, pool):
    partner_ids = pool['res.partner'].search(cr, SUPERUSER_ID, [])
    partners = pool['res.partner'].browse(cr, SUPERUSER_ID, partner_ids)
    for partner in partners:
        pool['res.partner']._default_splitmode(
            cr, SUPERUSER_ID, partner)
    return
