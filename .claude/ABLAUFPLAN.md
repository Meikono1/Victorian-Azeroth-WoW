# Ablaufplan Victorian Azeroth

Stand: 2026-10-29. Spiel: **1.13.11**, Mod deklariert: **1.13.\***. Letzter Commit: 2025-12-02.

Hier stehen Fahrplan, offene Entscheidungen und Grundsätzliches. Konkrete Aufgaben stehen als Tickets in [`tickets/`](tickets/README.md).

**Nächster Spieltest:** [Testprotokoll](TESTPROTOKOLL.md), Runde 3 ist durch. Als Nächstes die offenen Tests aus Runde 1 (T-003 bis T-012) zusammen mit Runde 5 (T-021, T-022) und Runde 6 (T-024 bis T-026).

## Offene Entscheidungen

- Welche Formables für Nord-EK, welche davon als Major Formation? (VA-017)
- Herrscher-Liste Nord-EK abnicken (VA-016)
- Hungersnot (VA-029): Region für Region; Nord- und Mittel-EK erledigt, nächste Region Süd-EK (28); Vashj'ir-Ressourcen offen

## Fahrplan

1. **Grundgerüst** – erledigt: `CLAUDE.md`, Ablaufplan, Ticketsystem, Kartenkorrektur aus Jan./Feb. 2026 ins Repo geholt, erstes Aufräumen.
2. **Spielbar auf 1.13** – VA-001, VA-002, VA-003, VA-004, VA-005
3. **Priorität Nord-EK** – VA-015 (Mechanik), VA-016 (Herrscher), VA-017 (Formables), Start-Gebäude; Prüfung mit `.claude/tools/va_check_states.py 26`. Quel'Thalas-Content nach [`konzepte/quel_thalas.md`](konzepte/quel_thalas.md): VA-019 (Grundbausteine) → VA-020 (Silvermoon) → VA-021 (Wretched) → VA-022 (Amani, Deathholme)
4. **Fehlende Texte** – VA-006, VA-007
5. **Content-Werkstatt** – VA-009, danach Content-Tickets (VA-008 …)
6. **Komfort** – VA-010

## Erledigt

- 2026-10-30: Mittel-EK Start-Gebäude nach Maßstab Frankreich: +388 Stufen (VA-029).

- 2026-10-30: Nord-EK Start-Gebäude nach Maßstab Frankreich 1836: +85 Stufen; Eisen 27 → 14, Holz 99 → 77, Fischerei 45 → 27 gekürzt (VA-029). Werkzeuge `va_region_overview.py`, `va_fill_buildings.py`.

- 2026-10-30: `common/company_types` und `common/character_templates` aus `replace_paths` genommen (VA-002 Teil 3). 223 Erde-Dateien per leerer Datei abgeschaltet, Standardvorlage als `00_default_template.txt` auf 1.13 gebracht. Offen: alte `99_basic_companies.txt` zurückholen (siehe VA-002).

- 2026-10-30: `common/journal_entries` und `common/scripted_buttons` aus `replace_paths` genommen (Entscheidung Kono). 178 Erde-Dateien per leerer Datei abgeschaltet, 20 alte Kopien gelöscht, 7 allgemeine Eventdateien wieder aktiv (VA-002 Teil 2).
- 2026-10-30: `events`, `events/india_events`, `events/soi_events` aus `replace_paths` genommen (Entscheidung Kono). 122 Erde-Eventdateien per leerer Datei abgeschaltet. 119 alte Kopien gelöscht, 27 geleert (VA-002).

- 2026-10-29: 29 Kartendateien und Menü-Video aus dem Upload-Ordner ins Repo geholt (noch nicht committet).
- 2026-10-29: 134 Dateien gelöscht (noch nicht committet, Kategorien überschneiden sich teilweise):
  - 67 leere Platzhalter in `replace_paths`-Ordnern (wirkungslos, Vanilla-Ordner ist dort ohnehin ersetzt), darunter die leeren `character_templates/va_*_charakters.txt`
  - 29 Kopien identisch mit Vanilla 1.13 außerhalb von `replace_paths`
  - 25 alte Vanilla-Kopien, deren Original Vanilla inzwischen umbenannt hat und die dadurch doppelt luden: `laws/00_*` (15), `tech_events` (5), `scripted_effects/00_ip3_victoria_scripted_effects.txt`, `events/subject_interaction_evts.txt`, Decisions `canada_australia`, `ionian_islands`, `hawaii_decisions`
  - 6 leere Achievement-Dateien mit alten Namen, 6 `.info`-Doku-Kopien, `history/trade_routes` und `history/interests` (gibt es in Vanilla nicht mehr)
  - Liste aller gelöschten Dateien: `git status` bzw. `git diff --stat`
- 2026-10-29: 37 weitere alte Kopien gelöscht (noch nicht committet): `interest_groups`, `ideologies`, `laws`, `government_types` (ohne `01_monarchies`), `portrait_modifiers`, `ai_strategies` – siehe VA-003.

## Content-Ideen

_(Region, Länder, Kurzbeschreibung. Ausgereifte Ideen werden zu Tickets.)_

- Gilneas: Worgen-Fluch (begonnen, VA-007)
- Quel'Thalas: Silvermoon, Wretched, Amani, Deathholme – ausgearbeitet in `konzepte/quel_thalas.md`, Tickets VA-019 bis VA-022
- Quel'Danas: Kael'thas flieht dorthin und will Kil'jaeden beschwören → Shadowsword und eine kleine Gruppe der Shattered Sun entstehen (Eventreihe, später)
- Deathholme: Ausharren und Unterwerfung unter den Lichkönig, sobald Northrend ein Geißel-Land hat (zurückgestellt, VA-022)

## Bewusste Vanilla-Overrides

_(Nur hier gelistete Vollkopien werden bei Patches nachgezogen. Format: Datei – Grund.)_
- `common/scripted_triggers/00_gfx_buildings_graphics_triggers.txt` – die 6 Stadtgrafik-Trigger aus Vanilla zeigen auf Erde-States. Ersetzt durch `always = no`. Bei Patches prüfen, ob Vanilla neue Trigger hinzufügt (sonst fehlen sie).
- `common/strait_definitions/strait_definitions.txt` – leer, Vanilla-Kanäle zeigen auf Erde-Provinzen.
- `common/character_templates/00_default_template.txt` – Vanilla-Standardvorlage plus WoW-Lebensdauer und Staatsreligion (mit `VA:` markiert). Ein `INJECT` würde `trait_generation` komplett ersetzen, also keine Ersparnis. Bei Patches Vanilla-Teil neu übernehmen.
- `common/company_types/99_basic_companies.txt` – vorübergehend, falls Kono die alte Kopie zurückholt (VA-002 Teil 3): passt zu den alten Gebäudenamen. Mit VA-003 (buildings) löschen.
- `common/defines/va_OVERWRITE_defines.txt` → `NEconomy.WORLD_MARKET_LOCATION` – Vanilla zeigt auf den Nordatlantik (Absturz). Bei Patches prüfen, ob neue Defines mit Provinz-IDs dazukommen.

## Checkliste: neue Spielversion (Patch)

Jedes Mal komplett abhaken, Ergebnis als Notiz in einem eigenen Ticket „Patch 1.x“.

- [ ] Version prüfen: `launcher\launcher-settings.json` → `rawVersion`; `.metadata/metadata.json` → `supported_game_version` anpassen
- [ ] Spiel einmal starten, in der Konsole `script_docs` ausführen (aktualisiert `docs\*.log`)
- [ ] Jede Datei unter „Bewusste Vanilla-Overrides“ gegen die neue Vanilla-Datei vergleichen und Neuerungen übernehmen
- [ ] `common/defines/00_defines.txt` auf neue Werte mit Provinz-/State-IDs prüfen (Absturzgefahr wie `WORLD_MARKET_LOCATION`)
- [ ] Neue Vanilla-Ordner und -Dateien suchen, die Erde-States, -Tags oder -Kulturen referenzieren (`history`, `strait_definitions`, `geographic_regions`, `ai_strategies` …) → abschalten oder abfangen (VA-004)
- [ ] Neue Vanilla-Pflichtfelder/-Formate in Ordnern mit eigenen Objekten prüfen (State Regions, Gebäude, Güter, Kulturen, Länder), z. B. Ressourcen-Format 1.13
- [ ] `python -I .claude/tools/va_events.py --details`: neue Vanilla-Eventdateien mit Erde-Inhalt mit `--stubs` abschalten; bei „vanilla-allgemein“ und `GENERIC` von Hand gegenprüfen
- [ ] Dasselbe mit `python -I .claude/tools/va_common_folders.py common/journal_entries --details` und ebenso für `common/scripted_buttons`, `common/company_types`, `common/character_templates`; neue „vanilla-allgemein“-Dateien mit Erde-Thema in `EARTH` eintragen
- [ ] `va_lint.py --regions 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35` → 0 neue Fehler
- [ ] Testrunde mit Kampagnenstart und `error.log`-Auswertung

## Checkliste: Upload in den Workshop

- [ ] Letzte Testrunde im [Testprotokoll](TESTPROTOKOLL.md) komplett OK
- [ ] `va_lint.py` meldet 0 neue Fehler
- [ ] Alle Tickets dieser Version stehen auf `erledigt` oder bewusst offen (mit Notiz)
- [ ] TODO-Durchgang: alle `TODO` im Mod (ohne `.claude/`) durchsehen; jedes gehört zu einem Ticket. Grafik-TODOs in VA-027 nachtragen bzw. erledigte dort austragen, übrige erledigen oder dem passenden Ticket als Notiz zuordnen
- [ ] `.metadata/metadata.json`: `version` hochgezählt, `supported_game_version` stimmt
- [ ] Mod-Ordner `mod\warcraft` vollständig aus dem Repo neu befüllt (ohne `.git`, `.claude`, `.gitignore`, `map_data/provinces.xcf`; gelöschte Repo-Dateien auch dort löschen) – VA-010
- [ ] Kurztest aus dem Mod-Ordner: Kampagne lädt
- [ ] Änderungen seit dem letzten Upload als Workshop-Text zusammengefasst
