# Karte: Werkzeuge

Teil der Code-Karte, Index: [`KARTE.md`](../KARTE.md). Pflege wie dort.

## Werkzeuge (`.claude/tools/`, Aufruf immer `python -I`)

| Skript | Zweck | Schreibt? |
|---|---|---|
| `va_lint.py [--regions NN …]` | Prüfung vor jeder Testrunde (BOM, Loc, Verweise, Duplikate, States) | nein |
| `va_errlog.py [--mod] [--top N] [--filter TEXT] [--by-file]` | error.log zusammenfassen; `--mod` nur Quelldateien aus dem Repo (9.581 → 967 Einträge) | nein |
| `va_check_states.py NN` | State-Region gegen Karte, History, Pops, Gebäude, Länder | nein |
| `va_region_overview.py NN [--md DATEI]` | Regionsübersicht je State (Besitzer, Pops, Ackerland, Gebäude) | nur `--md` |
| `va_events.py`, `va_common_folders.py <ordner>` | Vanilla-Dateien als Erde/allgemein/WoW einstufen, Stubs anlegen | mit `--stubs`/`--apply-copies` |
| `va_fill_buildings.py NN [--apply]` | Start-Gebäude auffüllen (Profile in `va_profiles.py`) | mit `--apply` |
| `va_add_gov_buildings.py`, `va_add_ports.py`, `va_add_trade_centers.py` | Verwaltung/Bausektor, Häfen, Handelszentralen ergänzen | mit `--apply` |
| `va_country_overview.py [--md DATEI] [--tag TAG]` | Länderübersicht (Charaktere, JEs, Formables, eigene Gebäude, Politik, Subjekte, fehlende Namen/Flaggen) | nur `--md` |
| `va_icon.py QUELLE ZIEL.dds [--size N] [--keep-aspect]` | Bild → Vic3-Icon (DDS BGRA mit Mipmaps wie Vanilla), Quellen in `.claude/grafik_quellen/` (VA-027); `--keep-aspect` für Event-Bilder (Breite N, z. B. 1280) | ja |
| `va_gen_dead_scar.py` | Todesschneisen-Buttons, -Balken, -Effekt erzeugen | ja |
| `va_terrain.py NN … [--png DATEI] [--apply]` | Provinz-Terrain aus Geländetexturen und Heightmap ableiten → `province_terrains.txt` (VA-051) | mit `--apply` |
| `va_dynamic_masks.py NN … [--masks …] [--clear] [--png ORDNER] [--apply]` | Dynamische Masken `gfx/map/masks/mask_dynamic_farmland/forestry/mining.png` je Region aus Terrain und Ressourcen malen, `--clear` leert die ganze Karte (VA-051) | mit `--apply` |
| `va_scar_mask.py NN STATE_… [--fill xRRGGBB …] [--free-others] [--scar-only] [--remove] [--apply]` | Todesschneise je State aus der Vorlage `.claude/regionen/va_dead_scar_form.png` in `mask_dynamic_mining.png` malen, `--fill` bemalt ganze Provinzen, `--free-others` leert dort Farmland/Forst, `--scar-only` lässt in den States nur die Schneise in der Bergbau-Maske (VA-062). Nach jedem `va_dynamic_masks.py`-Lauf über Region 26 erneut mit allen Optionen laufen lassen (Befehl im Ticket VA-062) | mit `--apply` |
| `va_gen_geo_regions.py [--apply]` | leere Erde-`geographic_regions` erzeugen (bei Patches) | mit `--apply` |
| `va_gen_earth_je_stubs.py [--apply]` | nie aktivierbare Hüllen für abgeschaltete Erde-JEs (bei Patches, nach neuen Stubs) | mit `--apply` |
| `va_gen_earth_template_stubs.py [--apply]` | leere Hüllen für aufgerufene Erde-Charaktervorlagen | mit `--apply` |
| `va_gen_earth_event_stubs.py [--apply]` | versteckte Hüllen für abgeschaltete Erde-Events → `events/va_earth_event_stubs/` | mit `--apply` |
| `va_gen_earth_overrides.py [--apply]` | Vanilla-Dateien mit Erde-States in oft geprüften Bedingungen entschärft übernehmen (Liste `FILES`: Monumente, Kanäle, Machtblock-Namen, Pan-Bewegungen, Erde-Regierungsformen, Errungenschaften, Flaggen; erkennt States, `sr:` und `c:`-Tags; Schlüssel als Pfad `flag_definition/trigger` für zweite Ebene) | mit `--apply` |
| `va_release_stats.py [--ref R] [--save V] [--compare V]` | Inhaltszahlen je Release (JEs, Events, Modifier, Texte, Wörter, AI WRITTEN …; zählt nur Namen, die Vanilla nicht kennt). Stände in `.claude/releases/version_*.json`, Basis `2025-12` | mit `--save` |
| `va_pop_report.py` | Startbevölkerung Vanilla gegen Mod → `.claude/regionen/bevoelkerung_vanilla_vs_mod.md` | ja |
| `va_doku_check.py [--all]` | Größe der Projekt-Doku gegen die Grenzen prüfen (VA-074); Exit 1 bei Überschreitung | nein |
| `va_script.py` | Bibliothek: Paradox-Script-Parser, wirksame Datei (Mod über Vanilla) | – |
