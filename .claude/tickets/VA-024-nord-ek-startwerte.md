# VA-024: Nord-EK – Pops, Start-Gebäude und Startwerte prüfen und anpassen

- **Status:** offen
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Nach VA-015 (Mechanik) die Startwerte im nördlichen Eastern Kingdoms (Region 26) inhaltlich durchgehen und an Lore und Spielbalance anpassen. Wunsch von Kono nach dem ersten Lauf über einige Monate (Runde 1, T-001): „sieht ganz okay aus“, jetzt Pops, Start-Gebäude und alles Übrige prüfen.

Umfang je State/Land:

- **Pops:** Größe, Kultur, Religion, Schichten (`pop_type`). Vergleich mit Vanilla-Größenordnungen.
- **Start-Gebäude:** Art, Stufen, Besitz, Produktionsmethoden; passen sie zu Ressourcen und Pops? Firmen-Gebäude (`building_company_*`) prüfen.
- **Übrige Startwerte:** Ressourcen/Arable Land, Gesetze (→ VA-014), Technologien, Institutionen, Diplomatie/Subjekte, Länder-Rang. Herrscher laufen in VA-016.

Dateien: `common/history/pops/va_north_eastern_kingdoms.txt`, `common/history/buildings/26_north_eastern_kingdoms.txt`, `map_data/state_regions/26_va_north_eastern_kingdoms.txt`, `common/history/countries/…`, `common/history/states/VA_eastern_kingdoms_states.txt`.

Vorschlag zum Vorgehen: erst eine Übersichtstabelle (State, Besitzer, Pops, Kulturen, Gebäude-Stufen) per Skript erzeugen, Kono markiert, was nicht passt, dann gezielt anpassen. Das Skript lässt sich danach für die anderen Regionen wiederverwenden.

## Notizen

### 2026-10-30 – Ausgangslage

- Pops Region 26: 78 States, zusammen **83,4 Mio.**. Zum Vergleich: Vanilla-Großmächte haben 1836 zweistellige Millionen. Vermutlich insgesamt zu hoch, Gesamtbudget für Azeroth festlegen.
- Größte States: Undercity 3,5 Mio., Zul'Aman 3,05 Mio., Gilneas City 2,76 Mio., **Archerus 2,55 Mio.** (Ebon Hold, Lore eher klein), New Avalon 2,34 Mio., Jintha'Alor 2,01 Mio.
- Kleinste: Sun's Reach, Magisters' Terrace, Sunwell Plateau je 10.000 (Platzhalter aus der Quel'Danas-Übernahme), Fenris Isle 280.000.
- Ohne Start-Gebäude: Sun's Reach, Magisters' Terrace, Sunwell Plateau, Stratholme, Aerie Peak.
- Archerus: Laufzeitfehler `Tried to create building of Type building_company_basic_fishing … in State 'Archerus', but such a building already exists` (mehrfach). Der Fischkai in der Gebäude-History hat Firmenbesitz `building_company_basic_fishing` – prüfen, ob die Firma dort zusätzlich ihr HQ bauen will; ggf. auf Länderbesitz umstellen.
- `STATE_STORMGARDE_KEEP`: 18 Provinzen gehören `STEAMWHEEDLE_CARTEL` (aus VA-015 offen).

## Offen

- **Kono:** Gesamtgröße der Bevölkerung für Azeroth / Nord-EK festlegen (Richtwert pro State).
