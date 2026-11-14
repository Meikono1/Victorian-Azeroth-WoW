# Code-Karte Victorian Azeroth

Wo liegt was. **Vor jeder Suche hier nachsehen**, dann nur die passende Teilkarte unter `karte/` und danach gezielt die genannten Dateien öffnen, statt Repo oder Vanilla zu durchsuchen.
Pflege: Claude trägt jede neue Datei, jedes neue System und jedes umbenannte Objekt sofort in die passende Teilkarte ein (Regel in `CLAUDE.md`, Abschnitt „Wissenspflege“). Dieser Index bleibt unter 15.000 Zeichen (`tools/va_doku_check.py`); neue Themen bekommen eine eigene Teilkarte und hier eine Zeile. Stand: 2026-11-14.

## Teilkarten (`karte/`)

| Datei | Inhalt |
|---|---|
| [`karte/content_systeme.md`](karte/content_systeme.md) | Eigener Content mit allen Objektnamen: Quel'Thalas (Mana, Todesschneise, Silvermoon-Ziele, Korridor, Wretched, Figuren), Zul'Jarra/Amani, Gilneas, Scarlet Crusade |
| [`karte/laender_wirtschaft.md`](karte/laender_wirtschaft.md) | Länder-Definitionen und -History, Regierungsformen, Herrscher, Subjekte, Machtblöcke, Kulturen, Religionen, Rassen-/Untot-Trigger, Loc; eigene Gebäude, Vanilla-Gebäude, KI, Defines, Terrain |
| [`karte/erde_abschalten.md`](karte/erde_abschalten.md) | Wie Erde-Inhalt abgeschaltet ist: Stubs, `REPLACE:`-Trigger/-Effekte, `replace_paths`, generierte Hüllen, alte Vollkopien |
| [`karte/werkzeuge.md`](karte/werkzeuge.md) | Alle Skripte in `.claude/tools/` mit Aufruf und ob sie schreiben |

Kurz die wichtigsten Werkzeuge (Aufruf immer `python -I .claude/tools/…`): `va_lint.py --regions NN` vor jeder Testrunde, `va_errlog.py --mod` für das error.log, `va_check_states.py NN` für eine Region, `va_doku_check.py` für die Doku-Größen.

Arbeitsabläufe stehen als Skills in `.claude/skills/`:

| Skill | Wofür |
|---|---|
| `va-content` | Events, JEs, Decisions, Buttons, Modifier, Loc schreiben; Vanilla-Vorbilder je Mechanik; JE-Anzeigemöglichkeiten 1.15 in `je-darstellung.md` |
| `va-testrunde` | Lint, Testfälle, error.log auswerten, Ticket abschließen |
| `va-karte` | States, Provinzen, Pops, Start-Gebäude, Ressourcen, Karten-Werkzeuge |
| `va-patch-upload` | Checklisten Patch-Wechsel und Workshop-Upload |

## Projekt-Doku (`.claude/`)

| Pfad | Inhalt | Lesen |
|---|---|---|
| `ABLAUFPLAN.md` | Fokus, offene Entscheidungen, Fahrplan, bewusste Vanilla-Overrides | Kopf bis „Fahrplan“; Rest nur bei Bedarf |
| `ERLEDIGT.md` | Erledigt-Log (Datum, Ticket, ein Satz), neueste oben | nur für Historie und Workshop-Text |
| `tickets/README.md` | **Als Nächstes** (Reihenfolge), Themen → Tickets, Übersicht der offenen Tickets | bei „nimm das nächste Ticket“ oder einem Thema zuerst hier |
| `tickets/verlauf/` | wortgleicher alter Verlauf gekürzter Tickets | nur, wenn das Ticket darauf verweist und es gebraucht wird |
| `tickets/VA-NNN-*.md` | offenes Ticket: Beschreibung, Notizen, betroffene Dateien | nur das betroffene |
| `tickets/archiv/` | erledigte und verworfene Tickets, Übersicht in `archiv/README.md` | nur, wenn die Historie gebraucht wird; nächste freie Nummer über beide Tabellen |
| `TESTPROTOKOLL.md` | Testrunden mit offenen Testfällen (`T-NNN`) | per `grep -n "^## Runde\|^### T-"` springen, nie ganz lesen |
| `TESTPROTOKOLL_ARCHIV.md` | abgeschlossene Testrunden | nur für Historie; nächste freie T-ID über beide Dateien |
| `ablauf/<land>.md` | Ablauf je Land/JE-Reihe: Entscheidungen, Mechanik, Mermaid-Diagramm, Offenes | vor Content zu diesem Land |
| `ablauf/lore/<land>.md` | Lore-Recherche zum Ablauf (Wiki, Videos) mit Quelle und Datum | nur bei Lore-Fragen |
| `karte/` | Teilkarten, siehe oben | nur die passende |
| `konzepte/`, `recherche/` | Lore-Konzepte (Quel'Thalas), Quest-Recherche | nur für Lore-Fragen |
| `laender_uebersicht.md` | Alle Länder: Charaktere, JEs, Formables, eigene Gebäude, Politik, Subjekte, Lücken (generiert von `va_country_overview.py`) | gezielt greppen (`grep -n "TAG"`), nicht ganz lesen |
| `regionen/NN_*.md` | Regionsübersicht (Ausgabe `va_region_overview.py --md`) | statt die State-Dateien zu lesen |
| `tools/` | Prüf- und Generator-Skripte, siehe `karte/werkzeuge.md` | Docstring reicht (`head -20`) |
| `tools/va_lint_baseline.txt` | 65 KB Altlasten-Liste | **nie lesen**, nur über `va_lint.py` |

## Regionen (Präfix `NN`)

Ein Präfix verbindet State-Regionen, Gebäude-History und Regionsübersicht. States, Pops und Länder-History liegen pro Kontinent.

| NN | Region | `map_data/state_regions/` | State-History | Pops (`common/history/pops/`) | Gebäude (`common/history/buildings/`) |
|---|---|---|---|---|---|
| 21 | West-Northrend | `21_va_west_northrend.txt` | `VA_northrend_state.txt` | `va_west_northrend.txt` | `21_west_northrend.txt` |
| 22 | Ost-Northrend | `22_va_east_northrend.txt` | `VA_northrend_state.txt` | `va_east_northrend.txt` | `22_east_northrend.txt` |
| 23 | Nord-Kalimdor | `23_va_north_kalimdor.txt` | `VA_kalimdor_states.txt` | `va_north_kalimdor.txt` | `23_north_kalimdor.txt` |
| 24 | Zentral-Kalimdor | `24_va_center_kalimdor.txt` | `VA_kalimdor_states.txt` | `va_center_kalimdor.txt` | `24_center_kalimdor.txt` |
| 25 | Süd-Kalimdor | `25_va_south_kalimdor.txt` | `VA_kalimdor_states.txt` | `va_south_kalimdor.txt` | `25_south_kalimdor.txt` |
| 26 | Nord-EK (Lordaeron, Quel'Thalas) | `26_va_north_eastern_kingdoms.txt` | `VA_eastern_kingdoms_states.txt` | `va_north_eastern_kingdoms.txt` | `26_north_eastern_kingdoms.txt` |
| 27 | Mittel-EK (Khaz Modan) | `27_va_center_eastern_kingdoms.txt` | `VA_eastern_kingdoms_states.txt` | `va_center_eastern_kingdoms.txt` | `27_center_eastern_kingdoms.txt` |
| 28 | Süd-EK (Stormwind) | `28_va_south_eastern_kingdoms.txt` | `VA_eastern_kingdoms_states.txt` | `va_south_eastern_kingdoms.txt` | `28_south_eastern_kingdoms.txt` |
| 29 | Outland | `29_va_outlands.txt` | `VA_outlands.txt` | `va_outlands.txt` | `29_outlands.txt` |
| 30 | West-Pandaria | `30_va_west_pandaria.txt` | `VA_pandaria.txt` | `va_west_pandaria.txt` | `30_west_pandaria.txt` |
| 31 | Ost-Pandaria | `31_va_east_pandaria.txt` | `VA_pandaria.txt` | `va_east_pandaria.txt` | `31_east_pandaria.txt` |
| 32–35 | Draenor, Lost Isles, Zandalar, Kul Tiras | `32_va_dreanor.txt` … `35_va_kul_tiras.txt` | `VA_dreanor.txt` … `VA_kul_tiras.txt` | leer | – |
| 80 | Meere | `80_va_seas.txt` | – | – | – |

Weitere Karten-Dateien: `common/strategic_regions/va_*_strategic_regions.txt` (+ alte `kalimdor_strategic_regions.txt`), `map_data/default.map`, `adjacencies.csv`, `province_terrains.txt` (560 KB, nur gezielt greppen), State-Namen `localization/replace/english/map/va_states_l_english.yml`, Namen der Strategic Regions `strategic_regions_l_english.yml` (alt, Kalimdor/Northrend/Outland) und `va_strategic_regions_l_english.yml` (VA-057, Rest), Hub-Namen `va_hub_names_l_english.yml` (168 KB, nur greppen).

## Vanilla und Script-Doku

- Vanilla: `C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game`. Jeder Ordner unter `common/` hat oft eine `*.md`-Doku (z. B. `journal_entries/journal_entries.md`, `scripted_buttons/scripted_buttons.md`, `on_actions/_on_actions.md`): die zuerst lesen.
- Script-Doku: `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\docs\`, erzeugt 2026-11-06 mit 1.15.0 (VA-063). Groß (`effects.log` 960 KB, `triggers.log` 450 KB, `modifiers.log` 960 KB), deshalb nur gezielt greppen:
  - Effekt/Trigger: `grep -n -A8 "^## <name>$" effects.log` bzw. `triggers.log`
  - Modifier: `grep -n -A4 "^<name>:" modifiers.log` (Felder `Mask`, `Name`, `Description`)
  - Scope-Wechsel: `grep -n -A4 "^### <name>$" event_targets.log`; On-Actions: `grep -n -A4 "^<name>:" on_actions.log`
  - Bei Zweifel schlägt die Verwendung in Vanilla-Dateien die Doku.
