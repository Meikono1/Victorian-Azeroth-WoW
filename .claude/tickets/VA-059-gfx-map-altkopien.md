# VA-059: Alte Vanilla-Kopien unter `gfx/map` aufräumen

- **Status:** offen
- **Typ:** technik
- **Priorität:** mittel
- **Erstellt:** 2026-11-03

## Beschreibung

Alte Vollkopien unter `gfx/map` überdecken neue Vanilla-Stände. In VA-058 fehlten deshalb die Formations-Marker (`map_modes`) und Fehler kamen aus `fleet_dioramas`. Diese Ordner sind gelöscht: `army_dioramas`, `front_entities`, `fleet_dioramas`, `fleet_entities`, `map_modes`.

Abgleich aller Text-Dateien unter `gfx/map` (2026-11-03): 65 gleich wie Vanilla (überflüssig), 94 abweichend, 28 nur im Mod.
- Vermutlich alte Kopien ohne Mod-Inhalt: `city_data/city_types` (28 Dateien, 07/2025), `building_config/default.txt`, `city_data/city_vfx/01_fireworks.txt`.
- Kartenspezifisch, behalten: `map_object_data/generated`, `terrain`, `water`, `environment` (einzeln prüfen).
- Identische Kopien: können weg, schaden aber nicht sofort (bei Patches jedoch schon).

Vorgehen: je Ordner diffen (Mod-Inhalt?), Liste an Kono, nach Freigabe löschen (Repo und `mod\warcraft`), Spieltest (Städte, Gebäude-Optik, Karte). Binärdateien (`.bin`, `.dds`) nur auf ausdrücklichen Wunsch.

## Notizen
- 2026-11-03, Claude: aus VA-058 abgespalten.
- 2026-11-06 (VA-063): `spline_network/military_route_graphics/` gelöscht (Vanilla 1.15: `route_graphics`). Übrig in `spline_network`: `roadpaved_*.dds`, `roadpavedsandstone_diffuse.dds` (von Vanilla nicht mehr benutzt, dort `road_paved_*`), mit Vanilla identische `naval_route_*.dds`, `road_*.dds`, `game_road_data.txt`. Eigen und behalten: `spline_network.splnet`. Binärdateien nur mit Konos Freigabe löschen.
