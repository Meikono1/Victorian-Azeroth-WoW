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

### 2026-10-30 – Spieltest Kono (Food Security) und Pop-Analyse

Kono fragt, ob die Pops stimmen. Maßstab Vanilla 1.13: Frankreich ~20.000 Pops je Stufe Ackerland, Paris 47.000, London 70.000 (Städte leben von Industrie und Importen). Median Vanilla 14.500.
Nord-EK gesamt 16.800, also **insgesamt nicht zu karg**. Das Problem sind einzelne States mit wenig Acker und vielen Pops:

| State | Pops | Acker | Pops je Acker | Vorschlag |
|---|---|---|---|---|
| Archerus (Ebon Blade) | 2,55 Mio. | 15 | 170.000 | **Keine starke Kürzung** (Kono: Lichkönig und seine Streitkräfte sitzen zu Beginn dort). Nahrung über Eroberung → VA-035 |
| Undercity | 3,5 Mio. | 35 | 100.000 | Pops auf ~2,0 Mio. (Hauptstadt, Industrie vorhanden) |
| Scholomance | 1,58 Mio. | 18 | 88.000 | Pops auf ~0,6 Mio. (Insel, Schule) |
| Shadowfang Keep | 1,7 Mio. | 35 | 48.600 | Pops auf ~1,0 Mio. |
| Deathknell | 1,7 Mio. | 37 → 65 | 26.000 | Acker erhöht (umgesetzt) |
| Zul'Aman | 3,05 Mio. | 70 → 110 | 27.800 | Acker erhöht (umgesetzt) |
| Aerie Peak | 1,47 Mio. | 35 → 55 | 26.700 | Acker erhöht, Ranch 3 und Mais +2 (umgesetzt) |
| The Bulwark | 1,55 Mio. | 38 → 60 | 25.800 | Acker erhöht (umgesetzt) |
| Crown Guard Tower | 1,47 Mio. | 62 → 75 | 19.600 | Acker erhöht (umgesetzt) |

- Pop-Kürzungen sind nur Vorschlag, **Entscheidung Kono**.
- Mittel-EK zum Vergleich: Gnomeregan 3,2 Mio. auf 8 Acker (400.000), Ironforge 3,6 Mio. auf 14 (257.000), Grim Batol 3,4 Mio. auf 23 (148.000), The Cauldron 0,84 Mio. auf 7 (120.000). Ohne Markt-Anbindung (VA-036) bzw. weniger Pops verhungern diese Städte.
- Nightmare Vale: Die 8 Stufen Bausektor stehen nicht in der History, sie sind im Spiel entstanden (KI baut). Farmen dort bewusst knapp lassen (Kono).
- „No historical data“ (Screenshot Kono, Bevölkerungs-Tooltip): Die Verlaufsgrafiken füllen sich erst mit laufender Spielzeit; direkt nach dem Start sind sie überall leer. Bleibt es nach einigen Monaten leer, erneut melden.
- Im selben Screenshot (Blood-Elf-Land, 5,15 Mio.): nur 235 Tsd. Beschäftigte, 3,86 Mio. Abhängige, Lebensstandard 8,8 – es fehlen Arbeitsplätze, nicht nur Nahrung.
- **Pops gekürzt 2026-10-30** (Kono: „Ja, kürzen“), `common/history/pops/va_north_eastern_kingdoms.txt`: Undercity 3,5 → 2,0 Mio., Scholomance 1,58 → 0,6 Mio., Shadowfang Keep 1,7 → 1,0 Mio. Je State nur ein `create_pop`, Kultur/Religion unverändert. Nord-EK jetzt 80,2 Mio. Pops. Gebäude unverändert (Auffüllen meldet 0). Lint 0 neue Fehler. Test: T-030.
- Archerus bleibt (VA-035). Mittel-EK-Städte (Ironforge, Gnomeregan, Grim Batol) noch offen, hängen an VA-036.
