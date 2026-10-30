# VA-042: Charakter-Kleidung (alle in Lumpen) und Kartenfarben der Regionen

- **Status:** in Arbeit
- **Typ:** grafik
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Kono 2026-10-30:
1. Alle Personen laufen in Lumpen herum. Gebraucht werden Alternativen und eigene Grafiken.
2. Die Farbe der Regionen ist überall pissgelb.

## Ursache Kleidung (Analyse 2026-10-30)

- Vanilla `gfx/portraits/portrait_modifiers/01_clothes.txt` wählt die Kleidung über Trigger aus `common/scripted_triggers/00_clothes_triggers.txt`. Beispiel: `european_clothes_trigger` verlangt `has_discrimination_trait_group = heritage_group_european` oder Erde-Kulturen (`cu:japanese` …).
- Die Mod-Kulturen haben eigene Gruppen (`heritage_group_human`, `_elfen`, `_orc` … in `common/discrimination_traits/va_cultural_heritages.txt`). Kein Vanilla-Trigger greift, also gilt `fallback = default_clothes` mit `template = peasant_outfits`: Lumpen für alle, auch für Herrscher.
- `graphics = european` in den Kulturen betrifft nur Gebäude und Einheiten, nicht die Kleidung.

## Lösungswege (Entscheidung Kono)

1. **Schnell (Alternativen aus Vanilla):** Vanilla-Trigger gleichnamig zu überschreiben würde kollidieren. Deshalb eine eigene Datei in `gfx/portraits/portrait_modifiers/va_clothes.txt` mit eigenem Modifier-Block, der je Mod-Gruppe (Mensch, Elf, Zwerg …) Vanilla-Vorlagen zuweist (europäische Mäntel, Uniformen, Adelskleidung für Herrscher). Vorher prüfen, ob mehrere `clothes = {}`-Dateien zusammengeführt werden oder sich überschreiben.
2. **Trigger umbiegen:** `european_clothes_trigger` u. a. so ergänzen, dass auch `heritage_group_human` greift. Das wäre eine Vollkopie von `00_clothes_triggers.txt` und damit ein bewusster Vanilla-Override. Nicht empfohlen.
3. **Eigene Grafiken:** eigene Outfits je Volk (Elfen, Orks, Untote …) als Mesh/Textur unter `gfx/models/portraits/…` und eigene Templates im Gen `outfits`. Das ist echter Grafikaufwand, jeder Eintrag kommt in die Liste in VA-027.
- Nichtmenschliche Völker brauchen ohnehin eigene Modelle. Kleidung allein macht keinen Ork. Das gehört zu VA-027.

## Kartenfarben

- 70 Strategic Regions hatten `map_color = { 200 200 0 }` (Kalimdor 29, Eastern Kingdoms 28, Pandaria 12, Northrend 1).
- **Behoben 2026-10-30:** Per Skript bekommt jede Region eine eigene Farbe, die Farbtöne folgen dem goldenen Schnitt in Dateireihenfolge, damit benachbarte Einträge sich unterscheiden. Dateien: `common/strategic_regions/kalimdor_strategic_regions.txt`, `va_eastern_kingdom_strategic_regions.txt`, `va_northrend_strategic_regions.txt`, `va_pandaria_strategic_regions.txt`. Test: T-031.
- Falls Kono andere „Regionen“ meinte (z. B. State-Farben, Länderfarben): Bitte melden.

## Notizen

### 2026-10-30 – Kleidung über Vanilla-Vorlagen umgesetzt (Kono: „Ja, Vanilla-Vorlagen“)

- Weder ein zweiter `clothes = {}`-Block noch eine Vollkopie von `01_clothes.txt` (18.000 Zeilen). Stattdessen neue Datei `common/scripted_triggers/va_clothes_triggers.txt` mit `REPLACE:european_clothes_trigger` und `REPLACE:european_clothes_pop_trigger`. `REPLACE:` auf Scripted Triggers nutzt der Mod schon in `va_ai_triggers.txt`.
- Neuer Trigger `va_european_look_culture_trigger` (Scope culture) fasst die Völker mit europäischer Kleidung zusammen: Mensch, Zwerg, Gnom, Elf, Worgen, Draenei (`eredar`), Untote, Goblin, Ork, Troll, Tauren. Die beiden Vanilla-Trigger stecken in rund 60 Stellen der Porträtdateien (Kleidung, Hüte, Accessoires, Bärte). Damit greifen Herrscher-, Politiker-, Militär- und Agitator-Varianten automatisch.
- Die übrigen Völker (Murloc, Gnoll, Kobold, Harpyie, Stachelebern, Naga, Oger, Zentauren, Dämonen, Drachen …) bleiben vorerst in Lumpen. Zum Nachsteuern nur die Liste im Trigger ändern.
- Grenzen: Gruppen gibt es nur auf Kulturebene, eine Unterscheidung „Ork europäisch, Troll anders“ geht nur über weitere `REPLACE:` z. B. auf `arabic_clothes_pop_trigger` oder `african_clothes_pop_trigger`. Eigene Grafik bleibt TODO (siehe Datei, VA-027).
- Lint 0 neue Fehler. Test: T-032.
