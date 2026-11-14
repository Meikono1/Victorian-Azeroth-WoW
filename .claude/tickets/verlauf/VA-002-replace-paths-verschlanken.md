# VA-002: replace_paths verschlanken

- **Status:** in Arbeit
- **Typ:** technik
- **Priorität:** hoch
- **Erstellt:** 2026-10-29

## Beschreibung

`events`, `events/india_events`, `events/soi_events`, `common/journal_entries`, `common/scripted_buttons`, `common/company_types`, `common/character_templates` aus `replace_paths` nehmen. Danach nur historisch-spezifische Vanilla-Dateien leer überschreiben, allgemeine Mechaniken (Wahlen, Gesetze, Streiks …) kommen wieder aktuell aus Vanilla und die eigenen Kopien in diesen Ordnern können weg.

Hinweis: `replace_paths` gilt nur für genau den Ordner, nicht für Unterordner.

## Notizen

### 2026-10-30 – Teil 1: events

- Entscheidung Kono: `events` streichen. `events`, `events/india_events`, `events/soi_events` aus `.metadata/metadata.json` entfernt.
- Neues Prüfskript `.claude/tools/va_events.py` klassifiziert jede Eventdatei, die das Spiel jetzt lädt:
  - **Erde:** `s:`/`sr:` auf States/Regionen, die der Mod nicht hat, oder Vanilla-JEs/Erde-Länder/-Kulturen/-Religionen.
  - **Allgemein:** keine solchen Verweise, oder von Hand in `GENERIC` aufgenommen (Wahlen, Gesetze, Petitionen, Attentate, Unterdrückung, Lobbys …; 32 Dateien, die Erde-Länder/-Religionen oder Vanilla-JEs nur nebenbei nennen).
- 122 neue leere Dateien schalten Vanilla-Eventdateien mit Erde-Inhalt ab (`--stubs`). 32 leere Dateien gab es schon.
- Alte Mod-Kopien bereinigt (Liste: `VA-002-events-liste.txt`): 119 Kopien allgemeiner Events gelöscht (Vanilla 1.13 lädt), 27 Kopien von Erde-Events geleert. Befehl: `python -I .claude/tools/va_events.py --apply-copies`, Kontrolle ohne Option: `kopie-allgemein (0)`, `kopie-erde (0)`. Lint danach: 0 neue Fehler.
- Bewusst behalten: `events/agitators_events/coup_events.txt` (passt zur Mod-JE-Kopie `01_coup.txt`, siehe ABLAUFPLAN „Bewusste Vanilla-Overrides“).
- Event-Verweise: Nach dem Aufräumen zeigen 211 Verweise auf Events, die nicht mehr geladen werden (vorher 133; 101 neu, 23 behoben). Fast alle stehen in den alten Mod-Kopien der On-Actions (`common/on_actions/00_*.txt`) und Mod-JE-Kopien und zeigen auf abgeschaltete Erde-Events. Das gibt einmalige Ladefehler, keinen Spam. Die On-Action-Kopien bleiben vorerst (mit Vanilla-On-Actions wären es 297), Abbau mit VA-003.
- Gilneas: `common/journal_entries/VA_gilneas_infection.txt` ruft 18 Events aus `french_pretenders` auf (Vorlage war offenbar das Vanilla-JE der französischen Thronprätendenten). Diese Events gab es im Mod schon vorher nicht → VA-007 prüfen.

### Teil 2: journal_entries und scripted_buttons (2026-10-30, umgesetzt)

- Entscheidung Kono: Teil 2 angehen. `common/journal_entries` und `common/scripted_buttons` aus `replace_paths` entfernt. Buttons mussten mit, weil die allgemeinen JEs Vanilla-Buttons brauchen (Petition, Verhandlung, Gesetzesauflage).
- Neues Prüfskript `.claude/tools/va_common_folders.py <ordner>` (gleiche Regeln wie `va_events.py`, zusätzlich Liste `EARTH` für Erde-Themen ohne direkte Verweise, und Ausgabe „ruft ungeladene Events“).
- journal_entries: 40 Vanilla-Dateien laden (darunter 19 alte Mod-Kopien gelöscht, z. B. `01_coup.txt`, `00_tutorial.txt`, Spielerziele), 132 abgeschaltet (131 Stubs, `00_acw_entries.txt` geleert). `EARTH`: Expeditionen, Krakatau, Landgewinnung, Manifest Destiny, Scramble for Africa, Dreyfus, Caudillo, Japan (Iwakura, Sakoku, Tenpo). `GENERIC`: `00_slave_owner_paranoia.txt` (schließt nur Brasilien aus).
- scripted_buttons: 3 Vanilla-Dateien laden (Petition, Verhandlung, Gesetzesauflage; Mod-Kopie `04_law_imposition_buttons.txt` gelöscht), 47 abgeschaltet (`00_scripted_buttons.txt` war eine alte Positivismus-Kopie, jetzt Stub).
- Events: `KEEP_COPY` aufgelöst, `coup_events.txt` lädt wieder aus Vanilla 1.13 (Override-Eintrag im Ablaufplan entfernt). Freigegeben: `nihilism.txt`, `silkworm_diseases.txt`, `grunderzeit.txt`, `hungry_forties.txt`, `ip4_coup_events.txt`, `negotiation_events.txt`, dazu `scotland_yard.txt` (vom allgemeinen Polizei-JE aufgerufen, feuert nur für GBR).
- Bleibt abgeschaltet: `iberia_events/ip4_election_rigging.txt` – fragt `je_coffee_with_milk` ab (Brasilien-JE, abgeschaltet). Freigabe nur, wenn man die Abfrage per eigener Datei abfängt; vorerst nicht.
- Erwartete Restfehler: Vanilla-Scripts (Gesetze, KI, Great-Game-Effekte, Spielerziel „Great Game“, Mod-Kopie `00_code_on_actions.txt`) verweisen auf Erde-JEs. Laut `error.log` vom 2026-10-30 erzeugt nur `add_journal_entry` Fehler, Abfragen wie `has_journal_entry` nicht. Die Menge ist kleiner als vorher (151 statt 107 geladene JEs). Great-Game-Ziele → VA-001 beobachten.
- `VA_gilneas_infection.txt` nutzt weiterhin `french_pretenders`-Events und -Buttons → VA-007.
- Lint: 0 neue Fehler. Tests: T-019, T-020.

### 2026-10-30 – Auswertung T-020

- **Korrektur:** Auch `has_journal_entry` auf ein nicht geladenes JE erzeugt einen Ladefehler (712× im Log, PostValidate „Invalid database object 'je_…'“). Die Aussage oben („Abfragen wie `has_journal_entry` nicht“) war falsch. Die Verweise stehen in Vanilla-Dateien (Gesetze, Ideologien, KI, Effekte, allgemeine Events). Es sind nur Ladefehler, kein Laufzeit-Spam. Lösungsidee, falls sie stören: die betroffenen Erde-JEs nicht leer abschalten, sondern als Minimal-JE ohne Inhalt behalten (`possible = { always = no }`). Entscheidung offen.
- Lücke in `va_events.py`/`va_common_folders.py`: Erkannt werden nur `s:`/`sr:`-Verweise, keine nackten `STATE_…` (z. B. `owns_entire_state_region = STATE_HOME_COUNTIES` in `scotland_yard.txt`). Nachrüsten.

### 2026-10-30 – Lücke nackte STATE_… geschlossen

- `va_events.py` (`earth_refs`, gilt auch für `va_common_folders.py`) erkennt jetzt nackte `STATE_…` ohne `s:` als harten Erde-Verweis (`s:STATE_…`).
- Wirkung: Keine Datei wechselt zwischen geladen und abgeschaltet. Nur bestehende Stubs sind jetzt sicher als Erde eingeordnet statt „stub-pruefen“: Events `belle_epoque_events.txt`; JEs `00_indian_removal.txt`, `00_reunify_china.txt`, `01_krakow.txt`, `06_the_carlist_wars.txt`. Buttons unverändert.
- `scotland_yard.txt` wäre nach der neuen Regel Erde geworden. Bleibt geladen: `STATE_HOME_COUNTIES` steht nur in der GBR-Textvariante, der Fallback ist allgemein und das allgemeine Polizei-JE ruft das Event auf. Dafür neue Ausnahmeliste `GENERIC_GEO` in `va_events.py`.
- Lint: 0 neue Fehler. Kein Spieltest nötig (nur Prüfskript, keine Mod-Dateien geändert).

### Teil 3: company_types, character_templates (2026-10-30, umgesetzt)

- Kono: „Ja, Teil 3“. Beide Ordner aus `replace_paths` entfernt. Damit stehen dort nur noch `common/history*`, `common/strategic_regions`, `map_data*`.
- **company_types:** Alle Mod-Kopien waren alter Stand vor 1.13 (alte Gebäudenamen wie `building_textile_mills`, alte Modifier). 16 Vanilla-Dateien per Stub abgeschaltet, 3 Kopien (Afrika, Österreich-Ungarn, Italien) geleert, 2 Stubs gab es schon. Mod nutzt nur `company_basic_fishing` (History Archerus).
- **Offen (Kono):** `99_basic_companies.txt` hat `--apply-copies` gelöscht, damit Vanilla 1.13 lädt. Vanilla nutzt aber die 1.13-Gebäudenamen (`building_textile_mill`, `building_steel_mill`, `building_shipyard`, `building_paper_mill`, `building_vineyard` …), die die alten Kopien in `common/buildings/0*.txt` nicht definieren → Basisfirmen ohne gültige Gebäude, bis VA-003 (buildings) erledigt ist. Vorschlag: alte Kopie bis dahin per git zurückholen (`git restore common/company_types/99_basic_companies.txt`, darf Claude nicht). Sie steht vorsorglich in `OVERRIDE` von `va_common_folders.py`, damit `--apply-copies` sie nicht erneut löscht; mit VA-003 dort austragen und Kopie löschen.
- **character_templates:** 207 Vanilla-Dateien abgeschaltet (Erde-Charaktere). Allgemein und wieder aktiv: `00_default_template.txt` (Mod-Override, s. u.), `colonial_governor_templates.txt`, `test_template.txt`. `country_kaf.txt` und `french_dynastic_template.txt` in `EARTH` (nur Erde-Kultur/-Religion).
- **Standardvorlage:** Mod-Datei hieß `default_template.txt` (alter Stand vor 1.12) und definierte `default` ein zweites Mal neben Vanilla `00_default_template.txt`. Ersetzt durch gleichnamige `00_default_template.txt`: Vanilla 1.13 unverändert plus WoW-Teile (Lebensdauer-Eigenschaft nach Volk, Staatsreligion für Hauptkultur in `on_created`). Übernommen aus 1.13: `religion = random_accepted`, `culture = ig_before_random_accepted` (vorher `ig_before_primary_culture`), `home_region`, `holding_type`, `is_adult`. Bewusster Override, im Ablaufplan eingetragen.
- `va_common_folders.py`: neue Liste `OVERRIDE` (Gruppe „override“, bleibt bei `--apply-copies`).
- Lint: 0 neue Fehler. Tests: T-021 bis T-023.

### 2026-10-30 – Nachprüfung der abgeschalteten Events (Hinweis Kono: nihilism.txt)

- `va_events.py` wertet jeden `c:`/`cu:`/`rel:`-Verweis auf Erde-Objekte als Erde, auch reine Namensverzweigungen wie `c:RUS ?= THIS` mit Fallback. Dadurch wurden allgemeine Mechaniken abgeschaltet. Von den 181 Stubs haben 69 keinen `s:`/`sr:`-Verweis; das sind die Kandidaten.
- Umgesetzt (Kono: „alle 9“): alle neun stehen in `GENERIC`. Die zwei ohne JE sind wieder aktiv (Stub gelöscht per `--apply-copies`). Die sieben mit JE stehen in der neuen Skriptgruppe `stub-wartet-je` und kommen nach Teil 2 per `--apply-copies` automatisch frei. Lint: 0 neue Fehler. Test: T-018.
- Neue Skriptgruppen: `stub-pruefen` (60 Stubs ohne `s:`/`sr:`, bei Patches durchsehen), `stub-allgemein`, `stub-wartet-je`.
- Thematisch allgemein:
  - braucht Vanilla-JE, also erst mit Teil 2 zurück: `nihilism.txt` (`je_nihilist_movement`, Auslöser nur Technik/Gesetze), `agitators_events/silkworm_diseases.txt`, `balkans_events/hungry_forties.txt`, `balkans_events/grunderzeit.txt`, `iberia_events/ip4_coup_events.txt`, `iberia_events/negotiation_events.txt`, `iberia_events/ip4_election_rigging.txt` (nennt `je_coffee_with_milk` nur im `NOT`)
  - ohne JE, sofort möglich: `agitators_events/slave_revolt_events.txt`, `iberia_events/ip4_anarchism_events.txt`
- Klar Erde trotz fehlender State-Verweise: z. B. `scotland_yard.txt` (nur `c:GBR`), `titanic_events.txt`, Indien-, Japan-, Iberien-Länderreihen, Expeditionen.
- Markierung: Rücknahme über `GENERIC` in `va_events.py` (Stub löschen, Vanilla lädt). Zusätzlich soll das Skript Stubs ohne `s:`/`sr:` als eigene Gruppe „stub-pruefen“ ausgeben, damit solche Fälle bei Patches nicht still verschwinden.
