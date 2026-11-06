# VA-061: Dynamische Masken für übrige Kontinente

- **Status:** offen
- **Typ:** grafik
- **Priorität:** mittel
- **Erstellt:** 2026-11-04

## Beschreibung

Die Masken in `gfx/map/masks/` sind alte Vanilla-Kopien mit der Erdkarte (Stand 04.11.: Farmland 98 %, Forstwirtschaft 85 %, Bergbau 79 % deckungsgleich mit Vanilla). Folge: Holzfäller-/Bergbau-Optik und Farmland erscheinen an Erde-Stellen statt passend zu Azeroth.

- Farmland: EK neu gemalt (VA-051, `va_dynamic_masks.py 26 27 28`). Übrige Regionen offen: erst `va_terrain.py`, dann `va_dynamic_masks.py` je Kontinent.
- `mask_dynamic_forestry.png`: aus Wald-/Dschungel-Terrain bzw. `wood`-Hubs ableiten (Werkzeug um Maske erweitern).
- `mask_dynamic_mining.png`: um `mine`-Hubs bzw. States mit Bergbau-Ressourcen.
- Prüfen: `gfx/map/dynamic_masks/exclusion_mask.dds` (Vanilla-Kopie, 19 MB) blendet evtl. dynamische Optik an Erde-Stellen aus (VA-059).

## Notizen
- 2026-11-04: Alle drei Masken geleert (keine Erde-Reste), EK für Farmland, Forst, Bergbau gemalt (`va_dynamic_masks.py 26 27 28 --clear`). Rest: je Kontinent erst `va_terrain.py NN …`, dann `va_dynamic_masks.py NN …` (ohne `--clear`!). `exclusion_mask.dds` weiter prüfen.

- 2026-11-06 (in VA-062 gefunden): Forst/Bergbau in EK waren fast leer, weil `load_states` nur `bg_…`-Schlüssel in `capped_resources` las (EK und Kalimdor 23/24 nutzen `building_…`). Behoben, 26–28 für mining und forestry neu gemalt. Bei Kalimdor (23, 24) gleich mit dem neuen Parser malen.
