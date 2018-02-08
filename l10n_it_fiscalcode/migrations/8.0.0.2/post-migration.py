# -*- coding: utf-8 -*-
#    Copyright (C) 2010-2017 Associazione Odoo Italia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#

from openerp.addons.l10n_it_fiscalcode.post_install\
    import set_default_splitmode
from openerp import pooler


def migrate(cr, version):
    """Post-install script.
    If version is not set, we are called at installation time."""
    if not version:
        return

    pool = pooler.get_pool(cr.dbname)
    set_default_splitmode(cr, pool)
