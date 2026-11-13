# Code-Karte Victorian Azeroth

Wo liegt was. **Vor jeder Suche hier nachsehen**, danach gezielt die genannten Dateien öffnen statt das Repo oder Vanilla zu durchsuchen.
Pflege: Claude trägt jede neue Datei, jedes neue System und jedes umbenannte Objekt sofort hier ein (Regel in `CLAUDE.md`, Abschnitt „Wissenspflege“). Stand: 2026-11-03.

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
| `ABLAUFPLAN.md` | Fahrplan, offene Entscheidungen, Fokus, Erledigt-Log, bewusste Vanilla-Overrides, Checklisten | Kopf bis „Fahrplan“; Rest nur bei Bedarf |
| `tickets/README.md` | Ticket-Übersicht (Status-Tabelle) | Tabelle statt einzelner Tickets durchsuchen |
| `tickets/VA-NNN-*.md` | offenes Ticket: Beschreibung, Notizen, betroffene Dateien | nur das betroffene |
| `tickets/archiv/` | erledigte und verworfene Tickets | nur, wenn die Historie gebraucht wird |
| `TESTPROTOKOLL.md` | Testrunden mit offenen Testfällen (`T-NNN`) | per `grep -n "^## Runde\|^### T-"` springen, nie ganz lesen |
| `TESTPROTOKOLL_ARCHIV.md` | abgeschlossene Testrunden | nur für Historie; nächste freie T-ID über beide Dateien |
| `ablauf/<land>.md` | Mermaid-Ablauf je Land/JE-Reihe | vor Content zu diesem Land |
| `konzepte/`, `recherche/` | Lore-Konzepte (Quel'Thalas), Quest-Recherche | nur für Lore-Fragen |
| `laender_uebersicht.md` | Alle Länder: Charaktere, JEs, Formables, eigene Gebäude, Politik, Subjekte, Lücken (generiert von `va_country_overview.py`) | gezielt greppen (`grep -n "TAG"`), nicht ganz lesen |
| `regionen/NN_*.md` | Regionsübersicht (Ausgabe `va_region_overview.py --md`) | statt die State-Dateien zu lesen |
| `tools/` | Prüf- und Generator-Skripte, siehe unten | Docstring reicht (`head -20`) |
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

## Länder, Kulturen, Religionen

| Was | Dateien |
|---|---|
| Länder-Definitionen | `common/country_definitions/VA_eastern_kingdom.txt` (108 Tags), `VA_kalimdor.txt` (120), `VA_outlands.txt` (87). `00_countries.txt`, `01_africa.txt`, `01_pacific_and_australasia.txt` sind alte Vanilla-Kopien mit Erde-Tags (VA-003). Northrend/Pandaria haben noch keine eigenen Länder. |
| Länder-History | `common/history/countries/va_eastern_kingdom_countries.txt`, `va_kalimdor_countries.txt`, `va_outland_countries.txt`, `va_decentralized_countries.txt` (Kontinent-Tags `NRTHRND`, `KALIMDOR` …) (`COUNTRIES = { c:TAG ?= { … } }`) |
| Regierungsformen | `common/government_types/00_va_monarchies.txt` (`gov_archmage`, `gov_va_regency_quel_thalas` für Silvermoon; `00_`, damit vor Vanilla geprüft), Loc `va_goverment_l_english.yml`; übrige Dateien im Ordner sind erzeugt (`va_gen_earth_overrides.py`) |
| Herrscher | `common/history/characters/va_eastern_kingdom.txt`; Vorlagen `common/character_templates/va_*_charakters.txt`, Standardvorlage `00_default_template.txt` (bewusster Override) |
| Subjekte, Diplomatie | `common/history/diplomacy/va_subject_relationships.txt` (übrige `va_*` leer) |
| Machtblöcke (VA-065) | `common/history/power_blocs/00_power_blocs.txt` (Blöcke, Start-Leverage Horde/Allianz), Start-Verteidigungspakte `common/history/treaties/00_historical_treaties.txt`, Anführer-Modifier `common/static_modifiers/va_power_bloc_modifiers.txt` (`va_warchief_of_the_horde`, gesetzt in `va_kalimdor_countries.txt`), Loc `va_power_blocs_l_english.yml`. Anführer muss Major Power sein, Austritt ab Leverage-Vorteil ≤ 30 |
| Kulturen | `common/cultures/va_<volk>_cultures.txt` (34 Dateien), Start-Fervor `common/history/cultures/va_cultures.txt` |
| Kultur-Merkmale | `common/discrimination_traits/va_*.txt` (Heritage, Sprache, Tradition), Gruppen `common/discrimination_trait_groups/va_*.txt` |
| Religionen | `common/religions/religion.txt` (Name von Vanilla, Inhalt WoW) |
| Pflicht-Modifier je Kultur/Religion | `common/static_modifiers/va_culture_modifiers.txt` (93 KB), `va_religion_modifiers.txt`, Typen `common/modifier_type_definitions/va_culture_religion_modifier_types.txt` (alles generiert, nur greppen) |
| Rassen-Trigger | `common/scripted_triggers/va_racial_triggers.txt` (`is_elven`, `is_dwarven`, …) |
| Untot-Prüfung (zentral) | `va_undead_triggers.txt` (`va_is_undead_culture_trigger`, `va_country_undead_primary_trigger`, `va_state_undead_majority_trigger`), Wert `common/script_values/va_undead_values.txt` (`va_state_undead_share`) |
| Kleidung | `common/scripted_triggers/va_clothes_triggers.txt` (VA-042) |
| Loc | `localization/replace/english/va_countries_l_english.yml`, `va_cultures_…`, `va_culture_traits_…`, `va_religions_…`, Namenslisten `va_male/female/last_names_…` (60–70 KB, nur greppen) |

## Systeme (eigener Content)

### Quel'Thalas: Mana (VA-019)
Gut `mana` (`common/goods/va_goods.txt`, Icon `gfx/interface/icons/goods_icons/va_mana.dds`), Bedarf `common/pop_needs/va_pop_needs.txt`, Gebäude `building_leyline_tap` (`common/buildings/va_mana_buildings.txt`, PMG/PM `va_mana_production_method_groups.txt` / `va_mana_production_methods.txt`: Stufen Focus Crystals → Arcane Conduits → Runic Resonators, Zusatz Attunement/Arcane Sigils, Typen `va_mana_modifier_types.txt`).
JE `je_mana_hunger` (`common/journal_entries/va_mana.txt`) → `va_update_mana_dependency_effect` (`va_mana_effects.txt`) setzt eine von `va_mana_abundance` / `va_mana_scarcity` / `va_mana_withdrawal` (`va_mana_modifiers.txt`). Trigger `va_country_mana_dependent_trigger`, `va_is_mana_dependent_culture_trigger` (`va_mana_triggers.txt`). Loc `va_mana_l_english.yml`.

### Quel'Thalas: Todesschneise (VA-019) und Heilung (VA-046)
Start: `common/history/global/va_global_quel_thalas.txt` markiert State-Regionen mit Variable `va_dead_scar_region` und verteilt die Start-JEs.
Prüfung: `common/on_actions/va_on_actions_quel_thalas.txt` (monatlich, `on_state_owner_change`, `on_state_created`) → `va_update_dead_scar_effect` (`va_quel_thalas_effects.txt`) → Modifier `va_dead_scar`, `va_dead_scar_living`, `va_dead_scar_land_restored` (`va_quel_thalas_modifiers.txt`). Trigger `va_state_on_dead_scar_trigger`.
Heilung: JE `je_va_dead_scar` (`va_dead_scar.txt`), je Region Schalter `va_dead_scar_start/stop_<region>_button` (`va_dead_scar_buttons.txt`), Balken `va_dead_scar_bar_<region>` (`va_dead_scar_progress_bars.txt`), Monatsprüfung `va_dead_scar_heal_pulse_effect` (`va_dead_scar_effects.txt`), Gebäude `building_va_scar_ward` + `pm_ritual_circles_building_va_scar_ward` (`va_dead_scar_*`), Events `dead_scar_events.1–2` (`events/va_dead_scar_events.txt`), Loc `va_dead_scar_regions_l_english.yml`.
**Buttons, Balken und Heil-Effekt sind generiert** von `.claude/tools/va_gen_dead_scar.py`: dort ändern und neu erzeugen, nicht von Hand.
Sichtbare Schneise (VA-062): unsichtbares `building_va_dead_scar` (100 Stufen, `va_dead_scar_buildings.txt`) → Manipulator `va_dead_scar` (`common/terrain_manipulators/00_va_terrain_manipulators.txt`) → Gelände `va_dead_scar_land` (`common/terrain/va_terrain.txt`) unter der Schneise in `gfx/map/masks/mask_dynamic_mining.png` (geteilt mit Minen; eigene Masken kennt das Spiel nicht). Form: `.claude/regionen/va_dead_scar_form.png`. Anlegen/Abreißen in `va_update_dead_scar_effect`, Schrumpfen `va_dead_scar_set_level_effect`. Feste Schneise in `gfx/map/terrain/mask_devastation_mud_01.png` entfernt Kono je Region im Map-Editor.
Regionen: Sunwell Plateau, Ruins of Silvermoon, West Sanctum, East Sanctum, Tranquillien, Deathholme. Deathholme ohne Ritual (VA-062): `va_update_deathholme_scourge_effect` (generiert, `va_dead_scar_effects.txt`, Aufruf `on_monthly_pulse` in `va_on_actions_quel_thalas.txt`) gibt `c:DEATHHOLME` den Modifier `va_deathholme_scourge_tide` × Script-Wert `va_dead_scar_cursed_regions` (`common/script_values/va_dead_scar_values.txt`, generiert), Schneise dort schrumpft mit (20 Stufen je Region), bei 0 geheilt. Trigger `va_state_on_healable_dead_scar_trigger` (ohne Deathholme) für JE und Schalter.

Mana-Grundbedarf: `va_mana_upkeep` (State, `va_mana_modifiers.txt`), Wert `va_state_mana_upkeep` / `va_mana_upkeep_per_100k` (`common/script_values/va_mana_values.txt`), Effekt `va_update_mana_upkeep_effect` (`va_mana_effects.txt`). Maßnahmen: Schalter `va_mana_disenchant/rationing_start/rationing_stop_button`, `va_mana_drain_<region>_button` (`va_mana_buttons.txt`), Effekte `va_mana_*_effect` (`va_mana_relief_effects.txt`), Faktor `va_country_mana_relief_factor`, Disenchantment-Werkstatt `building_va_disenchantment` (`va_mana_buildings.txt`, Gruppe `bg_va_disenchantment`, PM in `va_mana_production_method*.txt`), Modifier `va_mana_disenchant_shame`, `va_mana_rationing`, `va_mana_fauna_drained/depleted/recovering`.

### Silvermoon-Ziele (VA-020), Korridor (VA-047), Wretched (VA-021)
JEs `je_silvermoon_deathholme`, `je_silvermoon_zul_aman`, `je_silvermoon_corridor` (`common/journal_entries/VA_silvermoon.txt`), Modifier `va_silvermoon_*` (`va_silvermoon_modifiers.txt`), Events `silvermoon_events.2–5` (`events/va_silvermoon_events.txt`), Global-Variable `va_amani_claims_shattered`.
Korridor: Button `va_silvermoon_corridor_start_button`, Balken `va_silvermoon_corridor_bar`, Effekte `va_silvermoon_corridor_*_effect`, Trigger `va_silvermoon_corridor_*_trigger` (jeweils `va_silvermoon_corridor_*.txt`). Loc `va_silvermoon_l_english.yml`, `va_quel_thalas_l_english.yml`. Ablauf `.claude/ablauf/silvermoon.md`.
Wretched (VA-021): JE `je_silvermoon_wretched` (`VA_silvermoon.txt`), Schalter `va_silvermoon_wretched_pact/annex/heal_button`, Balken `va_silvermoon_wretched_bar` und `va_silvermoon_wretched_threat_bar` (Bedrohung), Effekte `va_silvermoon_wretched_*_effect`, Trigger `va_silvermoon_wretched_partner/mana_supplied/sunsail_open_trigger` (jeweils `va_silvermoon_wretched_*.txt`), Events `wretched_events.1–5`, Raub-Events `.10–.15`, Eroberung `.16`, Angriff bei Bedrohung 100 `.17` (Effekt `va_silvermoon_wretched_frenzy_effect`, Trigger `va_silvermoon_wretched_frenzy_target_trigger`, Modifier `va_wretched_frenzy_1–3`, Variable `va_wretched_frenzy_cooldown`) (`events/va_wretched_events.txt`), Modifier `va_wretched_addiction`, `va_wretched_addicts` (`va_wretched_modifiers.txt`) und `va_silvermoon_wretched_*`, `va_silvermoon_unsafe_road/harbor_overrun/wall_breach/apprentices_disciplined/kinslaying_war/kinslaying_scars` (`va_silvermoon_modifiers.txt`), Variablen `va_wretched_united`, `va_wretched_absorbed`, `va_wretched_raid_cooldown`, `va_wretched_apprentice_cooldown`, State-Region `va_wretched_homeland`. Loc `va_wretched_l_english.yml`. Ablauf `.claude/ablauf/wretched.md`.
Wretched Schritt 2–4 (VA-021): Sucht-Stufen und Heil-Etappen `va_wretched_addiction_effects.txt` (Variablen `va_wretched_addiction_level`, `va_wretched_heal_stage`, `va_wretched_last_level`; Modifier `va_wretched_addiction_1/2/3`, `va_wretched_supervised_withdrawal/clarity/homesick`), Kopfgeld und Zerfall `va_silvermoon_wretched_bounty_effects.txt` (Schalter `va_silvermoon_wretched_bounty_<anführer>_button`, Variablen `va_wretched_hunt_<anführer>`, `va_wretched_<anführer>_slain`, `va_wretched_leaderless`), Anführer-Vorlagen `common/character_templates/va_wretched_characters.txt` (erzeugt in `history/characters/va_eastern_kingdom.txt`), Mana-Aufstand `va_mana_uprising_effects.txt` (Zähler `va_mana_shortage_months`, aufgerufen aus `va_update_mana_dependency_effect`). Events `wretched_heal_events.*`, `wretched_bounty_events.*`, `mana_uprising_events.*` (je eigene Datei in `events/`). Loc `va_wretched_story_l_english.yml`.

### Quel'Thalas-Figuren (VA-016, VA-066)
Vorlagen `va_qt_lorthemar_theron`, `va_qt_rommath`, `va_qt_halduron_brightwing`, `va_qt_liadrin` (Silvermoon), `va_qt_auriferous`, `va_qt_mavren` (Tranquillien), `va_qt_darkhan_drathir` (Deathholme), `va_qt_zuljin`, `va_qt_malacrass` (Zul'Jarra) in `common/character_templates/va_quel_thalas_characters.txt`; Abfragen `va_has_halduron/rommath/liadrin_trigger` (`va_quel_thalas_character_triggers.txt`), Liadrin-Bonus `va_liadrin_ritual_wardens_effect` (`va_quel_thalas_character_effects.txt`) → Modifier `va_silvermoon_blood_knight_wardens`, erzeugt in `history/characters/va_eastern_kingdom.txt`, Namen `va_quel_thalas_characters_l_english.yml`. Gemischte Pops Quel'Thalas: Kopfkommentar in `common/history/pops/va_north_eastern_kingdoms.txt` (VA-049). Startbevölkerung Vanilla gegen Mod (alle Länder, States, Kulturen, Sklaven): `.claude/regionen/bevoelkerung_vanilla_vs_mod.md`, erzeugt von `.claude/tools/va_pop_report.py`.

### Zul'Jarra / Amani (VA-022, VA-017)
Träger `AMANI_TRIBE`, Stämme `SHADOWPINE_TRIBE`, `MOSSFLAYER_TROLLS`. JEs `je_amani_tribes/loa/siege/empire/vengeance` (`common/journal_entries/va_amani.txt`, Start in `va_global_quel_thalas.txt`), Schalter `va_amani_shadowpine/mossflayer_button`, `va_amani_loa_<loa>_button` (`va_amani_buttons.txt`), Balken `va_amani_shadowpine_bar`, `va_amani_loa_bar` (`va_amani_bars.txt`), Effekte `va_amani_*_effect` (`va_amani_effects.txt`), Trigger `va_amani_*_trigger` (`va_amani_triggers.txt`), Modifier `va_amani_*` (`va_amani_modifiers.txt`), Schatzjäger `va_on_actions_amani.txt` (`on_monthly_pulse_country`). Events `amani_events.*`, `amani_loa_events.*`, `amani_treasure_events.*` (je eigene Datei in `events/`). Variablen `va_amani_shadowpine/mossflayer_joined`, `va_amani_tribes_gathered/failed`, `va_amani_loa_decided`, `va_amani_loa_wrath`, `va_amani_siege_over`, Global `va_amani_claims_shattered`. Loc `va_amani_l_english.yml`. Ablauf `.claude/ablauf/amani.md`. Formable `AMANI_EMPIRE` (Amani Empire): Formation `common/country_formation/va_formable_countries.txt` (13 States, 0,69 = 9 nötig, freigeschaltet über `va_amani_empire_restored`), Definition `VA_eastern_kingdom.txt`, Wappen `common/coat_of_arms/coat_of_arms/va_amani_coat_of_arms.txt`.

### Gilneas: Worgen-Infektion (VA-007, alt)
JE `je_infected_gilnean` (Platzhalter ohne Ziel) in `common/journal_entries/VA_gilneas_infection.txt`, Gruppe `je_group_gilneas_infection` (`common/journal_entry_groups/VA_journal_entries.txt`), Event `gilnean_infection_events.1` in `events/gilneas_events/infection_events.txt`, Modifier `gilneas_infection_unrest` (`va_event_modifiers.txt`), Loc `localization/replace/english/events/va_gilneas_events_l_english.yml`.

### Scarlet Crusade (VA-035, VA-041)
Nur geplant: `.claude/ablauf/scarlet_crusade.md`.

### Wirtschaft und KI
| Was | Dateien |
|---|---|
| Eigene Gebäude | `common/buildings/20_Victorian_Azeroth.txt` (`building_feliron_mine`, `building_eternium_mine`), `va_monument_buildings.txt` (`building_dark_portal`, PMG in `production_method_groups/va_monument_production_method_groups.txt`), `va_mana_buildings.txt`, `va_dead_scar_buildings.txt`, Gruppen `va_building_groups.txt` (`bg_feliron_mining`, `bg_eternium_mining`, …), Loc `va_buildings_l_english.yml` |
| Vanilla-Gebäude/PMs | Alte Vollkopien `common/buildings/01_…13_*.txt`, `production_methods/[01]*`, `production_method_groups/[01]*`, `building_groups/00_building_groups.txt` sind zum Löschen freigegeben (VA-043, Kono löscht); danach gilt Vanilla 1.13. History und `map_data` nutzen die echten 1.13-Namen; Vanilla-Aliase (`building_textile_mills`) gelten dort nicht |
| KI | `common/ai_strategies/va_default_strategy.txt`, `common/history/ai/va_ai_strategy.txt`, `va_ai_triggers.txt` (REPLACE) |
| Defines | `common/defines/va_OVERWRITE_defines.txt` (`WORLD_MARKET_LOCATION`) |
| Terrain | Provinz-Terrain `map_data/province_terrains.txt` (erzeugt von `va_terrain.py`), eigene Typen `common/terrain/va_terrain.txt` (`va_underwater` für Vashj'ir), Loc `va_terrain_l_english.yml`; dynamische Masken `gfx/map/masks/mask_dynamic_*.png` (EK gemalt, Rest leer, VA-061), gleiche Kopie für den Map-Editor in `tools/mapeditor/mask_painter/` (schreiben die Masken-Skripte mit) (VA-051) |
| Charakter-Traits | `common/character_traits/va_traits.txt` |
| Sonstiges | `common/scripted_effects/VA_scripted_effects.txt` (Dublette eines Vanilla-Effekts, zum Löschen freigegeben, VA-043) |

## Erde-Inhalt abschalten

| Mittel | Wo |
|---|---|
| Leere gleichnamige Dateien (Stubs, < 200 B) | ca. 670 Dateien, v. a. `character_templates`, `journal_entries`, `events/*`, `scripted_buttons`, `company_types`, `decisions`, `history`. Erzeugt von `va_events.py` / `va_common_folders.py --stubs` |
| Trigger auf „nie wahr“ (`REPLACE:`) | `va_earth_triggers.txt` (s:/sr: auf Erde-States), `va_geography_triggers.txt` (Erde-Kontinente) |
| Effekte leer (`REPLACE:`) | `common/scripted_effects/va_earth_effects.txt` (Great Game, Orientkrise, Balkan-Beute, Ezo, Indien) |
| `replace_paths` | `.metadata/metadata.json`: `common/history/*`, `common/strategic_regions`, `map_data` |
| Leere Hüllen gleichen Namens (generiert) | `common/geographic_regions/0*.txt` (175 Erde-Regionen, `va_gen_geo_regions.py`), `common/journal_entries/va_earth_je_stubs.txt` (294 Erde-JEs, `va_gen_earth_je_stubs.py`), `common/character_templates/va_earth_template_stubs.txt` (341 Erde-Vorlagen, `va_gen_earth_template_stubs.py`), `events/va_earth_event_stubs/` (483 aufgerufene Erde-Events, `va_gen_earth_event_stubs.py`), `08_monuments.txt`, `10_canals.txt`, `power_bloc_names/00_power_bloc_names.txt`, `political_movements/03_pan_national_movements.txt`, `government_types/01_monarchies/01_regencies/01_social_monarchies/05_council_republics.txt`, `achievements/*.txt`, `flag_definitions/00_flag_definitions.txt` (Vanilla mit `always = no`, `va_gen_earth_overrides.py`): Vanilla-Verweise bleiben gültig; `common/travel_network/naval_network.txt` (leer, Erde-Seewege seit 1.15, VA-063) |
| Festungs-Locators | `gfx/map/map_object_data/fortification_locators.txt` (eigene, bewusst leere Datei statt Vanillas Erde-Positionen, VA-060) |
| On-Action-Trigger | `common/on_actions/va_on_actions_earth.txt` (`historical_agitators_yearly_events` aus) |
| Bewusste Vollkopien | Liste im `ABLAUFPLAN.md` unter „Bewusste Vanilla-Overrides“ |
| Alte Vollkopien (Abbau VA-003) | u. a. `country_definitions/00_countries.txt`, `01_africa.txt`, `events/`, `gfx/map/` (VA-059), `buildings/`, `production_methods/` (Löschung offen, VA-043). On-Actions, Bewegungen, Scripted Effects, Flaggen, Custom Loc, Terrain: gelöscht 2026-11-03 |

## Werkzeuge (`.claude/tools/`, Aufruf immer `python -I`)

| Skript | Zweck | Schreibt? |
|---|---|---|
| `va_lint.py [--regions NN …]` | Prüfung vor jeder Testrunde (BOM, Loc, Verweise, Duplikate, States) | nein |
| `va_errlog.py [--mod] [--top N] [--filter TEXT] [--by-file]` | error.log zusammenfassen; `--mod` nur Quelldateien aus dem Repo (9.581 → 967 Einträge) | nein |
| `va_check_states.py NN` | State-Region gegen Karte, History, Pops, Gebäude, Länder | nein |
| `va_region_overview.py NN [--md DATEI]` | Regionsübersicht je State (Besitzer, Pops, Ackerland, Gebäude) | nur `--md` |
| `va_events.py`, `va_common_folders.py <ordner>` | Vanilla-Dateien als Erde/allgemein/WoW einstufen, Stubs anlegen | mit `--stubs`/`--apply-copies` |
| `va_fill_buildings.py NN [--apply]` | Start-Gebäude auffüllen (Profile in `va_profiles.py`) | mit `--apply` |
| `va_add_gov_buildings.py`, `va_add_ports.py`, `va_add_trade_centers.py` | Verwaltung/Bausektor, Häfen, Handelszentralen ergänzen | mit `--apply` |
| `va_country_overview.py [--md DATEI] [--tag TAG]` | Länderübersicht (Charaktere, JEs, Formables, eigene Gebäude, Politik, Subjekte, fehlende Namen/Flaggen) | nur `--md` |
| `va_icon.py QUELLE ZIEL.dds [--size N] [--keep-aspect]` | Bild → Vic3-Icon (DDS BGRA mit Mipmaps wie Vanilla), Quellen in `.claude/grafik_quellen/` (VA-027); `--keep-aspect` für Event-Bilder (Breite N, z. B. 1280) | ja |
| `va_gen_dead_scar.py` | Todesschneisen-Buttons, -Balken, -Effekt erzeugen | ja |
| `va_terrain.py NN … [--png DATEI] [--apply]` | Provinz-Terrain aus Geländetexturen und Heightmap ableiten → `province_terrains.txt` (VA-051) | mit `--apply` |
| `va_dynamic_masks.py NN … [--masks …] [--clear] [--png ORDNER] [--apply]` | Dynamische Masken `gfx/map/masks/mask_dynamic_farmland/forestry/mining.png` je Region aus Terrain und Ressourcen malen, `--clear` leert die ganze Karte (VA-051) | mit `--apply` |
| `va_scar_mask.py NN STATE_… [--fill xRRGGBB …] [--free-others] [--scar-only] [--remove] [--apply]` | Todesschneise je State aus der Vorlage `.claude/regionen/va_dead_scar_form.png` in `mask_dynamic_mining.png` malen, `--fill` bemalt ganze Provinzen, `--free-others` leert dort Farmland/Forst, `--scar-only` lässt in den States nur die Schneise in der Bergbau-Maske (VA-062). Nach jedem `va_dynamic_masks.py`-Lauf über Region 26 erneut mit allen Optionen laufen lassen (Befehl im Ticket VA-062) | mit `--apply` |
| `va_gen_geo_regions.py [--apply]` | leere Erde-`geographic_regions` erzeugen (bei Patches) | mit `--apply` |
| `va_gen_earth_je_stubs.py [--apply]` | nie aktivierbare Hüllen für abgeschaltete Erde-JEs (bei Patches, nach neuen Stubs) | mit `--apply` |
| `va_gen_earth_template_stubs.py [--apply]` | leere Hüllen für aufgerufene Erde-Charaktervorlagen | mit `--apply` |
| `va_gen_earth_event_stubs.py [--apply]` | versteckte Hüllen für abgeschaltete Erde-Events → `events/va_earth_event_stubs/` | mit `--apply` |
| `va_gen_earth_overrides.py [--apply]` | Vanilla-Dateien mit Erde-States in oft geprüften Bedingungen entschärft übernehmen (Liste `FILES`: Monumente, Kanäle, Machtblock-Namen, Pan-Bewegungen, Erde-Regierungsformen, Errungenschaften, Flaggen; erkennt States, `sr:` und `c:`-Tags; Schlüssel als Pfad `flag_definition/trigger` für zweite Ebene) | mit `--apply` |
| `va_release_stats.py [--ref R] [--save V] [--compare V]` | Inhaltszahlen je Release (JEs, Events, Modifier, Texte, Wörter, AI WRITTEN …; zählt nur Namen, die Vanilla nicht kennt). Stände in `.claude/releases/version_*.json`, Basis `2025-12` | mit `--save` |
| `va_script.py` | Bibliothek: Paradox-Script-Parser, wirksame Datei (Mod über Vanilla) | – |

## Vanilla und Script-Doku

- Vanilla: `C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game`. Jeder Ordner unter `common/` hat oft eine `*.md`-Doku (z. B. `journal_entries/journal_entries.md`, `scripted_buttons/scripted_buttons.md`, `on_actions/_on_actions.md`): die zuerst lesen.
- Script-Doku: `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\docs\`, erzeugt 2026-11-06 mit 1.15.0 (VA-063). Groß (`effects.log` 960 KB, `triggers.log` 450 KB, `modifiers.log` 960 KB), deshalb nur gezielt greppen:
  - Effekt/Trigger: `grep -n -A8 "^## <name>$" effects.log` bzw. `triggers.log`
  - Modifier: `grep -n -A4 "^<name>:" modifiers.log` (Felder `Mask`, `Name`, `Description`)
  - Scope-Wechsel: `grep -n -A4 "^### <name>$" event_targets.log`; On-Actions: `grep -n -A4 "^<name>:" on_actions.log`
  - Bei Zweifel schlägt die Verwendung in Vanilla-Dateien die Doku.
