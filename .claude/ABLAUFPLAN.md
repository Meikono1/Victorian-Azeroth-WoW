# Ablaufplan Victorian Azeroth

Stand: 2026-10-29. Spiel: **1.13.11**, Mod deklariert: **1.11.\***. Letzter Commit: 2025-12-02.

Hier stehen Fahrplan, offene Entscheidungen und Grundsätzliches. Konkrete Aufgaben stehen als Tickets in [`tickets/`](tickets/README.md).

## Offene Entscheidungen

_(keine)_

## Fahrplan

1. **Grundgerüst** – erledigt: `CLAUDE.md`, Ablaufplan, Ticketsystem, Kartenkorrektur aus Jan./Feb. 2026 ins Repo geholt, erstes Aufräumen.
2. **Spielbar auf 1.13** – VA-001, VA-002, VA-003, VA-004, VA-005
3. **Fehlende Texte** – VA-006, VA-007
4. **Content-Werkstatt** – VA-009, danach Content-Tickets (VA-008 …)
5. **Komfort** – VA-010

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
- Silvermoon: Wretched / Mana-Entzug (Gerüst, VA-008)

## Bewusste Vanilla-Overrides

_(Nur hier gelistete Vollkopien werden bei Patches nachgezogen. Format: Datei – Grund.)_
- `common/scripted_triggers/00_gfx_buildings_graphics_triggers.txt` – die 6 Stadtgrafik-Trigger aus Vanilla zeigen auf Erde-States. Ersetzt durch `always = no`. Bei Patches prüfen, ob Vanilla neue Trigger hinzufügt (sonst fehlen sie).
- `common/strait_definitions/strait_definitions.txt` – leer, Vanilla-Kanäle zeigen auf Erde-Provinzen.
- `common/defines/va_OVERWRITE_defines.txt` → `NEconomy.WORLD_MARKET_LOCATION` – Vanilla zeigt auf den Nordatlantik (Absturz). Bei Patches prüfen, ob neue Defines mit Provinz-IDs dazukommen.
