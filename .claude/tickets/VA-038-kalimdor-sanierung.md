# VA-038: Kalimdor von Grund auf sanieren (Provinzen und States)

- **Status:** in Arbeit
- **Typ:** technik
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Kono 2026-10-30: Kalimdor (Regionen 23, 24, 25) muss von Grund auf saniert werden. Die Provinzen um Exodar stimmen schon, dort sind aber die States kaputt. Den Rest muss Kono komplett neu zeichnen.

Zeitproblem: Fünf States im Ingame-Map-Editor zu reparieren hat Kono rund eine Stunde gekostet. Für ganz Kalimdor (175 States) braucht es einen schnelleren Weg → VA-039.

## Notizen

### 2026-10-30 – Editor-Stand ins Repo geholt

Aus `mod\warcraft` übernommen (dort neuer als im Repo): `common/history/states/VA_kalimdor_states.txt`, `map_data/state_regions/23_va_north_kalimdor.txt`, `map_data/provinces.png`, `gfx/map/spline_network/spline_network.splnet`, `gfx/map/map_object_data/generated_map_object_locators_port.txt` und `…_wood.txt`. In `26_va_north_eastern_kingdoms.txt` ist nur `STATE_TEST provinces = {}` übernommen. Die Ackerland-Erhöhungen aus VA-029 bleiben, im Mod-Ordner fehlen sie noch.

**Inkonsistenz nach dem Editor-Lauf:**
- `STATE_TEST` hat in der State Region keine Provinzen mehr. Seine 312 Provinzen stehen jetzt in der History von `STATE_GNARLPINE_HOLD` (Besitzer `GNARLPINE_FURBOLG`, 340 `owned_provinces`), aber nicht in dessen State Region.
- Von den 340 Provinzen liegen nur 68 in irgendeiner State Region. Alle 340 Farben sind noch in `provinces.png`. Die übrigen 272 gehören also zu keinem State. Das ergibt beim Start vermutlich Fehler oder einen Absturz (siehe VA-031).
- Entscheidung Kono offen: (a) Splitter wie geplant löschen (VA-031), (b) vorläufig in `STATE_TEST` zurück und aus der Gnarlpine-History nehmen, (c) Gnarlpine wirklich zuweisen.
- `va_check_states.py 23` meldet außerdem: Farmen und Plantagen in Exodar, Azure Watch, Wildwind Peak und Stillpine Hold haben Holzfäller-PMs (`pm_hardwood`, `pm_saw_mills` …). Die Hauptstadt `STATE_RUUAN_WEALD` von `CENARION_CIRCLE` gehört nicht dem Land.
- Lint `--regions 23 26`: 0 neue Fehler. Den Provinzfehler findet der Lint nicht.

### 2026-10-30 – Entscheidung Kono

- Die Provinzen von `STATE_TEST` und Gnarlpine Hold hat Kono selbst erledigt. Die Splitter-States im Süden bleiben vorerst liegen und schaden nicht, solange niemand sie benutzt.
- Kono zeichnet Kalimdor selbst neu. Ein generierter Stand würde nicht zur Heightmap und zu den Texturen passen (VA-039 verworfen). Das läuft nebenbei, der Fokus liegt auf EK.
- Start-Gebäude für Kalimdor (VA-029, Regionen 23–25) erst nach dem Neuzeichnen. Der Probelauf für 24 und die Profile `_ZENTRAL_KALIMDOR` bleiben liegen.
