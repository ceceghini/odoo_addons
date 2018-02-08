[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=8.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=8.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=8.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/l10n-italy/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
================================================================
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

Reverse Charge IVA
==================


Module to handle reverse charge IVA on supplier invoices.

Il modulo permette di automatizzare le registrazioni contabili derivate
dalle fatture fornitori intra UE ed extra UE mediante il reverse charge IVA.
Inoltre è automatizzata la procedura di annullamento e riapertura della fattura
fornitore.

E' anche possibile utilizzare la modalità "con autofattura fornitore aggiuntiva".
Questo tipicamente è usato per i fornitori extra UE, con lo scopo di mostrare,
nel registro IVA acquisti, una fattura intestata alla propria azienda,
che verrà poi totalmente riconciliata con l'autofattura attiva, sempre intestata alla
propria azienda

**NOTA**: al momento è gestito solo il metodo **Autofattura** e non quello
**Integrazione IVA**.

Installation
------------



Configuration
-------------




To configure this module, you need to:

create tax **22% intra UE** Vendita:

.. figure:: /l10n_it_reverse_charge/static/description/tax_22_v_i_ue.png
   :alt: 22% intra UE Vendita
   :width: 600 px

create tax **22% intra UE** Acquisti:

.. figure:: /l10n_it_reverse_charge/static/description/tax_22_a_i_ue.png
  :alt: 22% intra UE Acqisti
  :width: 600 px

create reverse charge **Autofattura**:

.. figure:: /l10n_it_reverse_charge/static/description/rc_selfinvoice.png
  :alt: reverse charge con Autofattura
  :width: 600 px

create reverse charge **Autofattura ExtraCee** :

.. figure:: /l10n_it_reverse_charge/static/description/rc_selfinvoice_extra.png
  :alt: reverse charge con Autofattura
  :width: 600 px

with transitory account created as follows:

.. figure:: /l10n_it_reverse_charge/static/description/temp_account_auto_inv.png
  :alt: conto transitorio Autofattura
  :width: 600 px

Self Invoice Payment Journal, in Default Debit Account and Default Credit Account must have the Self Invoice Transitory Account.

Then, in fiscal position, set the 'RC Type'

.. figure:: /l10n_it_reverse_charge/static/description/fiscal_pos_intra.png
  :alt: Impostazione posizioni fiscali Intra CEE
  :width: 600 px

Example :
**1)** Intra CEE Autofattura e stampa sui registri con Ragione sociale del
    fornitore. Es. imponibile 100 iva 22 .

.. figure:: /l10n_it_reverse_charge/static/description/exemple1_0.png
  :alt: Esempio 1
  :width: 600 px

scritture generate

.. figure:: /l10n_it_reverse_charge/static/description/exemple1_1.png
  :alt: Esempio 1
  :width: 600 px

.. figure:: /l10n_it_reverse_charge/static/description/exemple1_2.png
  :alt: Esempio 1
  :width: 600 px

.. figure:: /l10n_it_reverse_charge/static/description/exemple1_3.png
  :alt: Esempio 1
  :width: 600 px

.. figure:: /l10n_it_reverse_charge/static/description/exemple1_4.png
  :alt: Esempio 1
  :width: 600 px

**2)** Extra CEE Autofattura e stampa sui registri con Ragione sociale
del'azienda. Es. imponibile 200 iva 44 .

.. figure:: /l10n_it_reverse_charge/static/description/exemple2_0.png
  :alt: Esempio 2
  :width: 600 px

scritture generate

.. figure:: /l10n_it_reverse_charge/static/description/exemple2_1.png
  :alt: Esempio 2
  :width: 600 px

.. figure:: /l10n_it_reverse_charge/static/description/exemple2_2.png
  :alt: Esempio 2
  :width: 600 px

.. figure:: /l10n_it_reverse_charge/static/description/exemple2_3.png
  :alt: Esempio 2
  :width: 600 px

.. figure:: /l10n_it_reverse_charge/static/description/exemple2_4.png
  :alt: Esempio 2
  :width: 600 px

**3)** Extra CEE Autofattura e stampa sui registri con Ragione sociale
del'azienda senza che il fornitore venga riportato sui registri. La prima
scritture generata è senza iva. Es. imponibile 50 iva 11 .

.. figure:: /l10n_it_reverse_charge/static/description/exemple3_0.png
  :alt: Esempio 3
  :width: 600 px

.. figure:: /l10n_it_reverse_charge/static/description/exemple3_6.png
  :alt: Esempio 3
  :width: 600 px

scritture generate

.. figure:: /l10n_it_reverse_charge/static/description/exemple3_1.png
  :alt: Esempio 3
  :width: 600 px

.. figure:: /l10n_it_reverse_charge/static/description/exemple3_2.png
  :alt: Esempio 3
  :width: 600 px

.. figure:: /l10n_it_reverse_charge/static/description/exemple3_3.png
  :alt: Esempio 3
  :width: 600 px

.. figure:: /l10n_it_reverse_charge/static/description/exemple3_4.png
  :alt: Esempio 3
  :width: 600 px

.. figure:: /l10n_it_reverse_charge/static/description/exemple3_5.png
  :alt: Esempio 3
  :width: 600 px

Usage
-----



















=====

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/122/8.0

Known issues / Roadmap
----------------------



Bug Tracker
-----------




Bugs are tracked on `GitHub Issues
<https://github.com/OCA/l10n-italy/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
-------




Images

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.






### Contributors




* Davide Corio <davide.corio@abstract.it>
* Alex Comba <alex.comba@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com

### Funders
### Maintainer







.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.

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

