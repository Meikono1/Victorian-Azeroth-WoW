# VA-029: Ressourcen und Start-Gebäude außerhalb Nord-EK setzen (Hungersnot)

- **Status:** in Arbeit
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Spieltest 2026-10-30: Die ganze Welt verhungert, weil 612 von 702 besiedelten States keine Start-Gebäude hatten (fehlender Content außerhalb Nord-EK, kein Fehler). Ohne Farmen keine Nahrung am Markt, ohne Arbeitsplätze Arbeitslose und Sterblichkeit. Vollständiger Verlauf mit Analyse und Zahlen je Region: [verlauf/VA-029-start-gebaeude-hungersnot.md](verlauf/VA-029-start-gebaeude-hungersnot.md).

## Vorgehen (Kono, 2026-10-30)

- **Region für Region**, eher grob: Claude schlägt vor, Kono nickt je Region ab. Nur Gebäude, Ressourcen-Vorkommen in `map_data/state_regions` nur auf Ansage.
- Maßstab **Vanilla-Frankreich 1836** je Mio. Pops (Getreide 2,75, Ranch 0,75, Fisch 0,46, Holz 0,93, Kohle 0,38, Eisen 0,17 …), gerechnet auf Regionsebene. Lore verschiebt die Gewichte über **Länderprofile** in `.claude/tools/va_profiles.py` („Jedes Reich hat eine Persönlichkeit“); Nahrung mindestens 0,8 (`FOOD_MIN`).
- Werkzeuge: `va_region_overview.py NN --md` (Übersicht nach `.claude/regionen/`), `va_fill_buildings.py NN` (Probelauf, `--apply` schreibt, `--trim <gebäude>` kürzt), `va_add_ports.py`, `va_check_states.py NN`. Minen/Häfen nur mit passender Tech (`without_tech`).

## Stand je Region

| Region | Stand |
|---|---|
| 26 Nord-EK | fertig (+85, Eisen/Holz/Fisch gekürzt), Tests T-024, T-025 offen |
| 27 Mittel-EK | fertig (+388, Zwerge Minen ×1,5), Test T-026 offen |
| 28 Süd-EK | fertig mit Länderprofilen (+319), Test T-028 offen |
| 21–28 Häfen, Ackerland | 106 Start-Häfen, Ackerland für 5 Nord-EK-States, Test T-029 offen; Fischerei-Platzhalter im Binnenland entfernt, T-027 offen |
| 24 Zentral-Kalimdor | Probelauf +319 mit Profilen liegt bereit, **wartet auf Neuzeichnen VA-038** (alle States haben Platzhalter-Pops 1 Mio.) |
| 23, 25 Kalimdor | offen, nach VA-038 |
| 29 Outland | offen; dabei `size = zombie` (VA-055), doppelte Ressourcen, auskommentierte `bg_*_WIP` |
| 21/22 Northrend, 30/31 Pandaria, 32–35 | offen, zuletzt (wenig Pops) |

## Offen

- Verwaltung (Nord-EK nur 27 Stufen für 83 Mio. Pops) und Industrie in den fertigen Regionen; Weinberge (Stormwind u. a.) nachtragen, seit VA-003 heißt das Gebäude `building_vineyard`.
- Später (Kono): Dunkeleisenzwerge über Fleisch/Werkzeuge statt Ackerbau; Länderprofile verfeinern, sobald Content für ein Reich entsteht. Vashj'ir → VA-030.

## Notizen

- 2026-11-14 (VA-074): Ticket auf Stand gekürzt, alter Verlauf unter `verlauf/`.
