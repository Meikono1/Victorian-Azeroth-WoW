# Vanilla-Vorbilder je Mechanik

Pfade relativ zu `C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game`. Kleine Dateien zuerst, Zeilenzahl in Klammern. Geprüft für 1.13.11 (2026-11-01).
Neues Vorbild gefunden → hier eintragen (Pflege durch Claude).

## Doku-Dateien in Vanilla (zuerst lesen)

`common/journal_entries/journal_entries.md`, `common/scripted_buttons/scripted_buttons.md`, `common/scripted_progress_bars/scripted_progress_bars.md`, `common/on_actions/_on_actions.md`, `common/diplomatic_plays/diplomatic_plays.md`, `common/buildings/buildings.md`, `common/production_methods/production_methods.md`, `common/goods/goods.md`, `common/modifier_type_definitions/modifier_types.md`, `common/script_values/script_values.md`, `common/political_movements/political_movements.md`, `common/laws/readme.md`.

## Events

| Mechanik | Datei | Objekt / Stelle |
|---|---|---|
| Country-Event, Optionen, Bild, Flavor | `events/land_reclamation.txt` (119) | `land_reclamation.1` |
| State-Event | `events/paralegal_discrimination_events.txt` (171) | `type = state_event` |
| Charakter erzeugen | `events/ethiopia.txt` (65) | `create_character`, Z. 45 |
| Diplomatic Play aus Event | `events/iberia_events/ip4_lusosphere_events.txt` (405) | `create_diplomatic_play`, Z. 394 |
| Neues Land abspalten | `events/brazil/brazilian_minors.txt` (418) | `create_country` |
| Subjekt machen | `events/brazil/patagonia_events.txt` (96) | `create_diplomatic_pact = { … type = <subjekttyp> }` |
| Angebot an anderes Land, Antwort per Event, KI-Gewichtung | `events/romania_events.txt` | `romania.1`/`.2`, `ai_chance = { base modifier = { trigger add } }` |
| Land friedlich annektieren | `events/canada_australia_events.txt` | `annex_with_incorporation = <land>` (`can_aus.1`) |
| JE-Balken aus Event ändern bzw. abfragen | `events/agitators_events/algeria_events.txt`, `events/brazil/misc_events.txt` | `je:<je> ?= { add_progress = { value = 15 name = <bar> } }`, Abfrage `je:<je> ?= { "scripted_bar_progress(<bar>)" >= 50 }` |
| Zufalls-Events im JE mit bedingten Gewichten | `common/journal_entries/00_plague.txt` | `random_list = { 10 = { modifier = { if = { limit = { … } add = -10 } } trigger_event = … } }` |
| Zufallsevents per On-Action | `common/on_actions/00_on_actions_half_yearly.txt` (93) | `random_events = { chance_to_happen = … 40 = event.id }` |
| Event mit Verzögerung aus JE | `common/journal_entries/00_request_recognition.txt` (74) | `trigger_event = { id = … days = … }` |
| Custom-Loc (Text je Bedingung) | `common/customizable_localization/02_events.txt` | `type = country` + `text = { trigger … localization_key … }` |

## Journal Entries

| Mechanik | Datei | Objekt / Stelle |
|---|---|---|
| Besitz-Ziel mit Timeout, Modifier-Belohnung | `common/journal_entries/00_sick_man.txt` (419) | `je_sick_man_syria` |
| Markt-/Preisabfrage, Dauer-JE | `common/journal_entries/00_corn_laws.txt` (74) | `market_goods_pricier`, `mg:` |
| JE + Progress Bar | `common/journal_entries/00_request_recognition.txt` (74), `05_technocracy.txt` (76) | `scripted_progress_bar = …` |
| Mehrere Balken in einem JE | `common/journal_entries/00_antarctica.txt` | `expedition_progress_bar`, `expedition_peril_progress_bar` |
| JE + Scripted Button | `common/journal_entries/02_amazonas.txt` (63), `01_krakow.txt` (66) | `scripted_button = …` |
| `is_progressing` | `common/journal_entries/02_brazil_navy.txt` (138) | `is_progressing` |
| Status-Text | `common/journal_entries/00_ig_suppression.txt` (73) | `status_desc` |
| State-Region-Zustand | `common/journal_entries/00_land_reclamation.txt` (66) | State-Region-Abfragen |
| JE-Gruppen | `common/journal_entry_groups/00_journal_entries.txt` | `je_group_historical_content`, `je_group_internal_affairs` |

## Buttons, Balken, Modifier

| Mechanik | Datei | Objekt / Stelle |
|---|---|---|
| Button mit Einmalkosten | `common/scripted_buttons/00_hispaniola_buttons.txt` | `je_haitian_debt_payment_button` (Z. 43) |
| Progress Bar (Land-Scope) | `common/scripted_progress_bars/00_greece_progress_bars.txt` | `monthly_progress` ohne `owner` |
| Progress Bar (Expedition) | `common/scripted_progress_bars/00_victoria_progress_bars.txt` | `expedition_progress_bar` (Z. 644) |
| Static Modifier für Events | `common/static_modifiers/02_event_modifiers.txt` | Icons `timed_modifier_icons/…` |
| Belohnung/Malus aus JE | `common/static_modifiers/content_3_modifiers.txt` | `sick_man_of_europe`, `dead_man_of_europe` |
| Modifier-Namen und -Typen | `docs/modifiers.log` (900 KB, nur greppen), `common/modifier_type_definitions/01_building_modifier_types.txt` | |

## Decisions, Formables, Diplomatie

| Mechanik | Datei | Objekt / Stelle |
|---|---|---|
| Einfache Decision | `common/decisions/korea_decisions.txt` (25) | `KOR_declare_korean_empire` |
| Decision mit Provinzwechsel | `common/decisions/canal_decisions.txt` (357) | `set_owner_of_provinces`, Z. 144 |
| Formable (normal) | `common/country_formation/00_formable_countries.txt` | |
| Major Formation | `common/country_formation/00_major_formables.txt` (296) | |
| Diplomatic-Play-Typen | `common/diplomatic_plays/00_diplomatic_plays.txt` | |
| War Goals | `common/war_goal_types/` | |

## Wirtschaft

| Mechanik | Datei | Objekt / Stelle |
|---|---|---|
| Rohstoff-Gebäude | `common/buildings/03_mines.txt` | `building_coal_mine` |
| Gebäude, PMG, PM | `common/production_method_groups/03_mines.txt`, `common/production_methods/03_mines.txt` | |
| Handel | `common/buildings/11_private_infrastructure.txt` | `building_trade_center` |
| Gut | `common/goods/00_goods.txt` | `coal` |
| Pop-Bedarf | `common/pop_needs/00_pop_needs.txt` | `popneed_stimulants` |
| Script-Wert (Summe über States) | `common/script_values/building_values.txt` | `every_scope_state`, `divide = state_population` |

## On-Actions und History

| Mechanik | Datei | Objekt / Stelle |
|---|---|---|
| Code-On-Actions (Liste aller Hooks) | `common/on_actions/00_code_on_actions.txt`, `docs/on_actions.log` | `on_monthly_pulse_state`, `on_state_owner_change`, `on_state_created` |
| Globale Start-History | `common/history/global/00_global.txt` | `GLOBAL = { … }` |
| Länder-History | `common/history/countries/` (z. B. `fra - france.txt`) | |
| Gebäude-History (Maßstab) | `common/history/buildings/` (Frankreich 1836) | |
| Charakter-Vorlage Agitator / General | `common/character_templates/country_arg.txt`, `country_ald.txt` | `is_agitator = yes` mit `ideology`, `is_general = yes`; erzeugen per `create_character = { template = … }` in `history/characters`, finden per `has_template` |
| Land abspalten und zurückerobern | `events/brazil/brazilian_minors.txt`, `events/british_raj_events.txt` | `create_country = { tag origin state on_created }`, danach `create_diplomatic_play = { target_country type = dp_annex_war handle_annexation_as_civil_war = yes }` |
| Verwüstung | `events/paris_commune_events.txt` | `add_devastation = 30` (State oder State-Region) |
