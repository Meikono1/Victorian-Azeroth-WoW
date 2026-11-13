# Testprotokoll

Jede Änderung, die Claude macht, bekommt hier einen Testfall. Kono testet im Spiel und hakt ab. Ein Ticket gilt erst als `erledigt`, wenn alle seine Testfälle **OK** sind.

**Ablauf je Testrunde**

0. Claude: `va_lint.py` meldet 0 neue Fehler (Voraussetzung für die Freigabe).

1. Repo-Stand in den Mod-Ordner `mod\warcraft` kopieren.

2. Victoria 3 starten, Kampagne mit dem Mod laden, Tests unten durchgehen.

3. Spiel beenden und Claude Bescheid geben. Claude wertet `error.log` aus (Testfall „Log“ der Runde) und trägt das Ergebnis ein.

4. Ergebnis je Test eintragen: `[x] OK` oder `[x] Fehler` plus kurze Notiz (was stattdessen passiert ist, Screenshot-Name).

Abgeschlossene Runden wandern nach `TESTPROTOKOLL_ARCHIV.md` (Historie); hier stehen nur Runden mit offenen Testfällen. Bei einem Fehler legt Claude ein Ticket an oder öffnet das zugehörige wieder.

---

> **Release Version 3 (Kono 2026-11-13):** Offene Blocker-Tests T-073–T-076, T-113 (drittes/viertes Loa), T-131, T-132 sowie die Log-Fälle T-077/T-118 werden nach dem Release nachgeholt; Spieler testen mit.

## Runde 1 – Nord-EK, Quel'Danas, Zul'Jarra, Mana (Stand 2026-10-30)

Tickets: VA-015, VA-006, VA-019. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Zum Testen am besten als **Silvermoon** spielen.

### T-003 Stadt- und Hafenmarker sitzen sinnvoll

- **Schritte:** Auf der Karte heranzoomen bei Gilneas City, The Headlands, Scholomance, Northgate Woods (Hafen) und Seradane.

- **Erwartet:** Stadt, Farm, Mine, Holz und Hafen stehen jeweils im eigenen State, nicht im Wasser oder Gebirge. Northgate Woods hat einen Hafen an der Küste.

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: noch grafische Fehler, wird später genauer angesehen. Hängt mit fehlenden impassable-Bergprovinzen zusammen (VA-037). Offen.

## Runde 5 – Firmen und Charaktervorlagen aus replace_paths (Stand 2026-10-30)

Tickets: VA-002. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Kann mit den offenen Tests aus Runde 1 laufen. `mod\warcraft` vorher **leeren** und neu befüllen: `common/character_templates/default_template.txt` ist gelöscht und darf dort nicht mehr liegen (sonst gibt es `default` doppelt).

### T-021 Charaktere: Lebensdauer und Religion

- **Schritte:** Kampagne als Silvermoon starten. Herrscher, Erben und zwei Interessengruppen-Anführer ansehen (Eigenschaften, Religion). Ein Jahr laufen lassen, einen neu erschienenen Charakter (Agitator, General oder neuer IG-Anführer) ansehen.

- **Erwartet:** Elfen tragen die Eigenschaft für 50.000 Jahre Lebensdauer, neue Charaktere ebenso. Charaktere der Hauptkultur haben die Staatsreligion. Keine Charaktere mit Erde-Namen oder Erde-Kulturen.

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-022 Firmen: nur Basisfirmen

- **Schritte:** In derselben Kampagne den Reiter Firmen öffnen (mögliche Firmen).

- **Erwartet:** Nur allgemeine Basisfirmen (Fischerei, Holz, Textil …), keine historischen Firmen (Fiat, Suez, Škoda …).

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

## Runde 6 – Nord- und Mittel-EK: Start-Gebäude aufgefüllt (Stand 2026-10-30)

Tickets: VA-029. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Kann mit Runde 5 und den offenen Tests aus Runde 1 laufen. `mod\warcraft` neu befüllen.

### T-024 Nord-EK: Nahrung und Bevölkerung

- **Schritte:** Kampagne als Silvermoon starten. Undercity, Gilneas, Stratholme (Plaguelands) und Aerie Peak im Staatenfenster ansehen: Farmen, Ranches, Fischerei, Holz, Minen vorhanden? Markt von Silvermoon und Undercity ansehen (Getreide, Fleisch, Fisch). 5 Jahre laufen lassen, Bevölkerungsgrafik von Silvermoon, Undercity und Gilneas ansehen.

- **Erwartet:** Nord-EK-Staaten haben Nahrungs- und Rohstoffgebäude, Eisenminen nur wenige (14 Stufen in der Region). Nahrungsengpässe auf den Märkten deutlich kleiner als vorher (Getreide vorher −882 in Silvermoon). Bevölkerung in Nord-EK schrumpft nicht mehr dauerhaft (leichtes Auf und Ab ist normal). Andere Regionen hungern weiter, das ist erwartet (VA-029, nächste Regionen).

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-026 Mittel-EK: Nahrung und Bevölkerung

- **Schritte:** In derselben Kampagne Ironforge, Gnomeregan, Grim Batol und Menethil (Sumpfland) im Staatenfenster ansehen. Nach 5 Jahren Bevölkerungsgrafik von Ironforge ansehen (vorher 10,7 → 4,59 Mio. in 7 Jahren).

- **Erwartet:** Mittel-EK-Staaten haben Farmen, Ranches, Holzfäller und Minen. Ironforge schrumpft nicht mehr dauerhaft. Vashj'ir hat bewusst noch Platzhalter-Gebäude (Roggen, Holz), siehe VA-029.

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-025 error.log: Gebäude Nord- und Mittel-EK (Claude)

- **Schritte:** Nach T-024 und T-026 Claude Bescheid geben.

- **Erwartet:** Keine neuen Fehler aus `common/history/buildings/26_north_eastern_kingdoms.txt` und `27_center_eastern_kingdoms.txt`, kein „Tried to create building … already exists“ außer dem bekannten Archerus-Fischkai (VA-024). Kein „must have invented Shaft Mining“ mehr bei Deathholme (Zeile 1147/1158 im Log vom 30.10., behoben). Keine ungültigen Produktionsmethoden.

- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: Log 30.10. 14:23 (Stand mit Süd-EK): einziger Fehler Deathholme-Minen (26:1147/1158), behoben. Sonst nichts aus `history/buildings` oder `state_regions`, auch kein „already exists“. Nächster Lauf bestätigt den Fix.

### T-027 Fischerei-Platzhalter im Binnenland entfernt (VA-029)

- **Schritte:** Kampagne starten. Ironforge (Binnenland) und Stormwind (Küste) im Staatenfenster öffnen, unter Ressourcen nachsehen.

- **Erwartet:** Ironforge hat keine Fischerei mehr als Ressource, Stormwind schon. Fenris Isle und Scholomance (Lordamere-See) haben weiter Fischerei. `error.log` ohne neue Zeilen aus `map_data/state_regions/` (Claude prüft mit T-025).

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-028 Süd-EK: Nahrung und Länderprofile (VA-029)

- **Schritte:** In derselben Kampagne Stormwind, Booty Bay, Zul'Gurub und Redridge Canyons im Staatenfenster ansehen. Nach 5 Jahren Bevölkerungsgrafik von Stormwind und Booty Bay ansehen.

- **Erwartet:** Stormwind deutlich besser ausgebaut (Farmen, Holz, Ranches) als Gnoll- und Orkgebiete. Booty Bay mit Fischerei und Kaffee. Stormwind schrumpft nicht mehr dauerhaft. `error.log` ohne neue Fehler aus `common/history/buildings/28_south_eastern_kingdoms.txt` (Claude prüft mit T-025).

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-029 Häfen und Ackerland (VA-029)

- **Schritte:** Kampagne starten. Stormwind, Ironforge (Coldridge Valley), Gnomeregan, Deadmines, Orgrimmar im Staatenfenster öffnen. Zul'Aman, Deathknell, The Bulwark, Aerie Peak ansehen. Nach 2 Jahren Food Security in Nord-EK erneut ansehen.

- **Erwartet:** Genannte States haben einen Hafen, die Länder haben Weltmarkt-Zugang. Mehr Ackerland in den fünf Nord-EK-States, Aerie Peak mit Ranch. Weniger Hunger in Zul'Aman, Deathknell, Bulwark, Aerie Peak. `error.log` ohne „must have invented Navigation“ und ohne neue Fehler aus `common/history/buildings/2*` (Claude).

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-030 Pops gekürzt in Undercity, Scholomance, Shadowfang Keep (VA-024)

- **Schritte:** Kampagne starten, die drei States im Staatenfenster öffnen. Nach 2 Jahren Food Security und Lebensstandard ansehen.

- **Erwartet:** Undercity ~2,0 Mio., Scholomance ~0,6 Mio., Shadowfang Keep ~1,0 Mio. Pops. Weniger Hunger und Arbeitslose als vorher. Archerus unverändert 2,55 Mio.

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-031 Farben der Strategic Regions (VA-042)

- **Schritte:** Kampagne starten, Kartenmodus „Strategische Regionen“ öffnen (bzw. die Ansicht, in der alles gelb war). Kalimdor, Eastern Kingdoms, Northrend und Pandaria ansehen.

- **Erwartet:** Jede Strategic Region hat eine eigene Farbe, nichts mehr einheitlich gelb. Nachbarregionen sind meist deutlich verschieden; sonst Kono meldet, welche, dann passt Claude einzeln an. `error.log` ohne neue Zeilen aus `common/strategic_regions/` (Claude).

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-032 Kleidung statt Lumpen (VA-042)

- **Schritte:** Kampagne starten. Herrscher und Politiker von Stormwind, Ironforge, Silvermoon, Undercity, Orgrimmar und Thunder Bluff ansehen (Länderfenster, Interessengruppen). Außerdem ein Pop-Porträt in Stormwind und einen Murloc- oder Gnoll-Herrscher.

- **Erwartet:** Menschen, Zwerge, Gnome, Elfen, Worgen, Draenei, Untote, Goblins, Orks, Trolle und Tauren tragen europäische Kleidung (Mäntel, Uniformen, Herrscherkleidung), keine Lumpen mehr. Murlocs, Gnolle u. a. bleiben vorerst in Lumpen. Kono notiert, welche Völker anders aussehen sollen. `error.log` ohne Zeilen zu `va_clothes_triggers.txt` und ohne „unknown trigger“ (Claude).

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-033 error.log: Kleidung, Kartenfarben, Gebäude Nord-EK (Claude)

- **Schritte:** Nach T-031 und T-032 Claude Bescheid geben.

- **Erwartet:** Keine Zeilen zu `va_clothes_triggers.txt`, `european_clothes_trigger` oder `common/strategic_regions/`. Kein „Both levels and ownerships are undefined“ mehr aus `common/history/buildings/26_north_eastern_kingdoms.txt`. Keine „should be in utf8-bom“-Meldungen mehr für Mod-Dateien.

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz: Lauf 30.10. 17:50–17:52 (Repo = Mod-Ordner): nichts zu Kleidung oder Regionsfarben. Gefunden und behoben: 8 leere `add_ownership` in 26er Gebäuden (alt, schon im letzten Commit), fehlendes BOM in 70 Mod-Dateien (darunter die Strategic Regions). Nächster Lauf bestätigt die Fixes. Restbefunde → VA-043.

## Runde 15 – Wretched Schritt 2–4 (Stand 2026-11-03)

Ticket: VA-021. Lint vor Freigabe: 0 neue Fehler (2026-11-03). Neue Kampagne nötig (Charaktere und Sucht-Stufe kommen aus der Start-History).

### T-071 Sucht-Stufen (VA-021)
- **Schritte:** Neue Kampagne als Silvermoon. `play WRETCHED_BLOODELFES`, Modifier ansehen, zurück. Pakt anbieten (bzw. Konsole), 12 Monate Protektorat ohne Mana-Knappheit bei den Wretched laufen lassen. Gegenprobe: Wretched 12 Monate im Mana-Entzug.
- **Erwartet:** Wretched starten mit „Desperate Hunger (AI WRITTEN)“ (Stufe 3) statt „Wretched Addiction“. Nach 12 Monaten versorgtem Protektorat „Gnawing Hunger“ (Stufe 2), nie tiefer ohne Heilung. 12 Monate Entzug: eine Stufe höher.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Start „Desperate Hunger“, später „Gnawing Hunger“. Gegenprobe 12 Monate Entzug nicht getestet (kein Release-Blocker).

### T-072 Heilen in drei Etappen und Rückfall (VA-021)
- **Schritte:** Protektorat, „Begin the Healing“. Balken bis 20, 40, 60 laufen lassen (Konsole/Zeit). Einmal Mana bei den Wretched 3 Monate knapp machen (Entzug).
- **Erwartet:** Start: Wretched „Supervised Withdrawal (AI WRITTEN)“. Bei 20: „The First to Recover“, Bedrohung −10, Sucht −1, Silvermoon „Growing Hope“ (Legitimität +5), Wretched „Clarity“. Bei 40: „Their Eyes Grow Clear“ mit Waldläufer (−15.000, „Healed Rangers“) oder Arbeiter („Healed Workers“), Sucht −1, Silvermoon „Families Reunited“, Wretched „Longing for Home“. Bei 60: „The Wretched Healed“, alle Etappen-Modifier weg. Nach 3 Monaten Entzug: „Relapse“ mit Notlieferung (−50.000) oder Balken −6.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: „The First to Recover“ (Sucht −1), Arbeiter-Wahl bei 40, Heilung bei 60 fertig. Rückfall nicht getestet. 60 Monate fühlen sich lang an (Balance, später).

### T-073 Eingliedern nach Sucht-Stufe (VA-021)
- **Schritte:** Je ein Spielstand mit Wretched auf Stufe 3 und Stufe 2 (siehe T-071), jeweils „Absorb the Wretched“.
- **Erwartet:** Stufe 3: States 10 J. „Wretched Addicts“, Silvermoon 10 J. „The Wretched Absorbed“ (Legitimität −10). Stufe 2: 6 J. Addicts, 6 J. Absorbed mit −5. Stufe 1: keine Addicts, 5 J. Legitimität −5. Nach etwa 2 Jahren „Plunder of the Mana Stores“ (hart: 1 J. „Mana Stores Guarded“; versorgen: −25.000, ein State verliert Addicts).
- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-11-12, Kono: Stufe 3 (Pakt, gleich eingliedern) OK: 10 J. „The Wretched Absorbed“, −10, +25 % Radikale. Fehler: 2 Monate vor Heil-Ende dasselbe statt Stufe 1. Ursache: Entzugs-Zähler der Wretched lief während der Heilung weiter und hob die Sucht wieder an (Mana fehlte zu Beginn). Fix: in der Heilung kein Anstieg, Zähler auf 0 (`va_silvermoon_wretched_addiction_pulse_effect`). Erneut: heilen bis nach Etappe 40, dann eingliedern → 5 J. „Absorbed (light)“, keine Addicts.

### T-074 Anführer und Kopfgeld (VA-021)
- **Schritte:** Neue Kampagne. Wretched-Charaktere ansehen (Herrscher, Generäle, Agitatoren). Als Silvermoon die drei Kopfgeld-Schalter ansehen, einen drücken, bis Erfolg oder 12 Monate laufen lassen.
- **Erwartet:** Herrscher „Thaelis the Hungerer (AI WRITTEN)“, General „Aldaron the Reckless“, Agitator „Felendren the Banished“. Drei Schalter (WANTED Thaelis −30.000, Aldaron −25.000, Felendren −20.000), nur einer zugleich, gesperrt bei Krieg oder Protektorat. Erfolg: Popup, Anführer tot, Bedrohung −20, ggf. nach 2 Monaten „The Wretched Take Revenge“ (+10). Aldaron: „Harbor Overrun“ endet. Felendren: Wahl Splitter. 12 Monate ohne Erfolg: „The Hunt Has Failed“, Bedrohung +10, Schalter 1 Jahr gesperrt.
- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-11-12, Kono: Thaelis und Aldaron OK (Popup, Tod, Rache-Raub „Enraged by the death …“). Felendren-Schalter fehlte. Ursache vermutlich: Agitator landet im Exil-Pool. Fix: `va_wretched_felendren_alive_trigger` und `va_silvermoon_wretched_slay_felendren_effect` suchen auch im Exil. Felendren erneut testen. Idee Nachricht an die Wretched → VA-071.

### T-075 Führungslos und 20-Jahre-Ablauf (VA-021)
- **Schritte:** Alle drei Anführer per Kopfgeld töten (Konsole/Zeit). Getrennt: JE 20 Jahre ohne Lösung auslaufen lassen.
- **Erwartet:** Nach dem dritten: „The Wretched Fall Apart“, Wretched-Land gehört Silvermoon, Devastation 50 in den ehemaligen Wretched-States, Addicts nach Stufe, keine Legitimitätsstrafe, JE erledigt. Ablauf: 10 J. „Our Own Left Behind“ (Prestige −10 %).
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz: 2026-11-12, offen, braucht Felendren (T-074). 20-Jahre-Ablauf per Zeit ist mühsam, ggf. Konsole.

### T-076 Mana-Aufstand (VA-021)
- **Schritte:** Silvermoon (oder anderes Land mit Mana-Kultur und mindestens 2 States) lange in Mana-Entzug halten, Konsole `set_variable` geht nicht → Mana-Preis hoch lassen. Einmal mit, einmal ohne bestehende Wretched.
- **Erwartet:** Nach 12 Monaten „Hungry in the Streets“ (Notprogramm −50.000 und Zähler −6, oder „Crackdown on the Hungry“ 2 J.). Nach 24 Monaten ohne Wretched: „Rise of the Wretched“, ein Nicht-Hauptstadt-State wird Wretched-Land (Stufe 3), Kriegs-Play zur Annexion; bei Silvermoon startet „The Wretched“ neu. Mit Wretched: „Flight to the Ruins“, Radikale in der Hauptstadt, Bedrohung +30, Wretched-Sucht +1.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-077 error.log: Wretched Schritt 2–4 (Claude)
- **Schritte:** Nach T-071 bis T-076 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `va_wretched_addiction_effects.txt`, `va_silvermoon_wretched_bounty_effects.txt`, `va_mana_uprising_effects.txt`, `va_mana_effects.txt`, `va_wretched_heal_events.txt`, `va_wretched_bounty_events.txt`, `va_mana_uprising_events.txt`, `va_wretched_characters.txt`, `va_eastern_kingdom.txt` (Charaktere), `has_template`, `kill_character`, `create_country`, `dp_annex_war`, `add_devastation`, `va_wretched_*_trigger`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Claude: 48× va_wretched_last_level nicht gesetzt (va_silvermoon_wretched_effects.txt, aus JE-Fehlschlag Eroberung und Nachspiel-Puls). Fix: va_silvermoon_wretched_addicts_aftermath_effect ruft zuerst va_silvermoon_wretched_store_level_effect. Nächstes Log erneut prüfen. Zweites Log 2026-11-12 (Sitzung 2): va_wretched_last_level weg; neu 1582× va_wretched_heal_stage nicht gesetzt (va_wretched_addiction_effects.txt:90/95, aus dem Tooltip von „Begin the Healing“). Fix: has_variable vor var-Vergleich. Nächstes Log erneut prüfen. Drittes Log 2026-11-12 17:16: heal_stage-Zeilen nur noch vom Start vor dem Fix; neu 80× va_wretched_last_level (va_silvermoon_wretched_effects.txt:135, Tooltip des JE-Outcomes „anders untergegangen“). Fix: has_variable vor allen vier Vergleichen, ohne Variable Stufe 3. Nächstes Log erneut prüfen. Abschluss 2026-11-13 (Claude): error.log 22:39 ohne Zeilen zu den gelisteten Wretched-, Mana- und Figuren-Dateien.

## Runde 16 – error.log-Großputz (Stand 2026-11-03)

Ticket: VA-043 (mit VA-003, VA-026, VA-014, VA-007, VA-055). Lint vor Freigabe: 4 neue Fehler, alle Dubletten durch die Alt-Kopien, die Kono noch löschen muss (Liste in VA-043, 2026-11-03). Danach 0.

**Vorher (Kono):** die Dateien aus VA-043 „Von Kono zu löschen“ im Repo und in `mod\warcraft` löschen, `mod\warcraft` aus dem Repo neu befüllen (viele gelöschte Dateien, siehe ABLAUFPLAN „Erledigt“ 2026-11-03).

### T-081 error.log: Großputz (Claude)
- **Schritte:** Nach T-078 bis T-080 und T-082 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `geographic_region_*`, `Invalid database object 'je_*'`, `country_law_manager`, `building_type.cpp` (fehlende Loc alter Gebäude), `modifier_type_definition_database`, `VA_pandaria.txt`, `VA_northrend_state.txt`, `23_north_kalimdor.txt`, `va_outlands.txt` (Pops), `infection_events.txt`, `VA_gilneas_infection.txt`, `Invalid character` in Loc-Keys, `bg_*_WIP`, `00_code_on_actions.txt`/`political_movements`/`flag_definitions` aus dem Mod. Keine `fortification_graphics`-Zeilen (VA-060), kein `Invalid right side during comparison 's'` (`08_monuments`, `10_canals`, `00_power_bloc_names`, `03_pan_national_movements`; Spiel dafür mindestens ein halbes Jahr laufen lassen), kein `Invalid building`, kein `does not have a valid namespace`/`unknown random event`, kein `is orphaned` (außer `french_pretenders.6`), kein `has_template … Invalid database object` (Erde-Vorlagen), keine `Failed to find country` aus `government_types`, keine Zeilen zu `common/achievements/`, `owned_*_region_states`, `iberian_treaty_ports`, `is_afghan_nation`, `company_is_zaibatsu`, keine Zeilen zu `00_spanish_new_world_scripted_effects`, `00_the_grand_collapse_scripted_effects`, `00_victoria_great_game_scripted_effects`, keine Meldung zu doppelt definierten Effekten aus `va_earth_effects.txt`, kein `already has a journal entry of type je_mana_hunger`. Gesamtzahl der Einträge deutlich unter 9.598 (Stand 03.11.).
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

## Runde 17 – Provinz-Terrain Östliche Königreiche (Stand 2026-11-03)

Ticket: VA-051. `map_data/province_terrains.txt` (Regionen 26–28), neu `common/terrain/va_terrain.txt` und `localization/replace/english/va_terrain_l_english.yml`. Lint 26–28: 0 neue Fehler (2026-11-04). Vorher `mod\warcraft` mit dieser Datei aktualisieren. Vergleichsbild (links alt, rechts neu): `.claude/regionen/va_terrain_ek_vorschau.png`.

### T-083 Terrain in EK passt zur Karte (VA-051)
- **Schritte:** Kampagne starten, Kartenmodus „Gelände“ bzw. Provinz-Tooltip in Elwynn, Westfall, Dun Morogh, Sumpfland, Alterac, Gilneas ansehen; 1–2 States mit Farmen anklicken (State-Bild).
- **Erwartet:** Kein Absturz. Keine Tundra/Savanne mehr zufällig verstreut. Elwynn Wald, Dun Morogh Schnee, Sumpfland/Sümpfe des Elends Feuchtgebiet, Westfall Savanne, flache Täler Ebene, Gebirgsränder Gebirge, Ödland/Brennende Steppe Hügel. (2026-11-04 nachgebessert: deutlich mehr Hügel, Schlingendorntal Dschungel.) Farmland siehe T-085.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-084 Eigenes Terrain „Underwater“ in Vashj'ir (VA-051)
- **Schritte:** In Vashj'ir (z. B. Konsole `observe`, dann State Vashj'ir/Abyssal Breach) Provinz-Tooltip und State-Fenster ansehen; eine Armee dorthin schicken.
- **Erwartet:** Terrain heißt „Underwater (AI WRITTEN)“, State-Bild vorerst Feuchtgebiet (Platzhalter). Kein Absturz, Kampf funktioniert (schmale Front). error.log ohne Zeilen zu `va_underwater` oder `va_terrain.txt`.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-085 Farmland, Forst, Bergbau erscheinen in EK (VA-051)
- **Vorher:** `gfx/map/masks/mask_dynamic_farmland.png`, `mask_dynamic_forestry.png`, `mask_dynamic_mining.png` nach `mod\warcraft` kopieren.
- **Schritte:** Kampagne starten, in Elwynn, Westfall, Lordaeron (Tirisfal/Westliche Pestländer), Arathi heranzoomen; 5–10 Jahre laufen lassen bzw. per Konsole Farmen bauen.
- **Erwartet:** Felder (Bodentextur und Höfe/Windmühlen) erscheinen in Ebenen mit Farmen, schwächer in Hügeln, nicht in Gebirge, Schnee, Vashj'ir. Holzfäller zeigen Rodungen v. a. in Elwynn, Dämmerwald, Schlingendorntal; Minen Tagebau in Hügeln/Bergen nahe der Minen-Provinz. Keine Felder/Rodungen/Minen außerhalb von EK (andere Kontinente vorerst ohne). error.log: Warnung `terrain_manipulator.cpp … checksum no longer match` ist harmlos (Liste wird neu gebaut, verschwindet nach Speichern im Map-Editor).
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

## Runde 19 – Patch 1.15 (Stand 2026-11-06)

Ticket: VA-063. Lint alle Regionen: 0 neue Fehler (2026-11-06). Vorher nach `mod\warcraft` kopieren: `common/travel_network/naval_network.txt` (neu), `common/flag_definitions/00_flag_definitions.txt` (neu), neu erzeugt aus Vanilla 1.15: `common/achievements/*.txt`, `common/government_types/01_monarchies.txt`, `01_regencies.txt`, `01_social_monarchies.txt`, `05_council_republics.txt`, `common/political_movements/03_pan_national_movements.txt`, `common/power_bloc_names/00_power_bloc_names.txt`, `common/buildings/08_monuments.txt`, `10_canals.txt`.

### T-092 Flaggen ohne Erde-Abfragen (VA-063)
- **Schritte:** Kampagne starten, ein paar Monate laufen lassen; Flaggen von Stormwind, Silvermoon, Orgrimmar und einem kleinen Land ansehen. Wenn möglich eine Revolution auslösen oder ein Land kommunistisch machen (Konsole) und dessen Flagge ansehen.
- **Erwartet:** Flaggen wie vor dem Patch, Revolutionsflaggen funktionieren weiter. error.log ohne `00_flag_definitions.txt` (vorher 3.888 Zeilen `Invalid right side during comparison 's'`).
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz: 2026-11-06 error.log: 2 Zeilen übrig (Z. 294 `was_formed_from = HER`, Tag ohne `c:`, nur in Liste `AFG`, harmlos), sonst weg. Sichtprüfung der Flaggen steht aus.

### T-093 Marine-Grafik aus Vanilla (VA-063/VA-059)
- **Vorher:** in `mod\warcraft` den Ordner `gfx/map/spline_network/military_route_graphics/` löschen (im Repo gelöscht, alte Kopie von 2023; Vanilla heißt jetzt `route_graphics`).
- **Schritte:** Kampagne starten, Flotte bewegen und eine Armee per Straße/Bahn verlegen; Fahrzeuge auf den Routen ansehen.
- **Erwartet:** Schiffe, Wagen und Züge auf den Routen sichtbar. error.log ohne `03_naval_vehicles.txt` / `combat_unit_type_frigate`.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-095 JEs im neuen outcome-Format und neue Erde-Hüllen (VA-063)
- **Vorher:** nach `mod\warcraft` kopieren: `.metadata/metadata.json` (1.15.*), `common/journal_entries/` (ganzer Ordner: `VA_silvermoon.txt`, `va_dead_scar.txt`, `va_mana.txt`, `va_earth_je_stubs.txt`, neue leere `00_rlit_journal_entries.txt`, `08_*.txt`), `common/scripted_buttons/` (neu leer: `08_tsarpoints_buttons.txt`, `poland_buttons.txt`, `russia_civil_war_buttons.txt`), `common/company_types/00_companies_ip5.txt` (leer), `common/character_templates/` (neu leer: `country_abk/bko/mnl/pol/svn/tki.txt`, `easter egg templates.txt`; `va_earth_template_stubs.txt`), `events/` (neu leer: `rlit_cluster1_golden_age.txt`, `rlit_cluster2_crossroads.txt`, `russia_events/*.txt`; Ordner `va_earth_event_stubs/` komplett ersetzen), `common/geographic_regions/`. Lint alle Regionen: 0 neue Fehler.
- **Schritte:** Neue Kampagne als Silvermoon. Journal öffnen: Mana-Hunger, Deathholme, Zul'Aman, Korridor, Wretched, Todesschneise (nach `research quinine`). Konsole: `kill_country DEATHHOLME` o. ä. bzw. Ziel per Konsole erfüllen und sehen, ob das JE abschließt (Event `silvermoon_events.2`, Modifier). Ein paar Jahre laufen lassen.
- **Erwartet:** Alle JEs sichtbar mit Abschnitt „So erreichst du …“/„Bei Abschluss“ und Zeitlimit, wo vorher eins war. Abschluss löst Event und Modifier aus, abgeschlossene JEs stehen im Reiter „Abgeschlossen“. error.log ohne `Unexpected token: invalid`/`on_invalid`/`complete`, ohne Zeilen zu `va_earth_je_stubs.txt`; Gesamtzahl deutlich unter 4.300.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

## Runde 20 – Todesschneise ganz, Deathholme-Fluch (Stand 2026-11-06)

Ticket: VA-062. Lint 26: 0 neue Fehler. Nach `mod\warcraft` kopieren: `gfx/map/masks/mask_dynamic_mining.png`, `common/journal_entries/va_dead_scar.txt`, `common/scripted_buttons/va_dead_scar_buttons.txt`, `common/scripted_progress_bars/va_dead_scar_progress_bars.txt`, `common/scripted_effects/va_dead_scar_effects.txt`, `common/scripted_effects/va_quel_thalas_effects.txt`, `common/scripted_triggers/va_quel_thalas_triggers.txt`, `common/script_values/va_dead_scar_values.txt` (neu), `common/static_modifiers/va_quel_thalas_modifiers.txt`, `common/on_actions/va_on_actions_quel_thalas.txt`, `common/history/global/va_global_quel_thalas.txt`, `common/building_groups/va_building_groups.txt`, `localization/replace/english/va_dead_scar_regions_l_english.yml`. In `mod\warcraft` löschen: `gui/` (Test-Knopf). Neue Kampagne. Karte zeigt Änderungen erst nach Speichern/Laden.

### T-108 Ley Line Tap: Ausbaustufen (VA-019)
- **Vorher:** `common/buildings/va_mana_buildings.txt`, `common/production_methods/va_mana_production_methods.txt`, `common/production_method_groups/va_mana_production_method_groups.txt`, `localization/replace/english/va_mana_l_english.yml` nach `mod\warcraft`; neue Kampagne als Silvermoon.
- **Schritte:** Ley Line Tap in Sunwell öffnen: zwei Gruppen „Ley Line Focus“ und „Attunement“. Per Konsole `research atmospheric_engine`, `research empiricism`, `research electrical_generation`, dann umschalten und Tooltips lesen.
- **Erwartet:** Start mit Focus Crystals / No Attunement. Nach Forschung lassen sich Arcane Conduits, Runic Resonators und Arcane Sigils wählen; Mana-Ausstoß 12 → 24 → 36 (+6 mit Sigils; Nerf 2026-11-13, vorher 20/40/65/+15), Strom- und Papierbedarf erscheinen. Namen mit „(AI WRITTEN)“, keine Loc-Keys. error.log ohne Zeilen zu den drei Dateien.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-109 Rogue-Provinzen von Nord-Kalimdor-States gelöst (VA-031)
- **Vorher:** `map_data/state_regions/23_va_north_kalimdor.txt`, `common/history/states/VA_kalimdor_states.txt` nach `mod\warcraft`; neue Kampagne.
- **Schritte:** Spiel starten; Haufen im Südmeer ansehen und überfahren; Teldrassil- und Azuremyst-States öffnen (Marker, Bau-Menü Hafen bei Dolanaar); Wandering Isles unverändert?
- **Hubs (Test 2026-11-06):** Dolanaar city/mine/wood → xD950C5/xFA8A80/x2750DE, Gnarlpine Hold city/farm/mine → x3489FE/x7CC77F/x22103F (trockene, passierbare GNARLPINE_FURBOLG-Provinzen auf Teldrassil). Ergebnis Kono: weiterhin Hafen. Zusätzlich Strategieregion Teldrassil `capital_province` → xD950C5.
- **Erwartet:** Kein Absturz. Dolanaar und Gnarlpine Hold ohne Hafen (wie Shadowglen/Oracle Glade). error.log: Meldungen zu übrigen Hubs außerhalb ihres States, unzugeordneten Haufen-Provinzen und EXODAR/Nestlewood (Pops/Gebäude ohne State) sind erwartet; Rest notieren.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-110 Oracle Glade neu geteilt (VA-031)
- **Vorher:** Kono-Vorgabe 2026-11-06: 14 Provinzen im Süden (x3383E0 x8D801C x6703FD x8F553A x6849B4 xE35510 xAE038D x5CF8E8 x098E2F x577F5A, abgerundet mit x3FF213 xABDF84 xEC3DB7 x365308) an DARNASSUS, alle übrigen (auch die impassable) an BLOODFEATHER_HARPY. Pops/Gebäude wie zuvor: kal_dorei, Tee 2, Roggen 2 bei Darnassus; Harpyien, Holz, Roggen (Herrenhaus) bei Bloodfeather.
- **Schritte:** Neue Kampagne, Oracle Glade ansehen (Besitzgrenze, Pops, Gebäude beider Anteile); als Bloodfeather und als Darnassus Bau-Menü nach Hafen prüfen.
- **Erwartet:** Darnassus-Anteil im Süden wie gewünscht, keine fehlenden Provinzen, kein Hafen. error.log ohne neue Zeilen zu STATE_ORACLE_GLADE.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

## Runde 21 – Amani-Reihe V1 (Stand 2026-11-10)

Ticket: VA-022. Lint vor Freigabe: 0 neue Fehler (2026-11-10).

### T-111 Amani-JEs zum Start (VA-022)
- **Vorher:** Neue Kampagne als Zul'Jarra (`AMANI_TRIBE`).
- **Schritte:** Journal öffnen; alle vier JEs lesen (Gather the Tribes, Malacrass and the Loa, The Siege of Zul'Aman, Restore the Amani Empire), Schalter und Balken ansehen, Modifier „Besieged“ im Länder-Tooltip.
- **Erwartet:** Vier JEs mit Texten „(AI WRITTEN)“, keine Loc-Keys im Klartext. Gather the Tribes: Schalter „Summon the Shadowpine“ und „Send Envoys to Zul'Mashar“, Balken Shadowpine Oaths. Loa: vier Ritual-Schalter, Balken Ritual Preparations. error.log ohne Zeilen zu `va_amani*`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: vier JEs sichtbar, Texte ok.

### T-112 Stämme sammeln (VA-022)
- **Vorher:** Spielstand aus T-111.
- **Schritte:** „Summon the Shadowpine“ drücken, Monate laufen lassen (Balken +1/Monat, im Krieg Stillstand mit Tooltip). Nach 24 Monaten: Event „The Shadowpine Come Home“, Shadowpine-States gehören Zul'Jarra. „Send Envoys to Zul'Mashar“: Antwort abwarten (annehmen → Marionette, ablehnen → Anspruch auf Zul'Mashar, Schalter 1 Jahr gesperrt). Zur Abkürzung Mossflayer per Konsole annektieren oder Zul'Mashar erobern.
- **Erwartet:** Mit beiden Stämmen Event „One Banner“, Modifier Tribes United (Prestige +25, 10 J.), JE erfüllt.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Shadowpine eingegliedert, Gesandte → Mossflayer als Marionette, „One Banner“ kam. Zu leicht: Eingliederung gefühlt nach 1 Jahr, viele Gebäude auf einmal → Tribut 50.000, Autorität −50, 36 Monate (va_amani_buttons/_bars/_modifiers). Nachtest T-131.

### T-113 Loa-Rituale (VA-022)
- **Vorher:** Spielstand aus T-111.
- **Schritte:** Ritual Akil'zon starten (−25.000, Modifier Ritual of Malacrass), andere Ritual-Schalter müssen gesperrt sein. 24 Monate laufen lassen → Event „The Shrine of the Eagle“, „Bind“ wählen. Zwei weitere Loa binden.
- **Erwartet:** Nach jedem Ritual Balken wieder 0, Bonus-Modifier dauerhaft, Priester-IG mit Loa Defiled bzw. Loa Honored. Nach der dritten Bindung Event „The Loa Turn Away“ (einmalig). Nach dem vierten Loa Event „The Four Have Answered“, JE erfüllt.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Schalter −100 Autorität und −25.000, Modifier da; Schrein-Event mit Binden/Ehren; KI startet Rituale bei genug Geld und ehrt. Nicht bis zum vierten Loa gespielt („The Loa Turn Away“, „The Four Have Answered“ offen). Vorher: −25 zu billig → −100.

### T-114 Belagerung, Reich, Rache, Schatzjäger (VA-022)
- **Vorher:** Spielstand aus T-112 (Stämme geeint) und T-113 (mind. zwei Loa).
- **Schritte:** Zul'Aman und Tor'Watha halten und ganz Sanctum of Sun einnehmen (Anteile von Shadowpine, Tranquillien und Nachtelfen-Außenposten; Anspruch kommt mit dem JE) → Belagerungs-JE erfüllt. Gegenprobe: nur Shadowpine eingegliedert → Belagerung läuft weiter. Dann prüfen, ob „Restore the Amani Empire“ erfüllt und „Vengeance for Zul'Aman“ mit Ansprüchen auf die Ghostlands erscheint. Schatzjäger: ein paar Jahre unter Isolationismus laufen lassen oder `event amani_treasure_events.1` bis `.3` per Konsole.
- **Erwartet:** Events „The Siege Is Broken“ und „The Amani Empire Rises“, Modifier Besieged weg. Rache-JE mit Ansprüchen auf Tranquillien, Suncrown Village, East Sanctum, Windrunner Village. Schatzjäger-Events mit zwei Optionen, Texte „(AI WRITTEN)“. Gegenprobe: Zul'Aman und Tor'Watha verlieren → Belagerung scheitert, die übrigen Amani-JEs verschwinden.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Siege Is Broken, Amani Empire Rises, Rache-JE mit Tranquillien und Suncrown Village → „The Debt Is Paid“; Schatzjäger 1–3 feuern. Wunsch: Belohnung nur Prestige fühlt sich schwach an, Formable Amani-Reich fehlt (VA-017). Schatzjäger-Autorität 10 → 75. Gegenprobe (Zul'Aman verlieren) nicht getestet.

### T-115 error.log: Amani-Reihe (Claude)
- **Schritte:** Nach T-111 bis T-114 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `va_amani.txt`, `va_amani_buttons.txt`, `va_amani_bars.txt`, `va_amani_effects.txt`, `va_amani_triggers.txt`, `va_amani_modifiers.txt`, `va_on_actions_amani.txt`, `va_amani_events.txt`, `va_amani_loa_events.txt`, `va_amani_treasure_events.txt`, `va_amani_l_english.yml`, `va_global_quel_thalas.txt`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Claude: keine Zeilen zu den Amani-Dateien außer 184× „Scoped object of type country is not valid (Country 4294967295)“ an den visible-Blöcken von va_amani_buttons.txt, nur im Observe-Modus (Oberfläche prüft Schalter ohne Spielerland). Harmlos.

### T-131 Nachtest Zul'Jarra-Balance und Korridor-Abbruch (VA-022, VA-047)
- **Schritte:** (1) Als Zul'Jarra „Summon the Shadowpine“ drücken, Datum notieren. (2) Schatzjäger: `event amani_treasure_events.1`, „Their heads go on the wall“. (3) Tranquillien mit Zul'Jarra erobern (Rache-JE) oder per Konsole an ein fremdes Land geben, einen Monat warten, als Silvermoon (`play SILVERMOON`) ins Journal sehen.
- **Erwartet:** (1) −50.000 sofort, Modifier „Summons to the Shadowpine“ mit Autorität −50, Balken bis 36, Eingliederung erst nach 36 Friedensmonaten (Datum prüfen; falls schneller, Claude Bescheid geben). (2) Modifier „Trespassers Executed“ mit Autorität +75 für 5 Jahre. (3) „The Road to Tranquillien“ ist verschwunden, Logistik-Modifier weg.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-132 Formable Amani-Reich (VA-017)
- **Vorher:** Neue Dateien `common/country_formation/va_formable_countries.txt`, `common/coat_of_arms/coat_of_arms/va_amani_coat_of_arms.txt`; geändert `VA_eastern_kingdom.txt` (Länderdefinition), `va_countries_l_english.yml`, `va_amani_l_english.yml`, `va_amani.txt`.
- **Schritte:** Spielstand nach „The Amani Empire Rises“ (T-114) oder neue Kampagne als Zul'Jarra und `je_amani_empire` per Konsole abschließen. Event-Text lesen. Danach Nation bilden (Formation-Knopf im Länderfenster), vorher Tooltip mit den Bedingungen ansehen. Gegenprobe vor dem Reichs-JE: Formation gesperrt.
- **Erwartet:** Event „The Amani Empire Rises“ nennt die Formation. Formation zeigt sechs States (Zul'Aman, Tor'Watha, Dawnstar Spire, Sanctum of Sun, Suncrown Village, Zul'Mashar), 66 % nötig, Bedingungen „We have restored the Amani Empire“ und „Silvermoon has not broken the Amani …“ (gesperrt nach silvermoon_events.3). Nach dem Bilden heißt das Land „Amani Empire“, Rang Imperium, Wappen mit Zul'jins Maske in Gold auf dunkelgrün. error.log ohne Zeilen zu `va_formable_countries.txt`, `AMANI_EMPIRE`, `va_amani_coat_of_arms.txt`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-13, Kono: vorher gesperrt, nach dem Reichs-JE bildbar, Farbe gefällt, Claims auf die Formation-States. Danach erweitert (Northpass Tower, East Sanctum, Sunsail Anchorage, Duskwither Spire, 5 von 10 nötig), Wappen getauscht (Reich: grün mit Adler-Loa, bisher Zul'Jarra; Zul'Jarra: türkis mit Zul'jins Maske), fehlende Ländernamen Quel'Thalas (SILVERMOON_ADJ im Return-State-Tooltip) ergänzt. Kultur und eigenes Wappen-Emblem später.

### T-133 Eigenes Event-Bild „The Wretched Healed“ (VA-027)
- **Vorher:** Neu `gfx/event_pictures/va_eversong_road_home.dds`; geändert `events/va_wretched_events.txt`.
- **Schritte:** Kampagne als Silvermoon, Konsole `event wretched_events.5`.
- **Erwartet:** Event zeigt die Eversong-Zeichnung (rot-goldene Bäume, Türme von Silvermoon) statt des Paradevideos, nicht verzerrt und nicht schwarz. error.log ohne Zeilen zu `va_eversong_road_home.dds` oder `wretched_events.5`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-13, Kono: Bild gut zu sehen.

### T-134 Mana-Nerf: Ley Line Tap und Bedarf nach Lebensstandard (VA-019)
- **Vorher:** geändert `common/production_methods/va_mana_production_methods.txt`, `common/script_values/va_mana_values.txt`. Neue Kampagne als Silvermoon.
- **Schritte:** Ley Line Tap in Sunwell öffnen (Ausstoß, Belegschaft). Mana-Markt ansehen (Angebot/Nachfrage, Preis). JE „The Mana Hunger“: Stufe zum Start. State-Tooltip „Mana Upkeep“ in Silvermoon City lesen. 5–10 Jahre laufen lassen, Maßnahmen nutzen, Taps ausbauen.
- **Erwartet:** Arcane Conduits 24 Mana je Stufe (Start 2 Stufen = 48), 7.000 Arbeitsplätze je Stufe mit 1.750 Akademikern. Silvermoon startet im Mana-Entzug; mit Rationierung, Fauna-Entzug und Disenchantment wird es erträglicher, aber erst nach mehreren neuen Stufen Knappheit oder stabil. Ley Line Tap nicht mehr das profitabelste Gebäude (Gewinn je Arbeiter etwa Tabakniveau). Mana Upkeep steigt in States mit hohem Lebensstandard. error.log ohne Zeilen zu `va_mana_values.txt`, `standard_of_living`, `va_mana_production_methods.txt`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-13, Kono: Werte sehen sehr gut aus. Claude: error.log 22:39 ohne Zeilen zu va_mana_values.txt, standard_of_living, va_mana_production_methods.txt (if im every_scope_pop wird angenommen).

## Runde 22 – Quel'Thalas: Bevölkerung und Figuren (Stand 2026-11-10)

Tickets: VA-049, VA-024, VA-016, VA-066, VA-021. Lint vor Freigabe: 0 neue Fehler (2026-11-10, `--regions 26`).

### T-120 Figuren-Boni in Silvermoon-JEs (VA-066)
- **Schritte:** Kampagne als Silvermoon. Korridor-Etappe starten und Balken-Tooltip lesen. Wretched-Kopfgeld-Schalter und Heilungs-Schalter lesen. Ritual Site an der Todesschneise starten, Länder-Modifier ansehen. Gegenprobe: Halduron bzw. Liadrin per Konsole töten oder entlassen, Monat abwarten. Deathholme-Abschluss per Konsole `event silvermoon_events.2`.
- **Erwartet:** Korridor-Balken +1,2 je Monat mit Zeile „Halduron Brightwing leads the Farstriders (AI WRITTEN)“, Etappe nach 15 Monaten. Schalter-Texte nennen Halduron (Kopfgeld +10 %) und Rommath (Rückfall erst nach 5 Monaten). Mit Ritual Site und Liadrin Modifier „Blood Knight Wardens (AI WRITTEN)“ mit Bürokratie +10; ohne Liadrin oder ohne Ritual verschwindet er im Folgemonat. Deathholme-Text nennt Dar'Khan, Auriferous und Mavren.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-127 Nachtest Kosten: Loa-Ritual und Korridor (VA-022, VA-047)
- **Schritte:** (1) Als Zul'Jarra ein Loa-Ritual starten: Modifier „Loa Ritual“ zieht laufend −100 Autorität (vorher −25). (2) Als Silvermoon „Launch Logistics Operation“ im Korridor-JE: Bürokratie −50 (vorher −25), Autorität weiter −25.
- **Erwartet:** Werte wie genannt, Kosten spürbar, aber tragbar.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: (2) Korridor OK (Kosten, richtige Provinzen). (1) Loa-Ritual −100 Autorität OK.

### T-129 Horde und Allianz bleiben zusammen (VA-065)
- **Schritte:** Neue Kampagne (z. B. als Silvermoon). Zum Start: Rang von Orgrimmar, Prestige-Tooltip (Modifier „Seat of the Warchief (AI WRITTEN)“ +30), Machtblock-Fenster Horde und Allianz (Leverage je Mitglied), Diplomatie: Verteidigungspakte „Pact of the Horde/Alliance (AI WRITTEN)“. Dann 1–2 Jahre laufen lassen.
- **Erwartet:** Orgrimmar Major Power (rund 70 Prestige), Horde wird nicht aufgelöst. Leverage-Vorteil bei allen Mitgliedern deutlich über 30, Pakte Orgrimmar ↔ Thunder Bluff/Silvermoon/Undercity/Darkspear und Stormwind ↔ Darnassus/Gnomeregan/Ironforge/Exodar mit 20 Jahren Bindung. Nach 1–2 Jahren alle Mitglieder noch drin. error.log ohne Zeilen zu `00_historical_treaties.txt`, `00_power_blocs.txt`, `va_power_bloc_modifiers.txt`, `va_warchief_of_the_horde`, `va_power_blocs_l_english.yml`.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-130 Lor'themar als Regent, Namen für Elven/Magical Lowlands (VA-068, VA-069)
- **Schritte:** Neue Kampagne als Silvermoon. Herrscher und Regierungsform ansehen. Kultur Sin'dorei/Quel'dorei: Sprache und Traditionen ansehen.
- **Erwartet:** Regierungsform „Regency of Quel'Thalas (AI WRITTEN)“, Titel „Regent Lord (AI WRITTEN) Lor'themar Theron“ statt König. Sprache „Elven (AI WRITTEN)“, Tradition „Magical Lowlands“, „Marshland“ mit Namen.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Regent Lord, Land heißt weiter Silvermoon; Elven/Magical Lowlands schon in T-116 bestätigt.

### T-118 error.log: Bevölkerung, Figuren, Mana-Aufstand (Claude)
- **Schritte:** Nach T-116, T-117, T-119 bis T-130 Claude Bescheid geben; wenn möglich auch T-076 (Mana-Aufstand) erneut.
- **Erwartet:** Keine Zeilen zu `va_mana_buildings.txt`, `26_north_eastern_kingdoms.txt` (Gebäude), `va_north_eastern_kingdoms.txt` (Pops), `va_quel_thalas_characters.txt`, `va_eastern_kingdom.txt` (außer bekanntem Murloc „Deeb“), `va_quel_thalas_characters_l_english.yml`, `va_quel_thalas_character_triggers.txt`, `va_quel_thalas_character_effects.txt`, `va_silvermoon_corridor_bars.txt`, `va_silvermoon_wretched_bounty_effects.txt`, `va_wretched_addiction_effects.txt`, `va_dead_scar.txt`, `va_silvermoon_modifiers.txt`, `va_eastern_kingdom_countries.txt` (Techs Deathholme/Grimscale), `va_mana_values.txt`, `va_mana_effects.txt`, `va_mana_relief_effects.txt`, `va_mana_buttons.txt`, `va_mana_modifiers.txt`, `va_mana.txt`, `va_mana_upkeep`, `state_buy_orders_mana_add`, `va_mana_uprising_effects.txt`, `va_silvermoon_wretched_effects.txt` (`va_wretched_last_level`, Fix 2026-11-12; `va_silvermoon_wretched_frenzy_effect`, `dp_conquer_state`), `va_silvermoon_wretched_triggers.txt`, `wretched_events.17`, `va_wretched_frenzy_1–3` (vorher: `Unexpected token: handle_annexation_as_civil_war`, behoben 2026-11-10).
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: Zwischenstand 2026-11-12 (Claude): keine Zeilen zu den gelisteten Dateien. Abschluss 2026-11-13 (Claude): error.log 22:39 ohne Zeilen zu den gelisteten Wretched-, Mana- und Figuren-Dateien.
