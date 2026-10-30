# Ablaufplan Victorian Azeroth

Stand: 2026-10-29. Spiel: **1.13.11**, Mod deklariert: **1.13.\***. Letzter Commit: 2025-12-02.

Hier stehen Fahrplan, offene Entscheidungen und Grundsätzliches. Konkrete Aufgaben stehen als Tickets in [`tickets/`](tickets/README.md).

**Nächster Spieltest:** [Testprotokoll](TESTPROTOKOLL.md), Runde 3 ist durch. Als Nächstes die offenen Tests aus Runde 1 (T-003 bis T-012) zusammen mit Runde 4 (T-018).

## Offene Entscheidungen

- Welche Formables für Nord-EK, welche davon als Major Formation? (VA-017)
- Herrscher-Liste Nord-EK abnicken (VA-016)

## Fahrplan

1. **Grundgerüst** – erledigt: `CLAUDE.md`, Ablaufplan, Ticketsystem, Kartenkorrektur aus Jan./Feb. 2026 ins Repo geholt, erstes Aufräumen.
2. **Spielbar auf 1.13** – VA-001, VA-002, VA-003, VA-004, VA-005
3. **Priorität Nord-EK** – VA-015 (Mechanik), VA-016 (Herrscher), VA-017 (Formables), Start-Gebäude; Prüfung mit `.claude/tools/va_check_states.py 26`. Quel'Thalas-Content nach [`konzepte/quel_thalas.md`](konzepte/quel_thalas.md): VA-019 (Grundbausteine) → VA-020 (Silvermoon) → VA-021 (Wretched) → VA-022 (Amani, Deathholme)
4. **Fehlende Texte** – VA-006, VA-007
5. **Content-Werkstatt** – VA-009, danach Content-Tickets (VA-008 …)
6. **Komfort** – VA-010

## Erledigt

- 2026-10-30: `events`, `events/india_events`, `events/soi_events` aus `replace_paths` genommen (Entscheidung Christian). 122 Erde-Eventdateien per leerer Datei abgeschaltet. 119 alte Kopien gelöscht, 27 geleert (VA-002).

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
- `events/agitators_events/coup_events.txt` – alte Fassung, passt zur Mod-JE-Kopie `common/journal_entries/01_coup.txt`. Fällt weg, sobald `journal_entries` aus `replace_paths` kommt (VA-002, `KEEP_COPY` in `tools/va_events.py`).
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
- [ ] `va_lint.py --regions 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35` → 0 neue Fehler
- [ ] Testrunde mit Kampagnenstart und `error.log`-Auswertung

## Checkliste: Upload in den Workshop

- [ ] Letzte Testrunde im [Testprotokoll](TESTPROTOKOLL.md) komplett OK
- [ ] `va_lint.py` meldet 0 neue Fehler
- [ ] Alle Tickets dieser Version stehen auf `erledigt` oder bewusst offen (mit Notiz)
- [ ] `.metadata/metadata.json`: `version` hochgezählt, `supported_game_version` stimmt
- [ ] Mod-Ordner `mod\warcraft` vollständig aus dem Repo neu befüllt (ohne `.git`, `.claude`, `.gitignore`, `map_data/provinces.xcf`; gelöschte Repo-Dateien auch dort löschen) – VA-010
- [ ] Kurztest aus dem Mod-Ordner: Kampagne lädt
- [ ] Änderungen seit dem letzten Upload als Workshop-Text zusammengefasst
