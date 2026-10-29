# VA-001: Spielstart mit Mod und error.log auswerten

- **Status:** in Arbeit
- **Typ:** technik
- **Priorität:** hoch
- **Erstellt:** 2026-10-29

## Beschreibung

Christian startet Victoria 3 (1.13.11) mit dem Mod bis in eine Kampagne und führt in der Konsole `script_docs` aus. Claude wertet danach `logs\error.log` aus und legt pro Fehlerursache ein Ticket an.

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
