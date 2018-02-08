# -*- coding: utf-8 -*-

import logging
from openerp import api, models, fields, exceptions, _

_logger = logging.getLogger(__name__)

class res_partner(models.Model):
    _inherit = 'res.partner'

    def name_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        res = []
        for record in self.browse(cr, uid, ids, context=context):
            name = record.name
            if record.parent_id and not record.is_company:
                name = "%s, %s" % (record.parent_name, name)
            if context.get('show_address_only'):
                name = self._display_address(cr, uid, record, without_company=True, context=context)
            if context.get('show_address'):
                name = name + "\n" + self._display_address(cr, uid, record, without_company=True, context=context)
            name = name.replace('\n\n','\n')
            name = name.replace('\n\n','\n')
            if context.get('show_name') and record.firstname and record.lastname:
                name = "%s\n[%s]" % (name, record.firstname + " " + record.lastname)
            if context.get('show_email') and record.email:
                name = "%s\n<%s>" % (name, record.email)
            res.append((record.id, name))
        return res
