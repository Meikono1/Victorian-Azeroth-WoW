# VA-030: Vashj'ir – Provinzen neu zeichnen und Ressourcen setzen

- **Status:** offen
- **Typ:** grafik
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Vashj'ir (Region 27, Besitzer `VASHJ_IR`, Naga) hat laut Kono dasselbe Provinzproblem wie andere Kartenteile und muss neu gezeichnet werden. Danach Ressourcen und Start-Gebäude passend zur Lore setzen (Unterwasser-Reich).

Stand 2026-10-30 (Analyse Claude):

| State | Provinzen | Pixel | Lage (x / y) |
|---|---|---|---|
| ABYSSAL_BREACH | 173 | 32.369 | 5131–5344 / 2365–2602 |
| SHIMMERING_GROTTO | 148 | 25.349 | 5320–5509 / 2373–2601 |
| L_GHOREK | 137 | 19.783 | 4946–5132 / 2541–2726 |
| NESPIRAH | 114 | 20.111 | 5332–5534 / 2564–2701 |
| KORTHUNS_END | 104 | 16.232 | 5074–5247 / 2586–2725 |
| VASHJ_IR | 95 | 16.859 | 5227–5353 / 2555–2759 |
| PROMONTORY_POINT | 74 | 10.901 | 5058–5173 / 2448–2579 |
| GNAWS_BONEYARD | 71 | 12.760 | 5464–5586 / 2402–2569 |
| BIELARAN_RIDGE | 70 | 13.197 | 5350–5523 / 2683–2791 |
| IMMORTAL_COIL | 67 | 9.111 | 5362–5518 / 2310–2415 |
| SMUGGLERS_SCAR | 56 | 7.916 | 5441–5565 / 2332–2439 |

- Alle 11 States haben identische Platzhalter-Ressourcen (`arable_land = 30`, Roggen, Ranch, Eisen 36, Blei 18, Holz 23, Fisch 11) und je 1 Mio. Pops.
- Seit VA-029 (Mittel-EK) stehen dort Platzhalter-Gebäude (je Roggen 3, Ranch 1, Fischerei 1, Holz 1), damit die Pops nicht hungern.

## Vorgehen

1. Kono zeichnet die Provinzen neu (Ingame-Map-Editor schreibt nach `mod\warcraft`, danach ins Repo zurückholen).
2. Claude prüft mit `va_check_states.py 27` (Hubs, Provinzen, Nachbarschaft).
3. Ressourcen nach Lore: Vorschlag Fisch/Walfang als Hauptnahrung, wenig Ackerland, keine Holzfäller; Kono entscheidet.
4. Gebäude neu: `va_fill_buildings.py 27`, vorher die Platzhalter-Gebäude in `common/history/buildings/27_center_eastern_kingdoms.txt` für Vashj'ir entfernen.

## Notizen
