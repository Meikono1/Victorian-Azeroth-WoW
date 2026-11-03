# VA-026: Vanilla geographic_regions und power_bloc_names mit Erde-Bezug

- **Status:** wartet (Spieltest)
- **Typ:** bug
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Größte verbliebene Fehlergruppen im vollständigen Log aus Runde 3 (T-017). Kein Spam mehr, aber viel Rauschen, das echte Fehler verdeckt.

- **`common/geographic_regions/*.txt` (Vanilla), rund 500×:** `geographic_region_krakatoa_tsunami_zone`, `_tropical_seas`, `_greater_germany`, `_ring_of_fire`, `_han_homelands`, `_french_natural_borders`, `*_old` (06_old_strategic_regions) … listen Erde-State-Regionen auf. Lösung prüfen: gleichnamige leere Dateien (wie in VA-002), vorher klären, welche Vanilla-Scripts diese Regionen benutzen (sonst Folgefehler „unbekannte geographic_region“). Ggf. eigene Azeroth-Regionen gleichen Namens mit `REPLACE:` statt leerer Datei.
- **`common/power_bloc_names/00_power_bloc_names.txt` (Vanilla), ~19× je Zeile, viele Zeilen:** `Invalid right side during comparison` – die Namensregeln fragen Erde-Regionen/-Länder ab. Lösung prüfen: Datei leer überschreiben und eigene Azeroth-Namen in `va_power_bloc_names.txt` (Vorbild: Vanilla-Datei), oder Erde-Einträge per `REPLACE:` entschärfen.

## Notizen
- 2026-11-03: `geographic_regions` erledigt: 175 Vanilla-Regionen leer mit gleichem `short_key` (`va_gen_geo_regions.py`). Alte Kopie `power_bloc_names/00_power_bloc_names.txt` gelöscht; Vanillas Datei lädt jetzt, ihre Erde-Abfragen bleiben bis eigene Azeroth-Namen kommen. Test T-081, Details VA-043.
