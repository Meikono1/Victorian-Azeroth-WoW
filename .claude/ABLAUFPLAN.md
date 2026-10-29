# Ablaufplan Victorian Azeroth

Stand: 2026-10-29. Spiel: **1.13.11**, Mod deklariert: **1.13.\***. Letzter Commit: 2025-12-02.

Hier stehen Fahrplan, offene Entscheidungen und Grundsätzliches. Konkrete Aufgaben stehen als Tickets in [`tickets/`](tickets/README.md).

## Offene Entscheidungen

- Quel'Danas (3 States) gehört dem Platzhalter-Land `EASTERNKINGDOMS` (Kvaldir, Hauptstadt Ironforge). Wem soll es gehören? (VA-015)
- Welche Formables für Nord-EK, welche davon als Major Formation? (VA-017)
- Herrscher-Liste Nord-EK abnicken (VA-016)
- Mana abstrakt (Variable + Fortschrittsbalken) oder als echtes Gut? Empfehlung: abstrakt (VA-019)
- Deathholme braucht ein Geißel-Land in Northrend, dort gibt es noch keine Länder (VA-022)

## Fahrplan

1. **Grundgerüst** – erledigt: `CLAUDE.md`, Ablaufplan, Ticketsystem, Kartenkorrektur aus Jan./Feb. 2026 ins Repo geholt, erstes Aufräumen.
2. **Spielbar auf 1.13** – VA-001, VA-002, VA-003, VA-004, VA-005
3. **Priorität Nord-EK** – VA-015 (Mechanik), VA-016 (Herrscher), VA-017 (Formables), Start-Gebäude; Prüfung mit `.claude/tools/va_check_states.py 26`. Quel'Thalas-Content nach [`konzepte/quel_thalas.md`](konzepte/quel_thalas.md): VA-019 (Grundbausteine) → VA-020 (Silvermoon) → VA-021 (Wretched) → VA-022 (Amani, Deathholme)
4. **Fehlende Texte** – VA-006, VA-007
5. **Content-Werkstatt** – VA-009, danach Content-Tickets (VA-008 …)
6. **Komfort** – VA-010

## Erledigt

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

## Bewusste Vanilla-Overrides

_(Nur hier gelistete Vollkopien werden bei Patches nachgezogen. Format: Datei – Grund.)_
- `common/scripted_triggers/00_gfx_buildings_graphics_triggers.txt` – die 6 Stadtgrafik-Trigger aus Vanilla zeigen auf Erde-States. Ersetzt durch `always = no`. Bei Patches prüfen, ob Vanilla neue Trigger hinzufügt (sonst fehlen sie).
- `common/strait_definitions/strait_definitions.txt` – leer, Vanilla-Kanäle zeigen auf Erde-Provinzen.
- `common/defines/va_OVERWRITE_defines.txt` → `NEconomy.WORLD_MARKET_LOCATION` – Vanilla zeigt auf den Nordatlantik (Absturz). Bei Patches prüfen, ob neue Defines mit Provinz-IDs dazukommen.
