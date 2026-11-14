# VA-007: Gilneas – Worgen-Reihe (Sammelticket)

- **Status:** offen
- **Typ:** content
- **Priorität:** mittel
- **Erstellt:** 2026-10-29

## Beschreibung

`gilnean_infection_events.*`, `je_infected_gilnean`, `je_cement_the_rightful_dynasty` haben keine Texte. `localization/replace/english/events/va_gilneas_events_l_english.yml` enthält nur den Vanilla-Key `assassination_events.1`.

## Teiltickets (2026-11-14)

Ablauf: `.claude/ablauf/gilneas.md`. Reihenfolge: VA-075 → VA-076 und VA-077 → VA-078 → VA-079 bis VA-081 → VA-082. Nebenstrang Sense der Elune (`ablauf/sense_der_elune.md`) und Bloodfang (VA-073) später.

| Ticket | Inhalt |
|---|---|
| VA-075 | Startzustand: Mauer-Gesetz, Gesetze, Crowley im Kerker, Platzhalter-JE raus |
| VA-076 | `je_gilneas_curse` und Paranoia |
| VA-077 | `je_gilneas_factions` (Greymane, Godfrey, Crowley) |
| VA-078 | Nachtelfen, Ritual von Tal'doren, Religion |
| VA-079 | Greymanes Biss und Liam |
| VA-080 | Crowley frei, Heilmittel, Crowleys Ultimatum |
| VA-081 | Godfreys Machtgriff, Aussprache, Verrat |
| VA-082 | Mauerfall und Forsaken-Krieg |

Dieses Ticket ist erledigt, wenn alle Teiltickets erledigt sind. Die ursprüngliche Aufgabe (Loc der alten Platzhalter) geht in VA-075 auf.

## Notizen
- 2026-10-29: `events/gilneas_events/infection_events.txt` (1.053 Zeilen) enthält neben `gilnean_infection_events.1` großteils kopierte `acw_events.*` (Amerikanischer Bürgerkrieg). Kono möchte eine Worgen-Reihe nach dem Muster der Frankreich-Inhalte; Vanilla-Vorbilder: `common/journal_entries/01_french_monarchism.txt`, `01_paris_commune.txt`, `events/french_pretenders(_pulse).txt`. Vor dem Schreiben klären, welche davon gemeint ist.
- 2026-10-30 (Log Runde 4): `common/journal_entries/VA_gilneas_infection.txt` hat kein BOM, `should_be_pinned_by_default` (Zeile 510) gibt es in 1.13 nicht mehr, `group = je_group_g` ist ungültig. Außerdem ruft die Datei `french_pretenders`-Events und `french_monarchy_*_button` auf, die abgeschaltet sind (VA-002).
- 2026-11-03: Kopierte `acw_events.1–9` aus `infection_events.txt` entfernt (Dubletten von Vanilla), `je_infected_gilnean` auf gültigen Platzhalter gekürzt, `je_cement_the_rightful_dynasty` und alle Frankreich-Aufrufe entfernt (VA-043). Für die Worgen-Reihe ist jetzt eine leere JE da.
- 2026-11-13: Ablauf-Entwurf `.claude/ablauf/gilneas.md` (Mauer, Northgate, Fluch, Invasion Undercity nach ca. 10 Jahren, Tal'doren, Exil). Wartet auf Besprechung mit Kono.
- 2026-11-14: Konzept mit Kono abgestimmt und um Video-Lore (Teil 1 und 2) ergänzt. Entschieden: Mauer als gesperrtes Gesetz `va_law_greymane_wall` (Vorbild `law_sakoku`), Mauerfall erzwingt Crowleys Ultimatum, Heilmittel „Protokoll oder Trank“, Biss-Optionen mit Liam-Pfad, „Godfrey zur Rede stellen“, Gesetz Worgen-Akzeptanz, Ausgang „Das wilde Rudel“ (Arugal). Zahlen und Schwellen werden beim Anlegen der JEs festgelegt. Nächster Schritt: Scripten (Startgesetze/History, dann `je_gilneas_factions`, `je_gilneas_curse`).
- 2026-11-14: Nebenstrang Sense der Elune als Entwurf in `.claude/ablauf/sense_der_elune.md` (von Kono, gegen das Wiki geprüft). Offen u. a.: State von Roland's Doom, aktive Parteien, Godfreys Erweckung ohne Val'kyr.
