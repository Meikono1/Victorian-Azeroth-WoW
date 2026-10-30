# VA-034: Startevent – Event-Übersicht und Zeitplan der Eventgruppen

- **Status:** offen
- **Typ:** content
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Beim Spielstart erscheint ein Event (Wunsch Kono), das

1. anzeigt, wie viele Events bzw. Eventgruppen der Mod enthält, und
2. die Möglichkeit gibt, bestimmte Eventgruppen an den Spielstart zu legen, statt auf ihren normalen Zeitpunkt zu warten.

Normaler Zeitplan der Eventgruppen (Jahre nach Spielbeginn):

| Eventgruppe | Standard |
|---|---|
| Deathwings Flug (Kataklysmus) | Spielstart, die Karte basiert auf Cataclysm |
| Outland | +25 Jahre |
| Northrend | +50 Jahre |
| Draenor – Portal öffnet sich | +60 Jahre |
| Lost Isles – Dämoneninvasion | +75 Jahre |

## Notizen

- Die Eventgruppen selbst gibt es noch nicht. Dieses Ticket baut zuerst den Rahmen (Startevent, Schalter, Zeitgeber), die einzelnen Gruppen kommen als eigene Tickets dazu.
- Technik-Idee (vor Umsetzung an Vanilla und Script-Doku prüfen):
  - Startevent über `on_game_started` (siehe `docs\on_actions.log`), nur für Spielerländer.
  - Je Gruppe eine globale Variable `va_eventgroup_<name>_start` (Startdatum) bzw. ein Flag; Optionen setzen sie auf „sofort“.
  - Auslöser der Gruppen prüfen das Datum bzw. das Flag (jährlicher Pulse oder `trigger_event` mit Verzögerung).
  - Die Event-Anzahl lässt sich nicht im Script zählen; als feste Zahlen in der Lokalisierung pflegen oder per Skript (`va_events.py`) vor jedem Upload in die Loc schreiben.
- Alternative prüfen: Vanilla `common/game_rules` (Regeln im Spielstart-Menü, `has_game_rule`). Damit wählt man vor Spielbeginn, ohne Event. Entscheidung Kono.
- Multiplayer: Wer darf entscheiden? Vorschlag: nur der Host bzw. das erste Spielerland.

- 2026-10-30 (Kono): Vor den globalen Eventgruppen bekommt jedes relevante Land 25–40 Jahre Journal Entries (Partie: 100 Jahre). Die Zeitpunkte der Eventgruppen oben sollten dazu passen, also die erste globale Gruppe frühestens ab etwa +25 Jahren. Ablaufdiagramme je Land unter `.claude/ablauf/` (Regel in `.claude/CLAUDE.md`, Content-Ablauf Punkt 5).
