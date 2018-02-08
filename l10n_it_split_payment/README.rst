[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=8.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=8.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=8.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/l10n-italy/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
================================================================
   :alt: License: AGPL-3

Italian Localization - split payment
====================================

Law: http://goo.gl/1riAwt (Articolo 17 ter)

Module to generate Split Payment accounting entries

Installation
------------

























Configuration
-------------


























To configure this module, you need to:

* go to Settings, Configuration, Accounting and configure 'Split Payment Write-off account' (like 'IVA n/debito sospesa SP'). Write-off account should be different from standard debit VAT, in order to separately add it in VAT statement.
* configure the fiscal position used for split payment, setting 'Split Payment' flag. In fiscal position, map standard VAT with SP VAT, like the following:

.. image:: /l10n_it_split_payment/static/fiscal_position.png



22SPL is configured like the following:


.. image:: /l10n_it_split_payment/static/SP.png

Usage
-----









































=====

To use this module, you need to select the correct fiscal position in invoices

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/122/8.0

Known issues / Roadmap
----------------------

























Bug Tracker
-----------


























Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-italy/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/l10n-italy/issues/new?body=module:%20l10n_it_split_payment%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
-------





















































### Contributors


























* Davide Corio <davide.corio@abstract.it>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>

### Funders
### Maintainer



















































.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**Odoo Italia Associazione**, or the [Associazione Odoo Italia](https://www.odoo-italia.org/)
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017, Odoo Italia Associazione replaces OCA members of Italy are developping code under Odoo Proprietary License.
Odoo Italia Associazione distributes only code under AGPL free license.

[Odoo Italia Associazione](https://www.odoo-italia.org/) è un'Associazione senza fine di lucro
che dal 2017 sostituisce gli sviluppatori italiani di OCA che sviluppano
con Odoo Proprietary License a pagamento.

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza [AGPL](http://www.gnu.org/licenses/agpl-3.0.html)

[//]: # (end copyright)


[//]: # (addons)

[//]: # (end addons)

