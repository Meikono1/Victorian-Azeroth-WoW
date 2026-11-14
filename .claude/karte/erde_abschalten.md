# Karte: Erde-Inhalt abschalten

Teil der Code-Karte, Index: [`KARTE.md`](../KARTE.md). Pflege wie dort.

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
