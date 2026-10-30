# VA-015: Nord-EK – Karte, Besitz, Ressourcen bereinigen

- **Status:** wartet (Spieltest)
- **Typ:** bug
- **Priorität:** hoch
- **Erstellt:** 2026-10-29

## Beschreibung

Nördliches Eastern Kingdoms (`map_data/state_regions/26_va_north_eastern_kingdoms.txt`, 79 States, 42 Länder) mechanisch fehlerfrei machen: State Regions, Hubs, Häfen, Besitz, Pops, Gebäude, Ressourcen, Hauptstädte.

Prüfung: `python -I .claude/tools/va_check_states.py 26` (geht auch für andere Regionen, z. B. `27`, `28`). Mit `--assign-test` schlägt das Skript für `STATE_TEST`-Provinzen den angrenzenden State vor.

## Notizen

### 2026-10-29 – erledigt

- **Ressourcen ins 1.13-Format:** `arable_resources`, `capped_resources`, `resource.type` von Gebäudegruppen (`bg_iron_mining`) auf Gebäudenamen (`building_iron_mine`) umgestellt, wie Vanilla 1.13. Zuordnung über `building_group` des aktuell geladenen Gebäudebestands. Achtung bei VA-003 (Gebäude): `building_vineyard_plantation` → Vanilla `building_vineyard`, `building_gold_fields` → `building_gold_field`. `_WIP`-Ressourcen nicht angefasst (gibt es in Nord-EK keine).
- **Quel'Danas:** `impassable` von `STATE_SUNS_REACH` gehörte zu Provinzen von `STATE_MAGISTERS_TERRACE` → dorthin verschoben.
- **Seradane/Scholomance:** 38 Provinzen, die die History `EMERALD_ENTRANCE_SERADANE` gibt, lagen in der State Region `STATE_SCHOLOMANCE` (dadurch Seradane-Hubs „fremd“, Scholomance fälschlich Küste). In `STATE_SERADANE` verschoben.
- **Hubs neu gesetzt** (per `provinces.png`, nur wo ungültig): Gilneas City (city, farm – Provinzen gab es nicht mehr), The Headlands (farm lag in Koroth Den, wood gab es nicht), Scholomance (city/mine/wood nach dem Verschieben). Northgate Woods: Port + `naval_exit_id 8063`. Tyr's Hand: `naval_exit_id 8057`. Christian: im Spiel prüfen, ob die Stadtmarker sinnvoll sitzen.
- **History:** West Sanctum – 8 Provinzen waren doppelt (Silvermoon und Grimscale), Silvermoon abgegeben. Homeland `cu:whiterbark_troll` (gibt es nicht) → `cu:forest_troll`. Pop-Kultur `wretched_bloodelf` (gibt es nicht) in Silvermoon City → `sin_dorei` (eigene Wretched-Kultur ggf. mit VA-008).
- **Hauptstädte** (`VA_eastern_kingdom.txt`): Wildhammer `STATE_BAMBALA` → `STATE_AERIE_PEAK`, Wretched `STATE_WITHERBARK_VILLAGE` → `STATE_RUINS_OF_SILVERMOON`, Frostwolf Highlands `STATE_HEADLAND` → `STATE_TARRENS_MILL`, Shadowpine `STATE_ULDAMAN` → `STATE_DAWNSTAR_SPIRE`.
- **Länder-History:** `TRANQUILLIEN` fehlte, nach Vorbild `SILVERMOON` angelegt.

### Offen

- 2026-10-30 erledigt: Quel'Danas (3 States inkl. Pops/Gebäude-Blöcke) gehört jetzt `SILVERMOON` statt Platzhalter `EASTERNKINGDOMS`. Der Tag selbst steckt in der Vanilla-Kopie `country_definitions/00_countries.txt` und hat keine States mehr.
- Ohne Start-Gebäude: `STATE_SUNS_REACH`, `STATE_MAGISTERS_TERRACE`, `STATE_SUNWELL_PLATEAU`, `STATE_STRATHOLME`, `STATE_AERIE_PEAK`.
- `STATE_STORMGARDE_KEEP`: 18 Provinzen gehören `STEAMWHEEDLE_CARTEL`, Homeland `goblin` – Lore prüfen.
- Gleiche Platzhalter-Hauptstädte gibt es auch bei Ländern außerhalb Nord-EK (`STATE_BAMBALA` 3×, `STATE_WITHERBARK_VILLAGE` 2×, `STATE_HEADLAND`, `STATE_ULDAMAN`) → mit `va_check_states.py 27`/`28` prüfen.
- Gebäude-History nutzt noch den alten Gebäudebestand (VA-003). Die PM-Prüfung im Skript läuft gegen den aktuell geladenen Stand und meldet für Nord-EK nichts.
- 2026-10-30: Testfälle im [Testprotokoll](../TESTPROTOKOLL.md), Runde 1: T-001 bis T-010.
