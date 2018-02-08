# -*- coding: utf-8 -*-

from openerp import http
import json
from openerp.addons.web.http import request

class Pointec(http.Controller):
    @http.route('/pointec/order/<path:order_id>', auth='public')
    def index(self, order_id, **kw):

        retval = {}
        regioncode_puntorigenera = {
            'AG' : 123,
            'AL' : 124,
            'AN' : 125,
            'AO' : 126,
            'AR' : 127,
            'AP' : 128,
            'AT' : 129,
            'AV' : 130,
            'BA' : 131,
            'BT' : 132,
            'BL' : 133,
            'BN' : 134,
            'BG' : 135,
            'BI' : 136,
            'BO' : 137,
            'BZ' : 138,
            'BS' : 139,
            'BR' : 140,
            'CA' : 141,
            'CL' : 142,
            'CB' : 143,
            'CI' : 144,
            'CE' : 145,
            'CT' : 146,
            'CZ' : 147,
            'CH' : 148,
            'CO' : 149,
            'CS' : 150,
            'CR' : 151,
            'KR' : 152,
            'CN' : 153,
            'EN' : 154,
            'FM' : 155,
            'FE' : 156,
            'FI' : 157,
            'FG' : 158,
            'FC' : 159,
            'FR' : 160,
            'GE' : 161,
            'GO' : 162,
            'GR' : 163,
            'IM' : 164,
            'IS' : 165,
            'SP' : 167,
            'AQ' : 166,
            'LT' : 168,
            'LE' : 169,
            'LC' : 170,
            'LI' : 171,
            'LO' : 172,
            'LU' : 173,
            'MC' : 174,
            'MN' : 175,
            'MS' : 176,
            'MT' : 177,
            'ME' : 179,
            'MI' : 180,
            'MO' : 181,
            'MB' : 182,
            'NA' : 183,
            'NO' : 184,
            'NU' : 185,
            'OT' : 187,
            'OR' : 188,
            'PD' : 189,
            'PA' : 190,
            'PR' : 191,
            'PV' : 192,
            'PG' : 193,
            'PU' : 194,
            'PE' : 195,
            'PC' : 196,
            'PI' : 197,
            'PT' : 198,
            'PN' : 199,
            'PZ' : 200,
            'PO' : 201,
            'RG' : 202,
            'RA' : 203,
            'RC' : 204,
            'RE' : 205,
            'RI' : 206,
            'RN' : 207,
            'RM' : 208,
            'RO' : 209,
            'SA' : 210,
            'VS' : 178,
            'SS' : 211,
            'SV' : 212,
            'SI' : 213,
            'SR' : 214,
            'SO' : 215,
            'TA' : 216,
            'TE' : 217,
            'TR' : 218,
            'TO' : 219,
            'OG' : 186,
            'TP' : 220,
            'TN' : 221,
            'TV' : 222,
            'TS' : 223,
            'UD' : 224,
            'VA' : 225,
            'VE' : 226,
            'VB' : 362,
            'VC' : 313,
            'VR' : 315,
            'VV' : 323,
            'VI' : 329,
            'VT' : 331
        }

        Invoice = http.request.env['sale.order'].browse(int(order_id))
        Partner = Invoice.partner_shipping_id

        retval["id"] = order_id
        retval["firstname"] = Partner.firstname
        retval["lastname"] = Partner.lastname
        retval["company"] = Partner.name
        retval["telephone"] = Partner.phone
        retval["email"] = Partner.email
        retval["street"] = Partner.street
        retval["postcode"] = Partner.zip
        retval["city"] = Partner.city
        retval["region_code"] = Partner.state_id.code
        retval["regioncode_puntorigenera"] = regioncode_puntorigenera[Partner.state_id.code]

        return json.dumps(retval)
