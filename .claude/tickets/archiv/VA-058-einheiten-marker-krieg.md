# VA-058: Einheiten-Icons im Krieg fehlen (prüfen)

- **Status:** erledigt
- **Typ:** bug
- **Priorität:** mittel
- **Erstellt:** 2026-11-03

## Beschreibung

Spieltest Kono 2026-11-03: Im Krieg (Thorium Brotherhood gegen Dark Iron, Searing Gorge) fehlen die Soldaten-Icons, die Vanilla zeigt (Vergleich Brasilien: rote/grüne Schilde mit Helm und Bataillonszahl über dem Schlacht-Marker). Im Mod-Screenshot nur ein grüner Marker „93“ an der Front.

Befund Claude (nur gelesen):
- Die Schilde mit Helm und Zahl sind in Vanilla `gui/map_markers.gui` → `battle_marker` (Angreifer/Verteidiger, Farbe `GetMilitaryInterfaceColor`). Sie erscheinen nur bei einer **laufenden Schlacht** und in naher Zoomstufe (`IsZoomLevelNear`).
- Im Mod-Screenshot läuft keine Schlacht, nur Front bzw. Armee im Anmarsch. Das Fehlen dort ist also evtl. normal.
- Der Mod überschreibt weder `gui/map_markers.gui` noch Einheiten (`common/combat_unit_types`, `gfx/models/units` fehlen im Mod). Alle Mod-Kulturen nutzen `graphics = european`, also Vanilla-Soldatenmodelle.
- error.log vom 2026-11-03 20:28: keine Zeile zu Einheiten oder Markern.

## Notizen
- Kono prüft: Fehlen die Schilde auch während einer laufenden Schlacht (nah heranzoomen, Kartenmodus Militär)? Fehlen die 3D-Soldaten an der Front? Screenshot mit laufender Schlacht hilft.
- 2026-11-03, Kono: Bestätigt, auch in einer laufenden Schlacht fehlen die Symbole (Screenshot Silvermoon gegen Wretched: Schlacht-Marker 20 gegen 6 da, Soldaten fehlen).
- 2026-11-03, Claude: Wahrscheinliche Ursache sind **alte Vollkopien von Vanilla-Grafikdateien** im Mod, die die aktuellen Dateien von 1.13 überdecken: `gfx/map/army_dioramas/` (2 Dateien, Stand 07/2025, Vanilla seitdem fast doppelt so groß), `gfx/map/front_entities/` (9 Dateien, Stand 2024, z. B. Infanterie kennt nur `has_culture_graphics = european` in alter Form) und `gfx/map/fleet_dioramas/` (`naval_battle_dioramas.txt` gibt es in Vanilla nicht mehr; Ursache der bekannten `fleet_dioramas`-Logzeilen). Ein Diff zeigt keine Mod-eigenen Inhalte, nur alte Vanilla-Stände.
- Lösung: die drei Ordner aus Repo **und** `mod\warcraft` löschen, damit Vanilla greift. Das Löschen hat die Rechteprüfung von Claude blockiert → Kono löscht oder gibt frei. Danach Test T-070.
- Folgeprüfung: weitere alte Vollkopien unter `gfx/map/` (z. B. `environment`, `map_modes`, `borders`) gegen Vanilla vergleichen; nur behalten, was Mod-Inhalt hat (Karte, Wasser, Masken).
- 2026-11-03, Claude: Mit Konos Freigabe `gfx/map/army_dioramas`, `front_entities`, `fleet_dioramas` im Repo gelöscht (in `mod\warcraft` löscht Kono). Weiterer Fund: `gfx/map/fleet_entities/01_fleet_entities.txt` ist ebenfalls alte Vanilla-Kopie (2024, 2,7 KB gegen 106 KB in 1.13, kein Mod-Inhalt) und deckt die Schiffsmodelle ab; mit Konos Freigabe ebenfalls gelöscht (auch in `mod\warcraft` löschen).
- 2026-11-03, Kono: `mod\warcraft` neu befüllt, Formations-Flaggen fehlen weiter. Claude: `fleet_dioramas`-Fehler sind aus dem error.log verschwunden. Ursache der fehlenden Flaggen: `gfx/map/map_modes/map_modes.txt` ist eine alte Vanilla-Kopie (07/2025) und nennt den Marker `military_formation_marker`; seit 1.13 heißen die Marker `land_formation_marker` und `fleet_formation_marker`. Kein Kartenmodus zeigt deshalb die Formations-Marker mit Flagge. Kein Mod-Inhalt in der Datei. Lösung: Datei löschen; mit Konos Freigabe gelöscht 2026-11-03 (auch in `mod\warcraft` löschen).
- Abgleich aller Text-Dateien unter `gfx/map` (2026-11-03): 65 gleich wie Vanilla (überflüssig), 94 abweichend, 28 nur im Mod. Abweichend und vermutlich alte Kopien: `city_data/city_types` (28), `building_config/default.txt`, `city_data/city_vfx/01_fireworks.txt`. Kartenspezifisch (behalten): `map_object_data/generated`, `terrain`, `water`, `environment`. Aufräumen als eigener Schritt.
- 2026-11-03: T-070 OK. Erledigt. Aufräumen der übrigen `gfx/map`-Kopien → VA-059.
