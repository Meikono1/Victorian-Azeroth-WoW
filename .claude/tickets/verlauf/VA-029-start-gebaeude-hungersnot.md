# VA-029: Ressourcen und Start-Gebäude außerhalb Nord-EK setzen (Hungersnot)

- **Status:** in Arbeit
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Spieltest 2026-10-30 (Kono, 7 Jahre bis 1.1.625): Die ganze Welt stirbt, weil es keine Nahrung gibt. Beispiel Ironforge: 10,7 Mio. → 4,59 Mio. Pops, −7,5 %/Jahr, nur 25,6 Tsd. Beschäftigte, 770 Tsd. Bauern, 351 Tsd. Arbeitslose, 3,44 Mio. Abhängige, Lebensstandard 5,4. Silvermoon-Markt: Getreide −882, Holz −272 und weitere Engpässe.

## Ursache (Analyse 2026-10-30)

- **612 von 702 States mit Pops haben keine Start-Gebäude** (`common/history/buildings/*.txt`, leere `s:STATE_… = { }`-Blöcke). Das betrifft 323,7 von 420,8 Mio. Pops.
- Ohne Farmen, Ranches und Fischerei gibt es kaum Nahrung auf den Märkten, und ohne Arbeitsplätze sind die Pops arbeitslos oder abhängig. Der niedrige Lebensstandard treibt die Sterblichkeit.
- Subsistenz fängt das nicht auf: 5.000 Bauern je Stufe Ackerland, im Schnitt kommen aber rund 14.700 Pops auf eine Stufe. Beispiel `STATE_IRONFORGE`: 3,6 Mio. Pops, `arable_land = 14`, keine Gebäude.
- Kein Problem aus VA-002 (Firmen/Charaktervorlagen) und keine Defines: Mod-Defines ändern Wachstum und Sterblichkeit nicht. Der Rückgang läuft laut Pop-Grafik seit Spielstart gleichmäßig.
- Verwandt: VA-024 (Startwerte Nord-EK, dort 5 States ohne Gebäude und Pops vermutlich zu hoch).

## Lösungswege (Entscheidung Kono)

1. **Gebäude-History pro Region nachtragen** (Vorbild Vanilla `common/history/buildings/*.txt`): Farmen/Ranches/Fischerei nach `arable_resources` und `capped_resources`, dazu Grundindustrie und Verwaltung. Lore-genau, aber viel Arbeit (612 States). Ließe sich per Skript als Rohfassung erzeugen (Stufen aus Pops und Ackerland), die Kono dann je Region nachbessert.
2. **Pops senken**, bis Subsistenz und vorhandene Gebäude sie tragen (VA-024 „Gesamtbudget“). Hilft allein nicht gegen den Nahrungsmangel auf den Märkten.
3. Beides kombiniert: Pop-Budget festlegen, dann Gebäude-Rohfassung per Skript.

## Notizen

### 2026-10-30 – Stand je Region

Kono: Ressourcen und Gebäude wurden außerhalb von Nord-EK nie gesetzt. Es ist also fehlender Content, kein Fehler. Die Ressourcen in `map_data/state_regions` (`arable_land`, `arable_resources`, `capped_resources`) sind dort vermutlich Platzhalter und gehören mit zum Umfang.

| Region | States mit Pops | davon mit Gebäuden | Pops (Mio.) |
|---|---|---|---|
| 21 West-Northrend | 76 | 0 | 13,7 |
| 22 Ost-Northrend | 56 | 0 | 0,6 |
| 23 Nord-Kalimdor | 75 | 16 | 74,5 |
| 24 Zentral-Kalimdor | 55 | 0 | 53,0 |
| 25 Süd-Kalimdor | 45 | 0 | 32,4 |
| 26 Nord-EK | 78 | 73 | 83,4 |
| 27 Zentral-EK | 61 | 0 | 59,3 |
| 28 Süd-EK | 46 | 0 | 42,2 |
| 29 Outland | 82 | 1 | 60,5 |
| 30/31 Pandaria | 124 | 0 | 1,3 |
| 32–35 (je 1 State) | 4 | 0 | 0,0 |

Nur Nord-EK ist annähernd fertig. Reihenfolge-Vorschlag: Regionen mit vielen Pops zuerst (27, 24, 28, 25, 29, Rest von 23), Pandaria und Ost-Northrend zuletzt.

- Die alten Gebäudekopien (VA-003) definieren noch Namen vor 1.13 (`building_textile_mills`, `building_barracks`, `building_subsistence_pastures` usw.). Vanilla 1.13 kennt sie nur noch als `aliases`. Unverändert sind Farmen, Ranches, Minen, Holzfäller, Fischerei, Plantagen (außer Wein), Hafen, Verwaltung, Bausektor und Lebensmittelindustrie. Neue Gebäude-History zunächst nur mit diesen unveränderten Namen, dann ist sie vor und nach VA-003 gültig.

### 2026-10-30 – Vorgehen (Entscheidung Kono)

- **Region für Region**, nicht per Massenskript: Nord-EK, Mittel-EK, Süd-EK, danach Kalimdor, Northrend, Outland, Pandaria. Jede Region einzeln und eher grob; Claude schlägt vor und urteilt selbst, Kono nickt je Region ab.
- Werkzeug: `python -I .claude/tools/va_region_overview.py <NN> [--md DATEI]` (je State Besitzer, Pops, Kulturen, Ackerland, Ressourcen, Gebäudestufen). Übersichten liegen in `.claude/regionen/` (`26_nord_ek.md`, `27_mittel_ek.md`).
- Maßstab Vanilla 1.13 (Start 1836, 1.022 Mio. Pops, Stufen je Mio. Pops): Nahrung 2,1 · Plantagen 1,3 · Rohstoffe 0,8 · Industrie 1,1 · Verwaltung/Bau/Hafen 1,2 · Militär 1,5. Mod gesamt: 0,9 · 0,3 · 0,5 · 0,2 · 0,4 · 1,4. Pops je Stufe Ackerland: Vanilla 19.000, Mod 14.700. Die Pop-Menge an sich ist also nicht das Problem, es fehlen die Arbeitsplätze.
- **Korrektur:** Der Weltschnitt ist durch Indien und China (600 Mio. Pops, kaum Gebäude) verzerrt. Vanilla-Regionen mit Europa-Charakter, je Mio. Pops: Westeuropa Nahrung 4,7 / Rohstoffe 2,6 / Industrie 4,3 / Verwaltung 1,5; Südeuropa 5,5 / 1,7 / 2,6 / 1,3; Russland 4,4 / 2,6 / 1,5 / 0,6; Osteuropa 3,0 / 1,8 / 1,1 / 0,6. Maßstab für Azeroth deshalb: Nahrung 4,5, Rohstoffe 2,0, Plantagen 0,5.
- Werkzeug zum Auffüllen: `python -I .claude/tools/va_fill_buildings.py <NN>` (Probelauf mit Tabelle), `--apply` schreibt. Regeln stehen im Kopf des Skripts. Vorhandene Stufen werden angerechnet; ist ein Gebäudetyp im State schon da, erhöht das Skript dessen `levels` statt einen zweiten `create_building` anzulegen (sonst Laufzeitfehler „already exists“ wie in Archerus). Nur Gebäude mit unverändertem Namen, Besitz: Land. Ein zweiter Lauf meldet 0 Stufen.
- Zielwerte je Region am Maßstab Frankreich (siehe Nord-EK) ausrichten; Lore verschiebt die Gewichte (Zwerge: Minen × 1,5).

### Nord-EK (26) – grobe Einschätzung

- 79 States, 83,4 Mio. Pops, 1.368 Stufen, davon 407 Nahrung (4,9 je Mio., mit Plantagen). Militär (Kasernen) stark überwiegend: z. B. Deathholme 34 Kasernen, 2 Farmen; Gilneas City 40 Kasernen, keine Nahrung.
- Ohne Gebäude: Sun's Reach, Magisters' Terrace, Sunwell Plateau (je 10 Tsd. Pops, Platzhalter), Stratholme (1,58 Mio.), Aerie Peak (1,47 Mio.).
- Vorschlag: Nahrung und Rohstoffe in jedem State auf Vanilla-Niveau anheben (aus vorhandenen `arable_resources`/`capped_resources`), Verwaltung in Hauptstädten. Kasernen bleiben, keine neue Industrie. Untote bekommen trotz Lore gleich viel Nahrung, weil ihre Pops im Spiel genauso Nahrung brauchen.
- Erste Fassung (+262 Stufen, u. a. Eisen +22, Holz +36) verworfen. Kono: zu viele Ressourcen am Start, an Frankreich orientieren.
- **Maßstab jetzt Vanilla-Frankreich 1836** (29 States, 34,6 Mio. Pops), je Mio. Pops: Getreide 2,75 · Ranch 0,75 · Fisch 0,46 · Holz 0,93 · Kohle 0,38 · Eisen 0,17 · Schwefel 0,12 · Blei 0,09 · Plantagen ohne Wein 0,8 (Wein 2,26 fehlt, Name ändert sich mit 1.13) · Verwaltung 1,45. Das Skript rechnet je Gebäudeart auf **Regionsebene**: Liegt die Region schon über Frankreich, kommt nichts dazu. Der Rest geht an die States mit dem größten Rückstand.
- **Umgesetzt 2026-10-30:** Datei aus Sicherung zurückgesetzt, dann `va_fill_buildings.py 26 --apply`. +85 Stufen: Weizen 32, Kohle 24, Roggen 7, Blei 7, Mais 5, Schwefel 4, Reis 4, Ranch 2. Eisen, Holz, Fisch, Plantagen +0. Keine doppelten Typen je Block, zweiter Lauf 0. Stratholme und Aerie Peak haben jetzt Gebäude. Region danach: 1.453 Stufen.
- Nord-EK im Vergleich zu Frankreich (je Mio.): Getreide 2,75 (=), Ranch 0,74 (=), Kohle/Schwefel/Blei (=), aber aus Konos vorhandener History schon darüber: Fisch 0,67 (FRA 0,46), Holz 1,19 (0,93), **Eisen 0,32 (0,17)**.
- **Eisen gekürzt 2026-10-30** (Kono: „kürzen, das Spiel fängt gerade mit der industriellen Revolution an“): `va_fill_buildings.py 26 --trim building_iron_mine --apply`, 27 → 14 Stufen. Gekürzt zuerst, wo ein State am weitesten über seinem Anteil liegt; das letzte Eisen eines Landes bleibt. Emberstone, Deathknell, The Headlands je −2 (The Headlands damit ohne Eisen), Hearthglen, New Avalon, Zul'Aman, Undercity, Solliden, Sorrow Hill, Forsaken Rear Guard je −1. Klammern ausgeglichen, Lint 0 neue Fehler. 
- **Holz und Fisch gekürzt 2026-10-30** (Kono: „Ja, auch kürzen“): `--trim building_logging_camp` 99 → 77 (u. a. Stormglen Village −10, Sanctum of the Sun −5). `--trim fish` (Fischerei kürzen, Walfang zählt mit und bleibt): Fischerei 45 → 27, Walfang 11, zusammen 38 = 0,46 je Mio. (u. a. Koroth Den −3, Archerus −3, Sunsail Anchorage −4). Region danach 1.400 Stufen. Klammern ausgeglichen, Lint 0 neue Fehler, alle Arten jetzt auf Frankreich-Maßstab (Auffüllen und Kürzen melden 0).
- Bewusst offen: Quel'Danas-Platzhalter (Sun's Reach, Magisters' Terrace, Sunwell Plateau, je 10 Tsd. Pops, → VA-019/Konzept), Verwaltung (nur 27 Stufen für 83 Mio. Pops; Vanilla-Europa ~1,3 je Mio.; Hauptstädte bestimmen), Industrie (nach VA-003).
- Lint: 0 neue Fehler. `va_check_states.py 26`: Gebäude fehlen nur noch bei den drei Platzhaltern. Test: T-024, T-025.

### Mittel-EK (27) – umgesetzt 2026-10-30 (Kono: „Ja, Mittel-EK“)

- Ausgangslage: 69 States, 59,3 Mio. Pops, 2.431 Ackerland, **keine** Gebäude. Ressourcen noch im alten `bg_`-Format (lädt laut Log ohne Fehler).
- `va_fill_buildings.py 27 --apply`, Maßstab Frankreich: **+388 Stufen**. Roggen 109, Holz 55, Ranch 44, Baumwolle 33, Weizen 32, Fischerei 27, Kohle 26, Reis 13, Eisen 12, Hirse 9, Schwefel 8, Blei 6, Opium 5, Kaffee 3, Tee 3, Zucker 2, Tabak 1. Zwergen-States (Bronzebart, Wildhammer, Dunkeleisen) mit Minen × 1,5.
- Skript-Korrekturen dabei: Hirsefarm zählt als Getreide (Schwarzfels, Brennende Steppe). Fischerei nur in Küsten-States (`naval_exit_id`), weil fast jeder State in Mittel-EK den Platzhalter `bg_fishing = 11` hat, auch im Binnenland. Gebäude nur für Länder mit `create_state` im State. Kürzen rechnet mit demselben Zwergenfaktor wie Auffüllen. Nord-EK dadurch unverändert (Auffüllen und Kürzen melden 0).
- Prüfung: Klammern ausgeglichen, keine doppelten Typen, zweiter Lauf 0, Lint 0 neue Fehler. `va_check_states.py 27`: nur Crucible of Carnage ohne Gebäude (72 Tsd. Pops, unter der 100-Tsd.-Grenze).
- **Platzhalter für Kono (Lore):**
  - Vashj'ir (11 States, je 1 Mio. Naga): alle mit identischen Ressourcen (Roggen, Ranch, Eisen 36, Blei 18, Holz 23), also Roggenfarmen und Holzfäller unter Wasser. Vorschlag: Ressourcen auf Fisch/Seetang umstellen; bis dahin so gelassen, damit die Naga nicht hungern.
  - `bg_fishing = 11` in fast allen States, auch im Binnenland (Ironforge, Brennende Steppe, Sengende Schlucht).
  - 8 unbesiedelte States mit denselben Platzhalter-Ressourcen wie Vashj'ir (Tol Barad, Teile des Schattenhochlands: Largo Overlook, Darkwood, Farson Hold, Forgotten Hill, Ironclad Garrison, Slagworks, Baradin Hold, Warden's Vigil).
  - Gol'Bolar Quarry: Dark Iron Clan hat Pops, aber kein `create_state` (bekommt keine Gebäude).

### 2026-10-30 – Hinweise Kono

- Nur Gebäude geändert, keine Ressourcen-Vorkommen (`map_data/state_regions` unverändert).
- **Dunkeleisenzwerge** (Dark Iron, Schwarzfels-Gebiet) waren so gedacht, dass sie Nahrung über Fleisch und Werkzeuge bekommen statt über Ackerbau. Später einbauen (z. B. eigenes Nahrungsgebäude/PM oder Pop-Bedürfnis), vorerst Hirse/Roggen und Ranches wie überall.
- Vashj'ir: Provinzen neu zeichnen und Ressourcen → VA-030.

### 2026-10-30 – Länderprofile und Fischerei (Kono)

- Kono: „Jedes Reich sollte eine Persönlichkeit haben“ – Ressourcen nicht gleichmäßig je State, sondern nach Land (Macht, Kultur, Lore).
  - Neu: `.claude/tools/va_profiles.py` mit Länder- und Kulturprofilen (Faktor je Gruppe `all`/`food`/`fish`/`plantation`/`wood`/`mines`). Der Zwergenfaktor steckt jetzt dort. Bisher nur Süd-EK-Länder eingetragen.
  - `va_fill_buildings.py` verteilt jetzt je (State, Land) statt je State und vergibt Stufen einzeln nach Rückstand. Kleine Mitbesitzer verlieren dadurch nicht mehr in jedem State den Rundungsrest.
  - Nahrung hat die Untergrenze 0,8 (`FOOD_MIN`), damit schwache Reiche nicht verhungern; Schwäche zeigt sich bei Holz, Minen, Plantagen.
  - Nord- und Mittel-EK sind noch ohne Profile gefüllt. Ein Lauf meldet dort jetzt +1 Fischerei (Steamwheedle-Profil in Stormgarde Keep); nicht angewendet.
- **Fischerei-Platzhalter entfernt:** `bg_fishing = 11` bzw. `building_fishing_wharf = 11` in 296 Binnen-States (ohne `naval_exit_id`) aller Regionen. Andere Werte im Binnenland bleiben, weil handgesetzt (Lordamere-See: Fenris Isle 14, Scholomance 7; Zangarmarschen u. a.). Küsten-States behalten ihren Wert (meist 11). Keine Gebäude-History betroffen. Lint 0 neue Fehler. Test: T-027.

### Süd-EK (28) – umgesetzt 2026-10-30 (Kono: „Ja, schreiben“)

- Ausgangslage: 46 States, 42,2 Mio. Pops, keine Gebäude.
- `va_fill_buildings.py 28 --apply` mit Länderprofilen: **+319 Stufen** (davon 238 Nahrung). Weizen 88, Holz 45, Reis 39, Ranch 37, Fischerei 27, Baumwolle 25, Kohle 18, Kaffee 9, Eisen 8, Schwefel 6, Tee 5, Hirse 5, Blei 4, Roggen 2, Opium 1.
- Je Mio. Pops: Stormwind 10,4 · Steamwheedle 9,6 · Zanzil 9,0 · Gurubashi 8,1 · Defias 7,6 · Schwarzfels 4,5 · Gnolle, Oger, Worgen 2–4. Kleinstländer unter 0,25 Mio. bekommen nichts.
- Prüfung: Klammern ausgeglichen, keine doppelten Typen, zweiter Lauf 0, Lint 0 neue Fehler. `va_check_states.py 28`: nur Grosh'gok Compound ohne Gebäude (230 Tsd. Ogerpops, Anteil unter einer Stufe). Nebenbei gefundene Hub-/Provinzfehler → VA-033.
- Offen wie in Nord-EK: Weinberge (Stormwind, Goldshire, MacLure, Westbrook, Northshire) ohne Gebäude, bis VA-003 den Namen klärt; Verwaltung und Industrie. Ressourcen noch im alten `bg_`-Format.
- Test: T-028.

### 2026-10-30 – Feinabstimmung später (Kono)

- Länderprofile in `va_profiles.py` werden erst verfeinert, wenn für die Reiche Events und Content entstehen. Für die übrigen Regionen also grob weiterarbeiten.
- Spieltest mit annex all: Nazjatar hungert noch → VA-030 (Fischerei und eigene Gebäude).
- `error.log` vom 2026-10-30 14:23 ausgewertet: keine Fehler aus Süd-EK (28) und `map_data/state_regions`. Kono: Der neue Stand war im Lauf schon drin. Spieltests T-024/T-026/T-027/T-028 (Sichtprüfung) stehen noch aus.
- **Fehler behoben:** Deathholme (Tech-Stufe 6) bekam beim Nord-EK-Lauf Kohle 1 und Blei 1. Minen brauchen `shaft_mining`, das Stufe 6/7 nicht hat („must have invented Shaft Mining“, `26_north_eastern_kingdoms.txt:1147/1158`). Beide Einträge entfernt. `va_fill_buildings.py` vergibt Minen jetzt nur an Länder mit `shaft_mining` (`without_shaft_mining()`). Sonst ist kein Land mit Minen betroffen. Lint 0 neue Fehler.

### 2026-10-30 – Häfen, Ackerland, Outland-Fehler (Spieltest Kono)

- **Start-Häfen:** Kono: Stormwind, Defias, Gnomeregan brauchen einen Hafen, alle Länder sollen am Weltmarkt hängen. Neu `va_add_ports.py <Präfixe> [--apply]`: Hafen für jedes Land mit Küsten-State und ohne Hafen, in der Hauptstadt bzw. im größten Küsten-State, Stufe 1 + je 5 Mio. Pops, höchstens 3; nur mit `navigation` (Tech-Stufe 1–5). Angewendet auf 21–28: **106 Häfen, 118 Stufen**. Outland (29) und Pandaria (30/31) bewusst nicht (eigene Welt bzw. Nebel, Entscheidung offen). Zweiter Lauf 0, Klammern ausgeglichen.
- `va_fill_buildings.py`: `without_tech(tech)` statt `without_shaft_mining()`, gilt für Minen und Häfen.
- **Ackerland erhöht** (Kono): Zul'Aman 70 → 110, Crown Guard Tower 62 → 75, The Bulwark 38 → 60, Deathknell 37 → 65, Aerie Peak 35 → 55; Aerie Peak dazu Ranch 3 und Mais +2. Pop-Vorschläge → VA-024.
- **Outland-Datenfehler:** `STATE_MANAFORGE_BNAAR` `arable_land = 6a0` → 60 korrigiert. Offen: `common/history/pops/va_outlands.txt:1618` `size = zombie` (STATE_EXPEDITION_ARMORY / UNYIELDING_DEFENDER, Kultur stormwindian), richtiger Wert unbekannt → bei Region 29 klären. Beides fand weder Lint noch error.log; `va_region_overview.py` warnt jetzt bei ungültigen Zahlen statt abzubrechen.
- Lint 0 neue Fehler. Test: T-029.

### Zentral-Kalimdor (24) – Vorschlag 2026-10-30, wartet auf Kono

- Ausgangslage: 55 States, 53,0 Mio. Pops, 2.158 Ackerland, nur die 17 Hafenstufen. Übersicht: `.claude/regionen/24_zentral_kalimdor.md`.
- **Alle 53 besiedelten States haben genau 1.000 Tsd. Pops** (Platzhalter, Kulturen je Besitzer gleich verteilt). Die Gebäude richten sich danach; werden die Pops später lore-genau gesetzt, Region neu füllen.
- Länderprofile `_ZENTRAL_KALIMDOR` in `va_profiles.py` (38 Länder): Orgrimmar 1,3 (Minen hoch, Nahrung 0,9), Thunder Bluff 1,2 (Ranches × 1,6, Minen 0,5), Theramore 1,2 (Fisch 1,5), Darnassus 1,1 (Holz/Minen 0,5), Burning Blade 0,7, Onyxia 0,4, Stämme 0,4–0,6. Nord-, Mittel-, Süd-EK bleiben unverändert (Probelauf 0 / +1 bekannt / 0).
- Probelauf: **+319 Stufen** (Mais 53, Ranch 41, Holz 40, Fischerei 30, Baumwolle 29, Roggen 24, Hirse 24, Weizen 20, Kohle 17, Reis 16, Eisen 8, Kaffee 8, Schwefel 5, Blei 4). Je Mio. Pops: Theramore 10,6 · Thunder Bluff 7,6 · Orgrimmar 7,4 · Darkspear 8,0 · Burning Blade 4,8.
- Platzhalter: `STATE_KEZAN` und `STATE_LOST_ISLES` liegen in Region 24 (Besitzer `KALIMDOR`, je 10 Tsd. sin_dorei-Pops), bekommen nichts.
