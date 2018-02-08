# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2015-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#
#################################################################################
from openerp.osv import fields, osv
class sale_shop(osv.osv):
	_name = "sale.shop"
	_description = "Sales Shop"
	_columns = {
	    'name': fields.char('Shop Name', size=64, required=True),
	}
sale_shop()

class sale_order(osv.osv):
	_inherit = "sale.order"

	_columns = {     
			'shop_id':fields.many2one('sale.shop', 'Shop')
	}

sale_order()