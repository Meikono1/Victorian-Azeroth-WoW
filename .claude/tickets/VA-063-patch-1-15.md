# VA-063: Patch 1.15 (1.14 übersprungen)

- **Status:** in Arbeit
- **Typ:** technik
- **Priorität:** hoch
- **Erstellt:** 2026-11-06

## Beschreibung

Spiel steht auf `1.15.0` (`launcher-settings.json`), der Mod deklariert noch `1.13.*`. Nach dem Patch startet das Spiel, das error.log wächst aber von ~2.400 auf ~16.000 Einträge in einem Start (das Log rotiert in `error.1.log` … `error.5.log`, alle vom selben Start 2026-11-06 10:09).

## Befund error.log 2026-11-06 (15.993 Einträge)

| Anteil | Ursache | Lösung |
|---|---|---|
| ~7.600 | **Neu in 1.15:** `common/travel_network/naval_network.txt` (Vanilla, 11.000 Seeweg-Knoten der Erde). Daraus `Invalid or non-sea province for a naval node` (4.089), `Referencing non-existent province!` in Datei `""` (~3.300, Zeilennummern = Knoten der Datei), `Harbor node N has no port node` (168) | Eigenes Netz erzeugen: Konsole `TravelNetworkTools.GenerateNavalNetwork all` (Debug-Modus) schreibt `Documents\…\Victoria 3\generated\naval_network.txt` → ins Repo als `common/travel_network/naval_network.txt`. Ebenso vorhanden: `TravelNetworkTools.GenerateHarborLocators`, `TravelNetworkTools.CheckHubAnchorProvinces` |
| 3.888 | `common/flag_definitions/00_flag_definitions.txt` Z. 74, 98, 99, 120: Liste `DEFAULT` (gilt für jedes Land, 972 Prüfungen) fragt Erde-States ab (`s:STATE_KUBAN`, `STATE_RIGA` …) | Datei in `va_gen_earth_overrides.py` aufnehmen; das Werkzeug muss dafür `flag_definition`-Blöcke zweiter Ebene mit unbekannten States streichen können |
| 287 | **JE-Format geändert:** `complete`/`on_complete`, `fail`/`on_fail`, `invalid`/`on_invalid`, `timeout`/`on_timeout` gibt es nicht mehr, ersetzt durch `outcome = { header effect_header conclusion_desc flags trigger effect }` (Vanilla `common/journal_entries/journal_entries.md` ab Z. 134) | Betroffen: `va_earth_je_stubs.txt` (268, über `va_gen_earth_je_stubs.py`), `VA_silvermoon.txt` (13), `va_dead_scar.txt` (4), `va_mana.txt` (2). Umstellung auf `outcome`, Loc-Keys für `conclusion_desc` nötig |
| Rest | Alte Bekannte und kleinere Vanilla-Erde-Bezüge (`99_ru_custom_loc_V3.txt` PHL 137, `00_default_strategy.txt`, `00_dynamic_country_names.txt`, `rlit_cluster*`-Events, `00_company_charter_types.txt` …) | Nach den drei großen Blöcken neu auswerten |

## Checkliste (Skill `va-patch-upload`)

- [x] `supported_game_version` → `1.15.*` (2026-11-06)
- [x] Kono: `script_docs` ausführen (2026-11-06), `KARTE.md`- und `CLAUDE.md`-Hinweis aktualisiert
- [ ] Bewusste Vanilla-Overrides (`ABLAUFPLAN.md`) gegen 1.15 vergleichen
- [ ] `00_defines.txt` auf neue Provinz-/State-IDs prüfen
- [ ] Neue Vanilla-Ordner/-Dateien mit Erde-Bezug (bisher gefunden: `common/travel_network/`)
- [x] Neue Pflichtfelder/Formate in Ordnern mit eigenen Objekten: JE `outcome` umgestellt (2026-11-06); andere Ordner noch nicht systematisch geprüft
- [x] `va_events.py --details`, `va_common_folders.py` für JEs, Scripted Buttons, Company Types, Character Templates (2026-11-06)
- [x] Hüllen neu erzeugen (Geo-Regionen, JE-Stubs, Event-Stubs, Template-Stubs, Overrides; 2026-11-06)
- [x] Lint alle Regionen: 0 neue Fehler (2026-11-06)
- [ ] Vanilla-Vorbilder prüfen, Stand-Zeile aktualisieren
- [ ] Testrunde mit Kampagnenstart und error.log-Auswertung
- [ ] `gfx/map/`-Altkopien gegen Vanilla diffen (VA-059)

## Notizen

- 2026-11-06: Erstauswertung (siehe Tabelle). Unsere `map_data/nodes.dat` ist eine eigene Fassung (2026-01-29), nicht Vanilla; ob 1.15 sie noch nutzt oder nur noch `naval_network.txt`, ist offen.
- 2026-11-06: `TravelNetworkTools.GenerateNavalNetwork all` wird in der Konsole geblockt (vermutlich nur mit Startoption `-debug_mode`). Fallback: eigener Generator in Python aus `provinces.png` (Format der Vanilla-Datei: `nodes={ {province= x= y= type=sea|harbor|sea_from_spline} … }`, danach Kanten `{from= to=}`).
- 2026-11-06: Auch mit `-debug_mode` geblockt (Kono), der Befehl ist offenbar nur für Entwickler. Erster Schritt: `common/travel_network/naval_network.txt` als leere Datei (T-091), um zu sehen, ob Schiffe ohne Netz noch Wege finden. Wenn nicht: Python-Generator (`.claude/tools/va_naval_network.py`, geplant).
- 2026-11-06: Flaggen: `va_gen_earth_overrides.py` kennt jetzt Pfad-Schlüssel (`flag_definition/trigger`) und überspringt Kommentare beim Klammerzählen. `common/flag_definitions/00_flag_definitions.txt` erzeugt (22 Trigger in 9 Listen auf `always = no`, davon 7 in `DEFAULT`); die übrigen Override-Dateien dabei aus Vanilla 1.15 neu erzeugt. Lint: 0 neue Fehler. Test T-092.
- 2026-11-06, Kono-Test: 4.249 Einträge beim Start, 4.307 nach einem Jahr. Flaggen bis auf 2 Zeilen weg. Leeres Seewege-Netz: keine naval-Zeilen mehr, dafür ~150× `hq.cpp … no coastal state … has a port travel position` → eigenes Netz nötig (Generator). Größter Rest: JE-Stubs (268, `outcome`-Umstellung), `99_ru_custom_loc_V3.txt` (169), `00_default_strategy.txt` (~80), `00_dynamic_country_names.txt` (~75), `rlit_cluster*`-Events (74), `00_company_charter_types.txt` (~80). Mod-Kopie `gfx/map/spline_network/military_route_graphics/03_naval_vehicles.txt` nennt nicht mehr vorhandene Einheiten (`combat_unit_type_frigate`, `_destroyer`) → VA-059.
- 2026-11-06: Seefahrt mit leerem Netz geht (Kono, T-091 OK); `hq.cpp`-Meldungen bleiben, Generator vorerst nicht nötig. `gfx/map/spline_network/military_route_graphics/` gelöscht (Kopie aus INIT 2023, Vanilla heißt jetzt `route_graphics`), Test T-093. In `gfx/map/spline_network` liegen noch alte `roadpaved*.dds` (Vanilla: `road_paved_*`) und mit Vanilla identische `.dds`/`game_road_data.txt` → VA-059.
- 2026-11-06: JEs auf `outcome` umgestellt: `VA_silvermoon.txt` (4 JEs), `va_dead_scar.txt`, `va_mana.txt`; Standard-Loc-Keys aus Vanilla (`je_standard_*`, `JOURNAL_ENTRY_TIMEOUT*`), keine neue Loc. `je_silvermoon_zul_aman` bekam ein leeres timeout-outcome (seit 1.15 Pflicht). JE-Hüllen-Generator: neue Vorlage mit `disable_evaluation` + verstecktem `invalid_outcome`, Regex nur noch erste Spalte (eingerückte `je_tsarpoints_add_partial` waren als JE gezählt). 294 JE-Hüllen.
- 2026-11-06: Neue Vanilla-Erde-Dateien abgeschaltet (IP5 Russland/Polen, Zarenpunkte, `rlit_cluster*`, Erde-Charaktervorlagen, `00_companies_ip5.txt`). `va_events.py --stubs` hatte zunächst auch allgemeine Mechanik erfasst (Revolutionen, Industrieunfälle, Gesellschafts-Technik, Lobbys, Gesetze …), weil die neuen Russland-JEs noch nicht als Hülle existierten → diese 12 Stubs wieder gelöscht, `autocracy_events.txt` (nur `cu:russian`-Sonderzweig) in `GENERIC`. Offen: `stub-allgemein` `events/iberia_events/ip4_election_rigging.txt` (schon vorher, Tool empfiehlt Löschen) und 126 `mod-ohne-vanilla`-Eventdateien (alte Vanilla-Namen?). Test T-095.
- 2026-11-06: Mod-Version in `.metadata/metadata.json` auf `2` (Kono). Upload-Checkliste noch nicht durchlaufen.
- 2026-11-06: Neues Gut Kupfer → VA-064. Unsere `capped_resources` mit `bg_…`-Namen laden in 1.15 weiter ohne Meldung. Neue optionale State-Felder in Vanilla (`state_regions.md`): `prime_land`, `min_/max_cold_effect`, `blockade_locator`, `diorama_radius_multiplier`.
