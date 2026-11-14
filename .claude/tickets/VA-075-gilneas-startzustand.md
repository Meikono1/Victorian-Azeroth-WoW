# VA-075: Gilneas – Startzustand (Mauer, Gesetze, Crowley im Kerker)

- **Status:** offen
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-11-14

## Beschreibung

Teil des Sammeltickets VA-007 (Gilneas). Ablauf und Entscheidungen: [../ablauf/gilneas.md](../ablauf/gilneas.md). Abschnitte „Ausgangslage im Mod“ und „Startzustand“.

- Eigenes Gesetz `va_law_greymane_wall` (`parent = law_isolationism`, Vorbild Vanilla `law_sakoku`), bis zum Mauerfall gesperrt; Migration `law_closed_borders`; übrige Startgesetze nach Vorbild Japan (`jap - japan.txt`) prüfen.
- Passiver Zustand „Hinter dem Greymane-Wall“ (Abwehr +, kein Handel), Vorbild `je_sakoku` (`07_sakoku.txt`).
- Crowley im Kerker (Stoneward Prison), Groll von `ig_rural_folk`, Variable für die versteckten Northgate-Kanonen.
- Alter Platzhalter `je_infected_gilnean` und seine Loc raus (wird durch `je_gilneas_curse`, VA-076, ersetzt).
- Charakter-Vorlagen Genn, Liam, Crowley, Godfrey, Krennan (Belysra mit VA-078).

## Offen

- Nächster Schritt: Vanilla `law_sakoku` und `je_sakoku` lesen, Gesetz und Modifier anlegen, History von `GILNEAS` anpassen.
- Mauerfall selbst (Gesetz entsperren) kommt mit VA-082.

## Notizen

- 2026-11-14: Aus dem Gilneas-Ablauf (Version 4, mit Kono abgestimmt) geschnitten (VA-074).
