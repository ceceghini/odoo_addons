[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=8.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=8.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=8.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/l10n-italy/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)

[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

Base xml Agenzia delle Entrate
==============================

This module has no any specific function for End-user. It is base for modules
generate xml file like FatturaPA o VAT settlement.



[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Localizzazione italiana - Definizioni per file xml
==================================================

Questo modulo non ha funzioni specifice per l'utente finale. Serve come base
per i moduli che generano file xml in formato stabilito dall'Agenzia delle
Entrate, come FatturaPA o Liquidazione IVA elettronica.

Lo schema di definizione dei file xml dell'Agenzia delle Entrate, pubblicato
con urn:www.agenziaentrate.gov.it:specificheTecniche è base per tutti i file
xml; come conseguenza nasce un conflitto tra moduli diversi con lo stesso
schema di riferimento dell'Agenzia delle Entrate con l'errore:
*name CryptoBinary used for multiple values in typeBinding*

Tutti i moduli che generano file xml per l'Agenzia delle Entrate *devono*
dipendere da questo modulo.
Per maggiori informazioni visitare il sito www.odoo-italia.org o contattare
l'autore.

### Schemi

Il modulo rende disponibili i seguenti schemi:

* Liquidazione IVA elettronica versione 1.0
* Comunicazione clienti e fornitori (spesometro 2017) versione 2.0
* FatturaPA versione 1.2


Per aggiungere nuovi schemi o modificare o aggiornare gli schemi gestiti:

- Aggiungere o modificare gli schemi nella directory ./data
- Eseguire da una macchina CentOS lo script ./pyxbgen.sh -u



### Funzionalità & Certificati

Funzione | Status | Note
--- | --- | ---
Definizione sezionale autofatture | :white_check_mark: |
Definizione sezionale corrispettivi | :white_check_mark: | Funzionalità modulo OCA duplicata
Definizione sezionale avvisi di parcella | :white_check_mark: | Necessario per modulo RA


Logo | Ente/Certificato | Data inizio | Da fine | Note
--- | --- | --- | --- | ---
[![xml_schema](https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/icons/xml-schema.png)](https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md) | [ISO + Agenzia delle Entrate](http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/) | 01-10-2017 | 31-12-2017 | Validazione contro schema xml
[![xml_schema](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/icons/fatturapa.png)](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md) | [Agenzia delle Entrate](http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/) | 05-10-2017 | 31-12-2017 | Modulo [l10n_it_vat_communication](l10n_it_vat_communication/)
[![fatturapa](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/icons/fatturapa.png)](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md) | [FatturaPA](http://www.fatturapa.gov.it/export/fatturazione/it/fattura_PA.htm) | 22-09-2017 | 31-12-2017 | Modulo [l10n_it_fatturapa](l10n_it_fatturapa/)



Installation
------------

These instruction are just an example to remember what you have to do:

    pip install PyXB==1.2.4
    git clone https://github.com/zeroincombenze/l10n-italy
    cp -R l10n-italy/l10n_it_ade ODOO_DIR/l10n-italy/
    sudo service odoo-server restart -i l10n_it_ade -d MYDB

From UI: go to Setup > Module > Install


Configuration
-------------

:mute:


Usage
-----

For furthermore information, please visit http://wiki.zeroincombenze.org/it/Odoo/7.0/man/FI


Known issues / Roadmap
----------------------

:ticket: This module replace OCA module; PR will be issued
In order to use this module you have to use:

* [l10n_it_base](l10n_it_base/) replaces OCA module


Bug Tracker
-----------

Have a bug? Please visit https://odoo-italia.org/index.php/kunena/home

Credits
-------

### Contributors

* Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
* Andrei Levin <andrei.levin@didotech.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>

### Funders

This module has been financially supported by

* SHS-AV s.r.l. <https://www.zeroincombenze.it/>
* Didotech srl <http://www.didotech.com>

### Maintainer

[![Odoo Italia Associazione](https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png)](https://odoo-italia.org)

Odoo Italia is a nonprofit organization whose develops Italian Localization for
Odoo.

To contribute to this module, please visit <https://odoo-italia.org/>.


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

