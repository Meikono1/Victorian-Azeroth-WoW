---
name: va-karte
description: Karten- und State-Arbeit im Victorian-Azeroth-Mod – State Regions, Provinzen (xRRGGBB), Hubs (city/port/farm/mine/wood), impassable, Besitz und State-History, Pops, Start-Gebäude, Ressourcen/arable_land, Häfen, Handelszentralen, Strategic Regions, provinces.png, Ingame-Map-Editor. Nutzen bei Tickets zu Regionen (Präfix 21–35), Hungersnot/Startwerten, Provinzen löschen oder verschieben und nach Kartenarbeit von Kono.
---

# Karte, States, Startwerte (Victorian Azeroth)

## 1. Orientieren ohne große Dateien zu lesen

State-Dateien sind 40–130 KB, `province_terrains.txt` 560 KB, `provinces.png` 8192 × 3616. Nie ganz lesen.

1. Präfix und Dateien der Region aus der Regionentabelle in `.claude/KARTE.md`.
2. Überblick über die Werkzeuge statt Dateien:
   - `python -I .claude/tools/va_region_overview.py NN` – je State Besitzer, Pops, Kulturen, Ackerland, Ressourcen, Start-Gebäude. Mit `--md .claude/regionen/NN_<name>.md` die Übersicht ablegen; liegt sie schon in `.claude/regionen/`, die lesen.
   - `python -I .claude/tools/va_check_states.py NN` – Prüfung gegen Karte, History, Pops, Gebäude, Länder (`--no-png` schneller, `--assign-test` für STATE_TEST).
3. Einen einzelnen State gezielt holen: `grep -n "^STATE_X = {" map_data/state_regions/NN_*.txt`, dann mit Offset ~25 Zeilen lesen. In der History: `grep -n "s:STATE_X = {" common/history/<states|pops|buildings>/…`.
4. Wer besitzt was: `grep -n "country = c:TAG" common/history/states/VA_*.txt`.

## 2. Formate (Mod-Stand 1.13)

- **State Region** (`map_data/state_regions/NN_va_*.txt`): `id = NNxx` (Präfix × 100 + laufende Nr.; vor neuer ID die höchste vergebene per `grep -oE "^    id = [0-9]+"` prüfen), `subsistence_building`, `provinces = { "x…" }`, `impassable`, `prime_land`, `traits`, Hubs `city`/`farm`/`mine`/`wood`/`port` (müssen Provinzen **dieses** States sein), `arable_land`, `arable_resources = { "building_…" }`, `capped_resources = { building_… = N }` (1.13-Format), `naval_exit_id` (nur Küstenstates, Meer-State aus `80_va_seas.txt`).
- **State-History** (`common/history/states/VA_*.txt`): `STATES = { s:STATE_X = { create_state = { country = c:TAG owned_provinces = { x… } } add_homeland = cu:<kultur> } }`. Geteilte States: mehrere `create_state`, Provinzen ohne Anführungszeichen.
- **Pops** (`common/history/pops/va_*.txt`): `POPS = { s:STATE_X = { region_state:TAG = { create_pop = { culture = … size = … } } } }`.
- **Gebäude** (`common/history/buildings/NN_*.txt`): `BUILDINGS={ s:STATE_X={ region_state:TAG={ create_building={ building="…" add_ownership={ country={ country="c:TAG" levels=N } } reserves=1 activate_production_methods={ "pm_…" } } } } }`. Maßstab Vanilla-Frankreich 1836 (Kono: nicht zu viele Ressourcen am Start).
- **Adjazenz** (`map_data/adjacencies.csv`, `;`-getrennt): `From;To;Type;-1;x1;y1;x2;y2;;Kommentar`. `sea` = Land↔Land über Wasser, `special` = beliebige Entfernung (DarkPortal). Koordinaten = Pixel in `provinces.png`, **y gespiegelt** (Höhe 3616 − y). Statisch, keine Geschwindigkeit je Kante; `nodes.dat` ist binär und nicht editierbar. Meerengen (`strait_definitions`) verbinden nur Seezonen (VA-053).
- **Loc**: State-Namen in `localization/replace/english/map/va_states_l_english.yml`, Hubs in `va_hub_names_l_english.yml` (nur greppen).

## 3. Werkzeuge für Startwerte (Probelauf ohne `--apply`)

| Aufgabe | Aufruf |
|---|---|
| Nahrung, Rohstoffe, Plantagen auffüllen | `va_fill_buildings.py NN [--trim GEBÄUDE] [--apply]`, Länder-/Kulturprofile in `va_profiles.py` |
| Verwaltung und Bausektor | `va_add_gov_buildings.py NN … [--apply]` |
| Häfen für Küstenländer | `va_add_ports.py NN … [--apply]` |
| Handelszentralen | `va_add_trade_centers.py NN … [--apply]` |

Immer erst den Probelauf zeigen bzw. prüfen, dann `--apply`, danach `va_check_states.py NN` und `va_lint.py --regions NN`.

## 4. Regeln

- **Große Binärdateien** (`provinces.png`, `heightmap`, `.bin`, `.dds`, `nodes.dat`) nur auf ausdrücklichen Wunsch anfassen. Lesen mit numpy/Pillow ist erlaubt (Prüfskripte tun das).
- **Provinzen löschen nur vollständig** (VA-031): Farbe aus `provinces.png` weg **und** jede Referenz weg (`state_regions` inkl. `impassable`/`prime_land`/Hubs, `common/history/states`, `province_terrains.txt`, `default.map`, `adjacencies.csv`, `strategic_regions`). Referenz ohne Farbe → Absturz beim Start; Farbe ohne Referenz → weißer Fleck und Fehler je Frame. Danach gegenprüfen: ID-Suche über alle Textdateien = 0 und Farbsuche in `provinces.png` = 0.
- **Map-Editor**: Der Ingame-Editor schreibt in `Documents\…\mod\warcraft`, nicht ins Repo. Nach Konos Kartenarbeit daran erinnern, die Dateien zurückzuholen (Kono kopiert selbst; Claude öffnet `mod\` nur auf ausdrücklichen Wunsch).
- `replace_paths` umfasst `map_data` und `common/history/*`: Vanilla-Dateien dort zählen nicht, alles muss im Mod stehen.
- Neue States: ID im Präfix-Bereich, Loc-Name, `create_state` in der History, sonst fehlt der State im Spiel.

## Stolperfallen

- Hubs zeigen nach Verschiebungen oft auf fremde oder gelöschte Provinzen (VA-015, VA-033) → `va_check_states.py` meldet das.
- Nicht jede Bergprovinz ist `impassable`, dadurch springen Stadt-/Hafenmarker (VA-037).
- `navigation` Stufe 6/7 bekommt keinen Hafen, sonst Ladefehler „must have invented Navigation“.
- 1.13 handelt nur über `building_trade_center`; ohne Zentrale kein Import/Export (VA-040).
- Ohne Verwaltung und Bausektor in der Start-History stapelt die KI genau diese Gebäude (VA-044).
- Tippfehler in Zahlen findet weder Lint noch error.log (`arable_land = 6a0`, `size = zombie` in VA-029) → bei Regionsarbeit `va_region_overview.py` auf Ausreißer ansehen.
- `STATE_TEST` und leere States (0 Provinzen, z. B. `STATE_BARADIN_HOLD`) sind bekannte Altlasten (VA-018, VA-031).
- Gebäude-History mit PMs eines anderen Gebäudes (Reisfarm mit `pm_saw_mills`) oder `add_ownership = { country = { type … } }` meldet error.log nur als „Invalid production method“/„Unexpected token“ → bei Kopien aus anderen Blöcken PMs prüfen (VA-043).
- Vanilla-`aliases` (`building_barracks`, `building_subsistence_farms`) gelten nur für Spielstände, nicht in History/`map_data` → immer den echten 1.13-Namen schreiben (VA-043).
- Startgesetze, die ein Land nicht halten darf (fehlende Technik), tauscht das Spiel beim Start aus und meldet `country_law_manager` → das gemeldete Ersatzgesetz direkt in die History schreiben (VA-014).
