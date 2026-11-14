# Karte: Länder, Kulturen, Wirtschaft, KI

Teil der Code-Karte, Index: [`KARTE.md`](../KARTE.md). Pflege wie dort.

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

## Wirtschaft und KI
| Was | Dateien |
|---|---|
| Eigene Gebäude | `common/buildings/20_Victorian_Azeroth.txt` (`building_feliron_mine`, `building_eternium_mine`), `va_monument_buildings.txt` (`building_dark_portal`, PMG in `production_method_groups/va_monument_production_method_groups.txt`), `va_mana_buildings.txt`, `va_dead_scar_buildings.txt`, Gruppen `va_building_groups.txt` (`bg_feliron_mining`, `bg_eternium_mining`, …), Loc `va_buildings_l_english.yml` |
| Vanilla-Gebäude/PMs | Alte Vollkopien `common/buildings/01_…13_*.txt`, `production_methods/[01]*`, `production_method_groups/[01]*`, `building_groups/00_building_groups.txt` sind zum Löschen freigegeben (VA-043, Kono löscht); danach gilt Vanilla 1.13. History und `map_data` nutzen die echten 1.13-Namen; Vanilla-Aliase (`building_textile_mills`) gelten dort nicht |
| KI | `common/ai_strategies/va_default_strategy.txt`, `common/history/ai/va_ai_strategy.txt`, `va_ai_triggers.txt` (REPLACE) |
| Defines | `common/defines/va_OVERWRITE_defines.txt` (`WORLD_MARKET_LOCATION`) |
| Terrain | Provinz-Terrain `map_data/province_terrains.txt` (erzeugt von `va_terrain.py`), eigene Typen `common/terrain/va_terrain.txt` (`va_underwater` für Vashj'ir), Loc `va_terrain_l_english.yml`; dynamische Masken `gfx/map/masks/mask_dynamic_*.png` (EK gemalt, Rest leer, VA-061), gleiche Kopie für den Map-Editor in `tools/mapeditor/mask_painter/` (schreiben die Masken-Skripte mit) (VA-051) |
| Charakter-Traits | `common/character_traits/va_traits.txt` |
| Sonstiges | `common/scripted_effects/VA_scripted_effects.txt` (Dublette eines Vanilla-Effekts, zum Löschen freigegeben, VA-043) |
