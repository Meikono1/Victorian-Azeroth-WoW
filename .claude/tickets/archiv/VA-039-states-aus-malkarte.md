# VA-039: Werkzeug – States aus einer gemalten State-Karte erzeugen

- **Status:** verworfen
- **Typ:** technik
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Der Ingame-Map-Editor ist zu langsam: rund eine Stunde für fünf States (VA-038). Außerdem schreibt er inkonsistente Daten, z. B. Provinzen in der State-History, die in keiner State Region stehen.

Idee: Kono malt in einem Bildprogramm eine **State-Karte** als Ebene über `provinces.png`, eine Farbe je State, und dazu eine kleine Tabelle Farbe → `STATE_…`. Ein Skript in `.claude/tools/` erzeugt daraus:

- `provinces = { … }` je State in `map_data/state_regions/NN_….txt`: jede Provinz geht an den State mit den meisten Pixeln
- `owned_provinces` in `common/history/states/VA_….txt` (bei mehreren Besitzern nach Teilfarbe oder aufteilen lassen)
- Vorschläge für `city`/`port`/`farm`/`mine`/`wood`-Hubs (Küste, Mittelpunkt) und `naval_exit_id`
- Gegenprüfung: Jede Landprovinz liegt in genau einem State, jede Farbe ist auf der Karte, keine verwaisten IDs

## Notizen

- Vorhandene Bausteine: `va_check_states.py` (Karte gegen History), Pillow/numpy.
- Vorher mit Kono klären: Provinzen selbst weiter im Editor/Bildprogramm, nur die State-Zuordnung per Skript?
- 2026-10-30 **verworfen** (Kono): Neu zeichnen ist Pflicht, ein generierter Stand passt nicht zu Heightmap und Texturen.
