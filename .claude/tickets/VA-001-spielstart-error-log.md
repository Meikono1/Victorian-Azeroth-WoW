# VA-001: Spielstart mit Mod und error.log auswerten

- **Status:** in Arbeit
- **Typ:** technik
- **Priorität:** hoch
- **Erstellt:** 2026-10-29

## Beschreibung

Kono startet Victoria 3 (1.13.11) mit dem Mod bis in eine Kampagne und führt in der Konsole `script_docs` aus. Claude wertet danach `logs\error.log` aus und legt pro Fehlerursache ein Ticket an.

Achtung: `map_data/provinces.png` wurde im Jan. 2026 korrigiert, die State-Region-Dateien nicht. Auf Meldungen zu nicht zugeordneten Provinzen achten.

## Notizen

### 2026-10-29 – erster Start (Upload-Ordner, Stand vor dem Aufräumen)

- Hauptmenü erreicht, **Absturz beim Laden der Kampagne** (22:30:36). Letzte Zeile in `game.log`: `world_market.cpp: Failed to assign province, error: Referencing non-existent province!`
- ~31.000 Zeilen in `error.log` (5× rotiert).
- Absturz-Kandidaten:
  - Vanilla `common/strait_definitions/strait_definitions.txt` (neu seit 1.12/1.13, nicht überschrieben): Panama-/Suez-Kanal usw. verweisen auf 8 Provinzen, die es im Mod nicht gibt → VA-012
  - 12 Provinzen in `common/history/states/VA_*.txt` liegen laut Spiel in mehreren State Regions (`create_state … crossing multiple state regions`), vermutlich Folge der Kartenkorrektur Jan. 2026 → VA-011
- Größte Fehlergruppen (noch nicht abgearbeitet): `common/ideologies/01_character_ideologies.txt:212` (1950×), `leader`-Scope leer (975×), `has_role` mit `agitator`/`general` (Rollen in 1.13 geändert), Vanilla-`iberia_events`/`japan_events` mit Erde-States, `bg_*_WIP`-Ressourcen in State Regions, Lokalisierung mit `’` in Namens-Keys.
- Geprüft: Die `replace_paths` greifen. In `events`, `company_types`, `journal_entries`, `character_templates`, `scripted_buttons` gibt es 480 Vanilla-Dateien ohne Mod-Gegenstück, keine davon erzeugt Fehler. Die Company-Fehler kommen aus den eigenen Kopien mit Inhalt (`00_companies_italy/africa/austria_hungary.txt`, `99_basic_companies.txt`).
### 2026-10-29 – Absturzursache

- Crash-Bericht `crashes/victoria3_01260929_223037`: `EXCEPTION_ACCESS_VIOLATION`, keine Symbole. Eine Sekunde vorher: `world_market.cpp: Failed to assign province`.
- Ursache: Vanilla 1.13 `common/defines/00_defines.txt` → `NEconomy.WORLD_MARKET_LOCATION = "x9137A4"` (Nordatlantik). Gibt es auf Azeroth nicht.
- Fix: `common/defines/va_OVERWRITE_defines.txt` → `WORLD_MARKET_LOCATION = "x74FAFA"` (STATE_SOUTH_SEA_LANE_03). Die Provinz wurde ohne Kartenansicht gewählt. Falls der Weltmarkt-Zugang komisch wirkt, eine zentralere passierbare Meeresprovinz nehmen.
- Zusätzlich VA-012 erledigt. Nächster Test mit aufgeräumtem Repo-Stand.
### 2026-10-29 – zweiter Start: Kampagne lädt

- Kein Absturz mehr, der Fix für `WORLD_MARKET_LOCATION` wirkt.
- `error.log` ist in ~1 Minute 5× übergelaufen (je 512 KB, nur 6 Dateien werden behalten). Die Fehler vom Laden sind dadurch verloren.
- Der Spam kam zu 99 % aus Vanilla `common/scripted_triggers/00_gfx_buildings_graphics_triggers.txt` (Stadtgrafik-Trigger mit Erde-States, ~11.600 Fehler pro Minute). Fix: gleichnamige Datei mit neutralen Triggern (`always = no`), eingetragen als bewusster Override.
- Rest: `HOVER_LAND_PROVINCE_TOOLTIP_DEBUG` (nur Debug-Tooltip), `00_acw_entries.txt` (Vanilla-Kopie, VA-003), fehlende Wappen-Texturen (`ce_dragon`, `ce_nethergarde_tower`, `ce_block_*`, `ce_bend_lozenges`, `pattern_solid`).
- Nächster Test: Kampagne laden, sobald die Karte steht, Spiel beenden. Dann sind die Ladefehler vollständig im Log.
### 2026-10-29 – dritter Start

- Stadtgrafik-Spam ist weg (0 Treffer). Das Log läuft aber schon **beim Laden** über (~3 MB in 25 s). Die ersten ~20 s fehlen.
- Von den zuordenbaren Fehlern: ~7.700 aus eigenen Vanilla-Kopien, ~4.600 aus Vanilla-Dateien mit Erde-Bezügen.
- Größte Einzelquellen: `interest_groups/00_petty_bourgeoisie.txt` und `ideologies/01_character_ideologies.txt` (je ~2.080, `has_law_or_variant`: Gesetzesvarianten seit 1.12), `portrait_modifiers/01_clothes.txt` (516), Vanilla `geographic_regions/*` (~1.300), Vanilla `government_types/01_social_monarchies.txt` (368).
- Konsequenz: Erst VA-003 (Kopien abbauen), sonst bleibt das Log unlesbar.
### 2026-10-29 – vierter Start (22:57)

- Spiel läuft auf **1.13.11** (`code_revisions.log`: `release/1.13.11`). Eine 1.14 ist lokal nicht installiert.
- Log wieder übergelaufen, erhalten sind nur 22:58:00–22:58:17 (~15.800 Fehler).
- 10.305× Vanilla `common/ai_strategies/00_default_strategy.txt` (Block `strategic_region_scores` fragt `sr:region_arabia` usw. ab). Fix: `common/ai_strategies/va_default_strategy.txt` ersetzt nur diesen Block per `INJECT:ai_strategy_default`. Im nächsten Test prüfen, ob `INJECT` den Block ersetzt (Fehler weg) oder nur anhängt (Fehler bleiben → dann bewusster Override nötig).
- 5.496× Vanilla `gfx/portraits/portrait_modifiers/01_headgear.txt`/`01_clothes.txt`: `cu:griqua` fehlt, weil die Mod-Kopie `common/cultures/00_cultures.txt` eine alte Vanilla-Kulturliste ist (13 neue 1.13-Kulturen fehlen). Fix über VA-003 (Kulturen und Merkmale).
- Rest: 4× `00_acw_entries.txt`, fehlende Wappen-Texturen (wie zuvor), 18× `gfx/map/textures/ not found` (leerer Texturpfad, Quelle noch unklar).
### 2026-10-29 – fünfter Start (23:08)

- Kulturen-/Merkmal-Kopien gelöscht: `griqua`-Fehler weg. `INJECT:ai_strategy_default` wirkt (Fehler aus `strategic_region_scores` weg).
- Log läuft trotzdem in ~8 s über. Neu sichtbar: 15.952× `strategic_region_stance_type_scores` (Zeilen 4262/4285, gleicher Vanilla-Block-Typ) und 46× `01_admin_strategies.txt:51`. Beide jetzt ebenfalls per `INJECT` in `va_default_strategy.txt`.
- 490× `01_clothes.txt:13537` (`scope:pop` fehlt): Die Mod-Kopie `scripted_triggers/00_clothes_triggers.txt` ist alt, 53 Vanilla-Trigger fehlen (u. a. `spanish_clothes_pop_trigger`). → VA-003.
- 141× `Country X is not permitted to retain law …` (75 Länder) → VA-014.
- 318× `pdx_persistent_reader: Failed to read key reference … in file: ""` direkt nach den Gesetzen, Quelle unklar.
### 2026-10-29 – sechster Start (23:15)

- **Log läuft nicht mehr über.** 11.665 Einträge, alle beim Laden (23:15:04–23:15:51), danach nichts mehr. Kein Dauerfeuer mehr.
- Auswertung jetzt mit `python -I .claude/tools/va_errlog.py [--by-file] [--filter TEXT] [--top N]` (nimmt nur die Logs des letzten Starts).
- Aufteilung: ~8.400 aus Vanilla-Dateien mit Erde-Bezug (größte: `geographic_regions/*` ~1.300, `ai_strategies` ~630 PostValidate, `portrait_modifiers` ~620, Vanilla-`00_scripted_triggers.txt` 330, `government_types/01_social_monarchies` 195), ~3.300 Engine-Meldungen.
- Behoben: 586× `Missing expected culture/religion static modifier` → `common/static_modifiers/va_culture_modifiers.txt` (86 Kulturen × 6) und `va_religion_modifiers.txt` (35 Religionen × 2). Neue Kulturen/Religionen dort nachtragen.
- Offen, mit Ticket: Gebäude (279 fehlende Loc, VA-003), Start-Gesetze (141, VA-014).
- Offen, ohne Ticket bisher: 367× Festungs-Locator in Meeresprovinz (`fortification_graphics`), 318× `pdx_persistent_reader … file: ""`, 77× ungültige Hauptstädte von Erde-Tags aus `country_definitions/00_countries.txt`, ~185× State-Region-Hubs (Hub in fremder State Region/Seeregion, fehlende Hubs, z. B. `STATE_GILNEAS_CITY`, `STATE_LARGO_OVERLOOK`), 28× Strategic-Region-Hauptstadt außerhalb (Northrend), 70× Modifier-Typen aus Kopie „defined in script but not in code“, ~90× fehlende Loc `regaltest` in Kulturen.
### 2026-10-29 – siebter Start (23:24)

- Log wieder übergelaufen, Ursache selbst verschuldet: Die neuen Static Modifiers nutzen Modifier-Typen (`state_<kultur>_standard_of_living_add`, `country_<kultur>_cultural_acceptance_add`, `country_fervor_target_<kultur>_add`), die Vanilla eigens in `common/modifier_type_definitions/` anlegt. Fix: `common/modifier_type_definitions/va_culture_religion_modifier_types.txt` (293 Typen). Neue Kulturen/Religionen dort ebenfalls nachtragen.
- Karte geprüft (`map_data/provinces.png` gegen Vanilla): Mod 32.655 Provinzen, Median 180 px; Vanilla 40.875, Median 228 px. Provinzen <100 px: Mod 1.954, Vanilla 1.349. Die Provinzgröße liegt also im Vanilla-Rahmen, Neuzeichnen ist nicht nötig. Falls gewünscht: Winzlinge per Skript mit Nachbarn derselben State Region verschmelzen (Ticket bei Bedarf).
### 2026-10-29 – achter Start (23:29)

- Log läuft nicht über, 11.079 Einträge, nur beim Laden. Culture/Religion-Modifier und ihre Typen greifen (0 Fehler).
- Rest wie beim sechsten Start; dazu einzelne `Unknown modifier type` aus alten Kopien (`production_methods/11_private_infrastructure.txt`, `company_types/99_basic_companies.txt` mit alten Gebäudenamen → VA-003 Gebäude).

### 2026-10-30 – erstes vollständiges Log (Runde 3, nach VA-025/VA-002 Teil 1)

Das Log enthält jetzt die Ladefehler vom Start. Fehlergruppen nach Größe, mit Zuordnung:

- ~500× Vanilla `geographic_regions` und `power_bloc_names` mit Erde-Bezug → VA-026.
- 367× `fortification_graphics`: Festungs-Locator in Wasserprovinzen (Karten-Grafik, `gfx/map`). Noch kein Ticket; vermutlich alte Locator-Datei aus Vanilla.
- 216× `Invalid owner for scope type 0` und 216× `Value of wrong type` aus Vanilla `scripted_progress_bars` (JE-Fortschrittsbalken ohne JE) → mit VA-002 Teil 2 (journal_entries).
- 200× `… does not have a valid namespace`: On-Actions und Mod-JE-Kopien rufen abgeschaltete Erde-Events auf (erwartet, VA-002/VA-003).
- ~600× `PostValidate of trigger … returned false` (Vanilla `ai_strategies`, `laws`, `decrees`, `portrait_modifiers`, `royal_successions` …): Folgefehler fehlender Erde-Objekte; erst nach VA-002 Teil 2 neu zählen.
- 44× fehlendes UTF-8-BOM in Mod-Dateien (u. a. `VA_eastern_kingdom.txt`, alle `history/pops`, `history/states`) → VA-023.
- 13× `create_state … Province crossing multiple state regions` (Grim Batol, Booty Bay, Northrend, Outland, Pandaria) → VA-011.
- 24 Gebäude ohne Loc-Key (z. B. `building_eternium_mine`), 44 Ressourcen mit `_WIP`-Gebäudegruppen (`bg_fel_energy_crystals_WIP` …) → VA-006/VA-015-Umfeld.
- Herrscher führen ihre eigene Interessengruppe (Kirin Tor Expedition, Scarlet Crusade Whitemane) → VA-016.
- `history/characters/va_eastern_kingdom.txt:60` ungültige Kultur, `history/pops/va_outlands.txt:1618` Kultur `zombie` fehlt.
- 29× Archerus `building_company_basic_fishing` → VA-024.

