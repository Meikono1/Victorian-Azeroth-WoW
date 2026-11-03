# VA-060: Festungs-Locators für Azeroth

- **Status:** wartet (Spieltest)
- **Typ:** grafik
- **Priorität:** niedrig
- **Erstellt:** 2026-11-03

## Beschreibung

Der Mod hatte keine eigene `gfx/map/map_object_data/fortification_locators.txt`. Das Spiel lud Vanillas 586 Festungs-Positionen der Erde-Karte; die im Azeroth-Meer liegen, melden je Start `fortification_graphics.cpp:373 … locator N is in a non-land province` (734 Zeilen am 03.11.). Im Map-Editor tauchen sie nicht auf, weil es keine Mod-Datei gibt.

## Notizen

- 2026-11-03: Eigene Datei mit 7 Test-Festungen um Silbermond (STATE_SILVERMOON_CITY, ab Stadt-Locator 2606 bei x 6497 / z 2647, Abstände 15–35, Drehung je 50°). Alle Punkte auf passierbaren Provinzen des States geprüft (`provinces.png`, Bildzeile = 3615 − z). Test T-082.
- Offen: Was die Festungen im Spiel zeigen (vermutlich Modelle an Fronten/Befestigungen), entscheidet die Sichtprüfung. Danach echte Positionen festlegen, z. B. eine je Stadt-Hub per Skript aus `generated_map_object_locators_city.txt`.
- 2026-11-03: Kono hat die Test-Festungen gesehen: schöne Grafiken, aber im Map-Editor weder verschieb- noch auffindbar. Datei jetzt leer (`instances = { }`), überschreibt Vanilla weiter. Wiederaufnahme nur per Skript (Positionen aus Stadt-Hubs), nicht im Editor. T-082 geändert: prüft nur noch, dass keine Festungen und keine Log-Zeilen kommen.
