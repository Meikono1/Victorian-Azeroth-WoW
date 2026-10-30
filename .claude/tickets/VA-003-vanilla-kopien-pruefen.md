# VA-003: Verbleibende Vanilla-Kopien abbauen

- **Status:** in Arbeit
- **Typ:** aufraeumen
- **Priorität:** hoch
- **Erstellt:** 2026-10-29

## Beschreibung

Stand nach Aufräumen 2026-10-29: 326 Dateien weichen von gleichnamigen Vanilla-1.13-Dateien ab, 63 leere Dateien schalten Vanilla ab (bleiben), 15 identische Kopien liegen in replace_paths-Ordnern (bis VA-002 nötig).

Ordnerweise vorgehen: `on_actions` → `scripted_effects/triggers` → `laws` → `buildings`/`production_methods(_groups)` → `interest_groups`/`ideologies` → Events. Echte WoW-Änderungen in `va_`-Dateien oder per `INJECT` verschieben, Rest löschen oder leer überschreiben. Bewusste Vollkopien in ABLAUFPLAN.md eintragen.

## Notizen

- 2026-10-29: Automatische Klassifizierung in `VA-003-klassifizierung.txt`: 7 Kopien mit WoW-Bezeichnern (behalten), ~340 ohne (Kandidaten), 85 in replace_paths-Ordnern. Grenze: Die Prüfung erkennt nur hinzugefügte Zeilen, nicht bewusst entfernte.
- 2026-10-29: Runde 2 gelöscht (37 Dateien): `interest_groups` (8), `ideologies` (5), `laws` (8), `government_types` ohne `01_monarchies` (5), `gfx/portraits/portrait_modifiers` (6), `ai_strategies` (5). Git-Historie zeigt nur Update-Commits, keine gezielten Kürzungen.
- Noch übrig aus diesen Ordnern: `common/laws/readme.md` (Vanilla-Doku-Kopie), `portrait_modifiers/01_shrink_body.txt` und `01_weight.txt` (bis auf Leerzeichen identisch mit Vanilla).
- 2026-10-29: Runde 3 – `cultures`/`discrimination_traits`/`discrimination_trait_groups`. Die WoW-Einträge (34 Heritages, 36 Sprachen, 229 Traditionen, 14 religiöse Heritages, 80 Gruppen) liegen jetzt in `va_cultural_heritages.txt`, `va_languages.txt`, `va_traditions.txt`, `va_religious_heritages.txt`, `va_cultural_heritage_groups.txt`, `va_language_groups.txt`, `va_religious_heritage_groups.txt`. Vanilla-Einträge in den Kopien waren unverändert (außer alten Gruppen bei `language_batak`/`language_dayak`).
  - Kollision: WoW-`language_naga` überschrieb Vanillas indische Naga-Sprache. Umbenannt in `language_nazja` (Naga-Sprache der Lore), `va_naga_cultures.txt` angepasst. Loc für WoW-Sprachen fehlt generell (→ VA-006-Umfeld).
  - Erledigt 23:05 (Kono hat gelöscht). Vorher **offen (Kono):** alte Kopien löschen, sonst doppelte Einträge: `common/cultures/00_cultures.txt`, `common/discrimination_traits/00_cultural_heritages.txt`, `01_languages.txt`, `02_traditions.txt`, `03_religious_heritages.txt`, `common/discrimination_trait_groups/00_cultural_heritage_groups.txt`, `01_language_groups.txt`, `02_religious_heritage_groups.txt`. Danach lädt Vanillas Kulturliste inkl. `griqua` usw.
- 2026-10-29: `scripted_triggers` geprüft (Block-Vergleich mit Vanilla 1.13.11). Alle 7 Kopien sind alter Stand, jeder fehlen 5–53 neue Vanilla-Trigger.
  - Bewusst entschärft waren nur: 10 Trigger in `00_geography_triggers.txt` (Erde-Regionen entfernt) und 4 `has_je_*_reason` in `00_ai_triggers.txt` (Erde-JEs). Die liegen jetzt als `REPLACE:` in `va_geography_triggers.txt` und `va_ai_triggers.txt`, dazu die 7 leeren `state_is_in_*`-Stubs für alte Kopien in `terrain`/`dynamic_country_map_colors`. Ob `REPLACE:` bei Scripted Triggers greift, zeigt der nächste Test (sonst tauchen Fehler aus Vanilla-`00_geography_triggers.txt` auf).
  - **Offen (Kono):** löschen: `common/scripted_triggers/00_ai_triggers.txt`, `00_clothes_triggers.txt`, `00_coa_triggers.txt`, `00_geography_triggers.txt`, `00_gfx_route_graphics_triggers.txt`, `00_scripted_triggers.txt`, `00_victoria_scripted_triggers.txt`. `00_gfx_buildings_graphics_triggers.txt` bleibt (bewusster Override).
- 2026-10-29: Kono hat die 7 `scripted_triggers`-Kopien gelöscht.
- 2026-10-29: `buildings` geprüft. Alle 13 Kopien sind alter Stand. 1.13 hat Industrie-Gebäude umbenannt (`building_textile_mills` usw. sind in Vanilla nur noch `aliases`), `01_industry.txt` definiert die alten Namen neu → 279× fehlende Loc. Außerdem Subsistenz- und Militärgebäude anders aufgeteilt. WoW-eigen: `building_dark_portal` (08_monuments), `building_gold_fields`, `building_vineyard_plantation` (nur alter Stand?), alles in `20_Victorian_Azeroth.txt`. Vor dem Löschen prüfen, welche alten Gebäudenamen History/`map_data` noch benutzen (State-Ressourcen `bg_*`, Building-History).
- 2026-10-30 (Log Runde 4): Die alten Kopien unter `common/buildings/0*.txt` verdecken 1.13-Gebäude, die Vanilla-Scripts jetzt wieder brauchen (JEs/Events aus VA-002): `building_barrack` 50×, `building_art_academy` 30×, `building_naval_administration` 19×, `building_steel_mill` 17×, `building_munition_plant`, `building_textile_mill`, `building_chemical_plant` u. a. Ebenso fehlen Scripted Effects aus 1.13 (`rebind_prestige_good_company`, `exile_character_with_role_cleanup`, `resign_and_retire`), vermutlich wegen der alten Kopie `common/scripted_effects/00_scripted_effects.txt`. Buildings und Scripted Effects sind damit die nächsten Ordner für den Abbau.
