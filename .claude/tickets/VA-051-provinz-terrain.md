# VA-051: Provinz-Terrain zufällig (Berg, Feld)

- **Status:** wartet (Spieltest)
- **Typ:** bug
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Kono (2026-10-30): Provinzen haben zufällige Geländearten, manche Berg, manche Feld, passend zur Karte ist das nicht. Datei `map_data/province_terrains.txt`. Prüfen, wie das Terrain verteilt ist, ob es sich aus der Karte ableiten lässt (Heightmap, Geländetextur) und Region für Region korrigieren.

## Notizen

- 2026-11-03 Claude: Ursache: `province_terrains.txt` war Rauschen (alte, nicht zur Karte passende Zuordnung, z. B. 1.508 Tundra- und 311 Savannen-Provinzen in EK). Neues Werkzeug `.claude/tools/va_terrain.py` leitet das Terrain wie der Map-Editor aus den gemalten Texturen (`gfx/map/terrain/mask_*.png`, Gewichte nach Vanilla `common/terrain/01_terrain.txt`) plus Höhenrelief (`heightmap.png`) ab; `impassable` → Gebirge. Regeln im Docstring, Lore-Korrekturen je State über `STATE_OVERRIDES` (noch leer).
- 2026-11-03 EK (26–28) angewendet: 5.763 von 7.021 Provinzen geändert. Neu: plains 2.824, mountain 2.262, wetland 770, hills 490, snow 251, forest 226, savanna 102, desert 88. Vorschau `.claude/regionen/va_terrain_ek_vorschau.png`. Test T-083.
- **Farmland:** kein Grundterrain. Farmen wandeln Provinzen dynamisch um (Vanilla `common/terrain_manipulators`, `terrain_mask = "mask_dynamic_farmland"`, bevorzugt plains). ~~Farmland-Masken `mask_farmlands_0*.png` leer~~ (Irrtum 2026-11-03: das sind nur die Feldtexturen, auch in Vanilla leer).
- Offen: übrige Regionen (Kalimdor, Northrend, Outland, Pandaria …) mit demselben Werkzeug; Lore-Overrides mit Kono (Gilneas fast komplett plains, Westfall Savanne?).
- 2026-11-04 Kono: Hügel zu spärlich, Vashj'ir liegt unter Wasser → eigenes Terrain. Umgesetzt: Hügel-Schwelle Relief 650 → 400 (Feuchtgebiet bleibt bis 650), neues Terrain `va_underwater` (`common/terrain/va_terrain.txt`, Loc `va_terrain_l_english.yml`, State-Bild Platzhalter → VA-027) für die 11 States von `region_vashj_ir`, Schlingendorntal (10 States) Ebene/Wald/Savanne → Dschungel (dort ist keine Dschungel-Textur gemalt). EK jetzt: mountain 2.229, plains 1.198, va_underwater 1.109, hills 878, wetland 775, snow 250, forest 226, jungle 175, savanna 95, desert 82, tundra 4. Tests T-083, T-084.
- Nicht in EK vertreten: `lakes`, `ocean` (nur Wasserprovinzen), `tundra` praktisch nicht (richtig). Dynamische Typen (`farmland_*`, `pasture`, `plantation`, `cleared_land`, `mining`, `forestry`, `urban`, `docks`) setzt das Spiel selbst durch Gebäude, nicht über `province_terrains.txt`.
- 2026-11-04 Farmland: Die wirksame Maske ist `gfx/map/masks/mask_dynamic_farmland.png` (Liste erlaubter Provinzen baut das Spiel daraus beim Start neu). Im Mod steckte dort die Erdkarte (98 % deckungsgleich mit Vanilla) → Farmland an Erde-Stellen. Neues Werkzeug `.claude/tools/va_dynamic_masks.py` malt sie je Region nach neuem Terrain (plains 1.0, savanna 0.9, hills 0.55, forest 0.2, wetland/jungle 0.15, impassable/Gebirge/Schnee/Wüste/Unterwasser 0) mit Feld-Rauschen. EK (26–28) gemalt: 41 % der EK-Fläche (vorher 9,8 % zufällig). Test T-085. Forestry-/Mining-Maske und übrige Kontinente → VA-061.
- 2026-11-04 Kono: Karte plattmachen, Forst und Bergbau dazu. Alle drei Masken (`mask_dynamic_farmland/forestry/mining.png`) komplett geleert (`--clear`, keine Erde-Reste mehr), EK neu gemalt: Farmland 41 %, Forst 11,7 % (nur States mit `bg_logging`, `wood`-Hub voll), Bergbau 2,1 % (nur States mit `*_mining`, `mine`-Hub voll) der EK-Fläche. Übrige Kontinente bis VA-061 ohne dynamische Optik. Vorschau `.claude/regionen/va_masken_ek_vorschau.png`. Test T-085 erweitert.
- Status: EK fertig, wartet auf Spieltest (T-083 bis T-085).

