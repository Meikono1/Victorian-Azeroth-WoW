# VA-032: Zandalar, Kul Tiras, Verlorene Inseln, Draenor – Provinzen unterteilen und States anlegen

- **Status:** offen
- **Typ:** technik
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Kono wollte die Rogue-Provinzen (VA-031) nutzen, um Zandalar, Kul Tiras und die Verlorenen Inseln zu füllen. Diese Gebiete bestehen heute aus wenigen Riesenprovinzen und je einem State:

| Region | State-Datei | Provinzen | Pixel | Pixel je Provinz |
|---|---|---|---|---|
| Zandalar | `34_va_zandalar.txt` | 9 | 225.569 | ~25.000 |
| Kul Tiras | `35_va_kul_tiras.txt` | 15 | 196.867 | ~13.000 |
| Verlorene Inseln | `33_va_lost_isles.txt` | 10 | 268.203 | ~27.000 |
| Draenor | `32_va_dreanor.txt` | 11 | 593.880 | ~54.000 |

Normal sind ~180 Pixel je Provinz (Median der Karte). Bei ähnlicher Dichte bräuchte Zandalar allein über 1.000 Provinzen, mehr als der Haufen hergibt (649). Die Haufen-Provinzen selbst sind nur Farben; ihre Form im Haufen ist unbrauchbar.

## Vorschlag

- Riesenprovinzen per Skript in kleinere unterteilen (Voronoi/k-Means über die Landpixel jeder Riesenprovinz, Grenzen der Ausgangsprovinz bleiben). Farben: neue, eindeutige Farben; die Haufen-Farben nach VA-031 wiederzuverwenden ist möglich, bringt aber keinen Vorteil.
- Zielgröße mit Kono festlegen (z. B. 400–800 Pixel für dünn besiedelte Inseln, dann ~300–600 Provinzen für Zandalar).
- Danach States nach Lore schneiden (Kono gibt Grenzen grob vor, z. B. Zuldazar, Nazmir, Vol'dun für Zandalar; Tiragarde, Drustvar, Stormsong für Kul Tiras), Hubs setzen, `province_terrains.txt` ergänzen, History, Pops, Ressourcen, Gebäude (VA-029-Werkzeuge).
- Voraussetzung: VA-031 (Haufen weg), damit keine Provinz-IDs doppelt geplant werden.

**Freigabe nötig:** provinces.png wird geändert (Projektregel).

## Notizen
