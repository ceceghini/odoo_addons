[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy.svg?branch=8.0)](https://travis-ci.org/Odoo-Italia-Associazione/l10n-italy)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/l10n-italy/badge.svg?branch=8.0)](https://coveralls.io/github/Odoo-Italia-Associazione/l10n-italy?branch=8.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/l10n-italy/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/l10n-italy/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

[![icon](static/src/img/icon.png)](https://travis-ci.org/zeroincombenze)

Italian Localization - Spesometro2017
=====================================

Generate xml file for sending to Agenzia delle Entrate, kwnown as Spesometro.



[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Localizzazione Italiana - Spesometro2017
========================================

Gestisce la Comunicazione periodica IVA con l'elenco delle fatture emesse e
ricevute e genera il file da inviare all'Agenzia delle Entrate.
Questo obbligo è conosciuto anche come Spesometro 2017 e sostistuisce il
precedente obbbligo chiamato Spesometro.


### Funzionalità & Certificati

Funzione | Status | Note
--- | --- | ---
Fatture clienti e fornitori detraibili | :white_check_mark: | Fatture ordinarie
Fatture fornitori indetraibili | :white_check_mark: | Tutte le percentuali di indetraibilità
Fatture a privati senza Partita IVA| :white_check_mark: | Necessario codice fiscale
Fatture semplificata | :white_check_mark: | Per clienti senza PI ne CF
Fatture senza IVA | :white_check_mark: | Fatture esenti, NI, escluse, eccetera
Escludi importi Fuori Campo IVA | :white_check_mark: | Totale fattura in Comunicazione può essere diverso da registrazione
Escludi CAP e provincia no Italia in comunicazione | :white_check_mark: | Da nazione, oppure da partita IVA oppure Italia
Escludi CF no Italia in comunicazione | :white_check_mark: | Da nazione, oppure da partita IVA oppure Italia
Controlli dati anagrafici | 
Conversione ISO-Latin1 | :white_check_mark: | Evita rifiuto partner stranieri
IVA differita | :white_check_mark: | Da codice imposte
IVA da split-payment | :white_check_mark: | Da codice imposte
Ignora autofatture | :white_check_mark: | Esclusione tramite sezionale
Ignora corrispettivi | :white_check_mark: | Esclusione tramite sezionale
Ignora avvisi di parcella | :white_check_mark: | Esclusione tramite sezionale
Identificazione Reverse Charge | :white_check_mark: | Da codice imposte
Fatture vendita UE | :white_check_mark: | Inserite in spesometro
Fatture vendita extra-UE | :white_check_mark: | Inserite in spesometro
Fatture acq. intra-UE beni | :x: | In fase di rilascio
Fatture acq. intra-UE servizi | :white_check_mark: | Tutte le fatture EU (provvisoriamente)
Rettifica dichiarazione | :x: | In fase di rilascio
Nomenclatura del file | :white_check_mark: |
Dimensioni del file | :x: | Nessuna verifica anche futura

Logo | Ente/Certificato | Data inizio | Da fine | Note
--- | --- | --- | --- | ---
[![xml_schema](https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/icons/xml-schema.png)](https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md) | [ISO + Agenzia delle Entrate](http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/) | 01-10-2017 | 31-12-2017 | Validazione contro schema xml
[![xml_schema](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/icons/fatturapa.png)](https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md) | [Agenzia delle Entrate](http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Strumenti/Specifiche+tecniche/Specifiche+tecniche+comunicazioni/Fatture+e+corrispettivi+ST/) | 05-10-2017 | 31-12-2017 | File accettati da portale fatturaPA Agenzia delle Entrate


Installation
------------

These instruction are just an example to remember what you have to do:

    pip install PyXB==1.2.4
    pip install Unidecode
    git clone https://github.com/zeroincombenze/l10n-italy
    for module in l10n_it_base l10n_it_ade l10n_it_fiscalcode l10n_it_vat_communication account_invoice_entry_date; do
        mv ODOO_DIR/l10n-italy/$module BACKUP_DIR/
        cp -R l10n-italy/$module ODOO_DIR/l10n-italy/
    sudo service odoo-server restart -i l10n_it_ade -d MYDB

From UI: go to Setup > Module > Install


Configuration
-------------

:it:

* Contabilità > Configurazione > Sezionali > Sezionali :point_right: Impostare sezionali autofatture
* Contabilità > Configurazione > Imposte > Imposte :point_right: Impostare natura codici IVA
* Contabilità > Clienti > Clienti :point_right: Impostare nazione, partita IVA, codice fiscale e Cognome/nome
* Contabilità > Fornitori > Fornitori :point_right: Impostare nazione, partita IVA, codice fiscale e Cognome/nome
* Contabilità > Elaborazione periodica > Fine periodo > Comunicazione :point_right: Gestione Comunicazione e scarico file xml


Usage
-----

For furthermore information, please visit http://wiki.zeroincombenze.org/it/Odoo/7.0/man/FI



Known issues / Roadmap
----------------------

:ticket: This module replaces OCA module; PR have to be issued.
In order to use this module you have to use:

:warning: Use [l10n_it_base](l10n_it_base/) replacing OCA module

:warning: Use [l10n_it_ade](l10n_it_ade/) module does not exist in OCA repository

:warning: Use [l10n_it_fiscalcode](l10n_it_fiscalcode/) replacing OCA module


Bug Tracker
-----------

Have a bug? Please visit https://odoo-italia.org/index.php/kunena/home


Credits
-------

### Contributors

* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
* Andrei Levin <andrei.levin@didotech.com>

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

