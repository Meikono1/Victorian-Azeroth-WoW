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

## Runde 1 – Nord-EK, Quel'Danas, Zul'Jarra, Mana (Stand 2026-10-30)

Tickets: VA-015, VA-006, VA-019. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Zum Testen am besten als **Silvermoon** spielen.

### T-001 Kampagne lädt

- **Schritte:** Neue Kampagne starten (Land egal), bis die Karte steht. 2–3 Monate laufen lassen.

- **Erwartet:** Kein Absturz, kein Einfrieren.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30 einige Monate gelaufen, „sieht ganz okay aus“. Folgearbeit Pops/Gebäude/Startwerte → VA-024.

### T-002 error.log (Claude)

- **Schritte:** Nach T-001 Spiel beenden, Claude Bescheid geben. Claude prüft mit `python -I .claude/tools/va_errlog.py --filter …` auf: `26_va_north_eastern_kingdoms`, `VA_eastern_kingdoms_states`, `va_north_eastern_kingdoms`, `VA_eastern_kingdom.txt`, `va_eastern_kingdom_countries`, `va_goods`, `va_mana`, `va_building_groups`, `leyline`, `mana`, `va_countries_l_english`. Außerdem `python -I .claude/tools/va_check_states.py 26`.

- **Erwartet:** Keine Fehler aus diesen Dateien. Die Hub-Fehler für Gilneas City, The Headlands, Seradane, Scholomance, Northgate Woods und Tyr's Hand sind weg.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30 (Runde 3, vollständiges Log): keine Fehler aus den Prüfdateien außer fehlendem BOM (bekannte Altlast, VA-023), keine Hub-Fehler mehr. Erster Versuch: nur teilweise auswertbar. Log-Spam aus Vanilla-Scripts (reale Regionen, ~13.000 Einträge in 8 s) hat die Ladefehler wegrotiert (→ VA-025). Im erhaltenen Teil keine Fehler aus den Prüfdateien; einziger Mod-Bezug: doppeltes `building_company_basic_fishing` in Archerus (→ VA-024). `va_check_states.py 26`: Hubs nur noch bei STATE_TEST (VA-018). Wiederholen nach VA-025.

### T-003 Stadt- und Hafenmarker sitzen sinnvoll

- **Schritte:** Auf der Karte heranzoomen bei Gilneas City, The Headlands, Scholomance, Northgate Woods (Hafen) und Seradane.

- **Erwartet:** Stadt, Farm, Mine, Holz und Hafen stehen jeweils im eigenen State, nicht im Wasser oder Gebirge. Northgate Woods hat einen Hafen an der Küste.

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: noch grafische Fehler, wird später genauer angesehen. Hängt mit fehlenden impassable-Bergprovinzen zusammen (VA-037). Offen.

### T-004 Seradane und Scholomance

- **Schritte:** Kartenmodus „States“ bzw. Mausover auf die Region zwischen Scholomance und Seradane (Hinterland).

- **Erwartet:** Seradane umfasst das Gebiet des Emerald-Entrance-Landes und der Revantusk. Scholomance (Cult of the Damned) ist kleiner und **keine** Küstenregion mehr.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: Scholomance ist keine Küste mehr.

### T-005 West Sanctum geteilt

- **Schritte:** State West Sanctum anklicken.

- **Erwartet:** Zwei Teilstaaten, Silvermoon und Grimscale-Murlocs. Keine Provinz flackert oder gehört beiden.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: geteilt in Elfen und Murlocs.

### T-006 Quel'Danas gehört Silvermoon

- **Schritte:** Sun's Reach, Magisters' Terrace und Sunwell Plateau anklicken.

- **Erwartet:** Besitzer Silvermoon, Bevölkerung Sin'dorei. Magisters' Terrace zeigt Gebirge/unpassierbare Provinzen, Sun's Reach nicht.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: stimmt. Bevölkerung noch Platzhalter (je 10.000 Sin'dorei in Sun's Reach, Magisters' Terrace, Sunwell Plateau) → VA-024.

### T-007 Hauptstädte

- **Schritte:** Länderansicht bzw. Karte für die vier Länder öffnen.

- **Erwartet:** Wildhammer → Aerie Peak, Wretched → Ruins of Silvermoon, Frostwolf Highlands → Tarren Mill, Shadowpine → Dawnstar Spire. Keine Hauptstadt liegt außerhalb des eigenen Gebiets.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono.

### T-008 Tranquillien

- **Schritte:** Tranquillien in der Länderauswahl bzw. Länderansicht öffnen, Reiter „Politik/Gesetze“.

- **Erwartet:** Gesetze wie bei Silvermoon gesetzt (u. a. Protektionismus, Pachtbauern, Sklaverei verboten), keine leeren oder ungültigen Gesetze.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono.

### T-009 Zul'Jarra

- **Schritte:** Zul'Aman auf der Karte anklicken.

- **Erwartet:** Das Land heißt „Zul'Jarra“ (Adjektiv „Zul'Jarran“), kein roher Key `AMANI_TRIBE`.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono.

### T-010 Ressourcen im neuen Format

- **Schritte:** State Sunwell Plateau, Silvermoon City und Koroth Den öffnen, Bereich „Ressourcen/Potenziale“.

- **Erwartet:** Ressourcen werden angezeigt (z. B. Eisen, Kohle, Holz, Fischerei, Farmen). Sunwell Plateau zeigt „Ley Line Tap“ mit 40, Silvermoon City mit 20.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono. Gebäudebild noch Kohlemine (Platzhalter, in VA-027 gelistet).

### T-011 Leylinien-Gebäude baubar

- **Schritte:** Als Silvermoon in Silvermoon City „Ley Line Tap“ bauen. Nach Fertigstellung das Gebäude öffnen.

- **Erwartet:** Baubar ohne Technologie. Produktionsmethode „Focus Crystals“, Verbrauch Werkzeug, Produktion Mana, Arbeiter und Akademiker als Belegschaft. Texte ohne rohe Keys. Icons sind Platzhalter (Kohlemine/Strom), das ist gewollt.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: baubar, produziert Mana. Mana noch mit Strom-Icon (Platzhalter, VA-027).

### T-012 Mana am Markt

- **Schritte:** Marktansicht von Silvermoon öffnen, Gut „Mana“ suchen.

- **Erwartet:** Gut „Mana“ ist vorhanden, Angebot steigt nach T-011. Preis am Minimum ist **erwartet**, denn es gibt noch keine Abnehmer (VA-019).

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono.

---

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

### T-023 error.log: Firmen und Charaktervorlagen (Claude)

- **Schritte:** Nach T-021/T-022 Claude Bescheid geben.

- **Erwartet:** Keine Fehler aus `common/character_templates/` (insbesondere kein doppeltes `default`), keine aus `common/company_types/` außer bekannten Gebäudenamen aus den alten Gebäudekopien (VA-003). Vanilla-Vorlagen für Kolonialgouverneure (`colonial_governor_templates.txt`) laden ohne Fehler.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, 7 Jahre gelaufen, Log ab Ladebeginn vollständig (14.051 Einträge). Keine Fehler aus `common/character_templates/`, kein doppeltes `default`. `99_basic_companies.txt` 27× `is_building_type` (erwartet: Vanilla-Datei lädt, alte Kopie noch nicht zurückgeholt, VA-003). Bekannt und unverändert: `has_template` auf Erde-Vorlagen aus Vanilla-Scripts (~450, waren vorher schon fehlende Vorlagen) und `is_company_type` in `00_company_charter_types.txt`. Beim Lauf aufgefallen: weltweite Hungersnot → VA-029.

---

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

## Runde 9 – Mana als Obsession der Elfen (Stand 2026-10-30)

Ticket: VA-019. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Zum Testen am besten als **Silvermoon** spielen.

### T-040 Mana-Nachfrage durch Elfen (VA-019)

- **Schritte:** Kampagne starten als Silvermoon. Kulturfenster `Sin'dorei` und `Quel'dorei` öffnen (Obsessionen). Marktfenster Silvermoon → Mana: Angebot, Nachfrage, Preis. Ein Pop der Blutelfen öffnen → Bedürfnis „Intoxicants“. Zum Vergleich Marktfenster Stormwind → Liquor/Tobacco. 1 Jahr laufen lassen, Mana-Preis erneut ansehen.

- **Erwartet:** Beide Elfenkulturen haben die Obsession Mana. Mana hat im Silvermoon-Markt Pop-Nachfrage, der Preis liegt nicht mehr am Minimum. Im Bedürfnis Intoxicants steht Mana **zusätzlich** zu Liquor, Tobacco, Opium und Wine (wichtig: `INJECT` darf die Vanilla-Einträge nicht ersetzen; in Stormwind wird weiter Liquor/Tobacco konsumiert). Andere Kulturen kaufen Mana höchstens in kleinen Mengen.

- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-10-30, Kono: andere Rauschmittel gehen weiter, Mana erscheint mit 1.3. Effekt aber zu schwach. KI baut Ley Line Taps selbstständig. → Mana aus Intoxicants raus und nur noch in Stimulants (Kono: kein Rauschmittel), T-042.

### T-041 error.log: Mana-Obsession (Claude)

- **Schritte:** Nach T-040 Claude Bescheid geben.

- **Erwartet:** Keine Zeilen zu `common/pop_needs/va_pop_needs.txt`, `va_goods.txt`, `obsessions` in `va_elfen_cultures.txt` oder „unknown goods mana“.

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-042 Mana-Nachfrage verstärkt (VA-019)

- **Schritte:** Wie T-040: Kampagne als Silvermoon, Marktfenster Mana (Nachfrage, Preis), Blutelfen-Pop → Bedürfnisse Intoxicants und Stimulants. Marktfenster Stormwind → Mana, Tea, Tobacco. 2 Jahre laufen lassen, Mana-Preis und Zahl der Ley Line Taps in Silvermoon ansehen.

- **Erwartet:** Mana steht nur noch in Stimulants (neben Sugar, Tea, Coffee, Tobacco), nicht mehr in Intoxicants. Mana-Nachfrage in Silvermoon deutlich höher als in T-040, Preis über Grundpreis (40) oder zumindest klar über dem Minimum. Nebenwirkung: Auch Menschen u. a. kaufen spürbar Mana (Gewicht wie Tobacco). Kono notiert, ob das zu viel ist; dann sinkt das Grundgewicht wieder und die Elfen bekommen einen eigenen Hebel (Baustein 2).

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz: 2026-10-30, Kono (Stand weight 0.8/min 0, dann auf 0.65/0.1 geändert): Stormwind 15 Mio. Einwohner, Mana-Bedarf 11; Silvermoon 5,1 Mio., Bedarf 11; beide Märkte ohne Mana-Angebot. Nachfrage passt, Angebot fehlt → Start-Ley-Line-Tap (T-043). Nebenbefund Test-Icon im Schiffsbau → VA-045.

### T-043 Mana-Angebot zum Start (VA-019)

- **Schritte:** Kampagne als Silvermoon. Staatenfenster Sunwell Plateau ansehen. Marktfenster Silvermoon → Mana (Angebot, Nachfrage, Preis). Marktfenster Stormwind → Mana. 1 Jahr laufen lassen, erneut ansehen.

- **Erwartet:** Sunwell Plateau hat 1 Stufe Ley Line Tap (Silvermoon, PM Focus Crystals), voll besetzt (10.000 Sin'dorei im State, Bedarf 4.000 Arbeiter + 500 Akademiker). Silvermoon-Markt bietet ab Start bis zu 20 Mana an; die Nachfrage (Werte 0.65/0.1) liegt dort jetzt höher als 11, weil Angebot da ist. Überschuss geht über die Handelszentrale in andere Märkte, Stormwind importiert ggf. Mana. Preis nicht am Minimum.

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-044 Todesschneise (VA-019)

- **Schritte:** Kampagne als Silvermoon. Staatenfenster von Sunwell Plateau, Ruins of Silvermoon, West Sanctum, East Sanctum, Tranquillien und Deathholme öffnen (Modifier-Liste), Tooltip lesen. Zum Vergleich Silvermoon City, Sanctum of the Sun und Farstrider Retreat. Wo Ackerbau steht: Durchsatz ansehen.

- **Erwartet:** Die sechs States tragen „The Dead Scar“ (Platzhalter-Icon Feuer): Ackerbau-Durchsatz −30 %, Infrastruktur −15 %, Baugeschwindigkeit −15 %. Zusätzlich „Shadow of the Dead Scar“ (Sterblichkeit +10 %, Migrationssog −50 %) **nur** dort, wo Lebende die Mehrheit stellen: Sunwell Plateau, Ruins of Silvermoon, West Sanctum, Silvermoons Teile von East Sanctum und Tranquillien, Tranquilliens Teil. **Nicht** in Deathholmes Teilen (Banshees). Andere States ohne Modifier. Wird der Zweitmodifier zum Start nicht gesetzt, aber nach einem Jahr schon, läuft nur die On-Action (dann Startaufruf prüfen). Kono notiert, ob die Auswahl der States und die Stärke passen.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: Untote Bereiche ohne Lebenden-Malus, Elfen-Bereiche mit. Effekte greifen gut. Infrastruktur auf −30 % erhöht (nur Wert, kein neuer Test nötig).

### T-045 error.log: Mana-Angebot, Todesschneise (Claude)

- **Schritte:** Nach T-043 und T-044 Claude Bescheid geben.

- **Erwartet:** Keine Zeilen zu `building_leyline_tap` aus `history/buildings/26_*`, zu `va_dead_scar`, `va_quel_thalas_modifiers.txt`, `history/global/va_global_quel_thalas.txt` `va_quel_thalas_l_english.yml`, `va_undead_triggers.txt`, `va_undead_values.txt` (`total_size`, `this = cu:`), `va_quel_thalas_effects.txt`, `va_on_actions_quel_thalas.txt` oder `culture_percent_state`.

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-046 Todesschneise bei Eroberung (VA-019)

- **Schritte:** Kampagne als Silvermoon. Zum Start die sechs Schneisen-States wie in T-044 ansehen (beide Modifier wie vorher). Dann per Konsole oder Krieg einen Deathholme-Teil übernehmen, z. B. Deathholmes Teil von Tranquillien oder East Sanctum (`annex DEATHHOLME` oder Friedensvertrag). Direkt danach und nach 1 Monat den State ansehen.

- **Erwartet:** Zum Start unverändert: „The Dead Scar“ auf allen sechs States, „Shadow of the Dead Scar“ nur bei Elfen-Mehrheit. Nach der Übernahme steht „The Dead Scar“ weiter auf dem State (auch wenn er mit dem Silvermoon-Teil verschmilzt). „Shadow of the Dead Scar“ passt sich sofort bzw. spätestens nach einem Monat an die neue Mehrheit an, nicht erst nach einem Jahr.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: Anpassung nach Übernahme nahezu sofort.

### T-047 Mana-Hunger als Journal Entry (VA-019)

- **Schritte:** Kampagne als Silvermoon. **Sofort zum Start** das Journal öffnen (Innere Angelegenheiten), danach die Länder-Modifier. Dasselbe kurz für Tranquillien und Wretched (Länderfenster → Journal bzw. Modifier). Zum Vergleich Stormwind. Dann per Konsole oder Abriss den Ley Line Tap auf Sunwell Plateau entfernen bzw. Mana-Preis steigen lassen und 1–2 Monate warten.

- **Erwartet:** „The Mana Hunger (AI WRITTEN)“ ist ab Tag 1 aktiv und angeheftet, die Beschreibung erklärt die drei Stufen mit Preisgrenzen. Die Statuszeile zeigt die aktuelle Stufe (grün Arcane Abundance, neutral Stable, rot Scarcity/Withdrawal) und passt zum Länder-Modifier. Stufen: ≤ 40 Arcane Abundance (Forschung +10 %, Lebensstandard +1), 41–49 keine, ≥ 50 Mana Scarcity (Lebensstandard −1, Radikale/Loyale aus Lebensstandard +10 %), ≥ 68 Mana Withdrawal (Lebensstandard −2, Radikale/Loyale +25 %, Sterblichkeit +5 %, Durchsatz −10 %). Wechsel spätestens einen Monat nach Preisänderung. Stormwind hat weder JE noch Modifier.

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz: 2026-10-30, Kono (Screenshot Highvale): JE aktiv, Status „Mana Withdrawal“ mit passenden Werten. Bedingungen zeigten „culture_this_equal has no localization“ → per `custom_tooltip` behoben, beim nächsten Start Tooltip erneut ansehen. `HIGHVALE_HIGHELFES_ADJ` ohne Loc → VA-006.

### T-048 error.log: Mana-Abhängigkeit (Claude)

- **Schritte:** Nach T-047 Claude Bescheid geben.

- **Erwartet:** Keine Zeilen zu `va_mana_modifiers.txt`, `va_mana_triggers.txt`, `va_mana_effects.txt`, `journal_entries/va_mana.txt`, `je_mana_hunger`, `add_journal_entry`, `market_goods_pricier`, `market_capital` oder `mg:mana`.

- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

## Runde 10 – Silvermoon-Ziele (Stand 2026-10-30)

Ticket: VA-020. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Als **Silvermoon** spielen.

### T-049 Silvermoon-JEs zum Start (VA-020)
- **Schritte:** Kampagne als Silvermoon. Journal → Historischer Inhalt öffnen. Danach Karte: Ansprüche auf Deathholme, Windrunner Village, Tranquillien, East Sanctum, Suncrown Village, Zul'Aman, Tor Watha.
- **Erwartet:** Drei JEs aktiv und angeheftet: „Drive Out Deathholme“ (Ziel: Deathholme existiert nicht, Ablauf 15 Jahre), „Raze Zul'Aman“ (Ziel: Zul'Aman und Tor Watha vollständig besitzen, Ablauf 20 Jahre), das Heil-JE prüft jetzt T-053. Alle Texte enden mit „(AI WRITTEN)“. Ansprüche auf den sieben States vorhanden.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-050 Heilritual der Todesschneise (VA-020) – entfällt, ersetzt durch T-053/T-054 (VA-046)
- **Schritte:** Knopf „Fund a Healing Ritual“ drücken (kostet 25.000, Gold muss reichen). Tooltip des Knopfs vorher ansehen. 24 Monate laufen lassen (Konsole `tick` oder schnell vorspulen). Optional: Mana-Preis in „Mana Withdrawal“ treiben und prüfen, dass das Ritual ruht.
- **Erwartet:** Knopf zeigt Bedingungen lesbar (kein Ritual aktiv, eigener State auf der Schneise, Gold). Danach Status „A healing ritual is underway“, im Mana-Entzug „The ritual has stalled …“. Nach 24 Monaten Popup „The Scar Recedes“ mit State-Namen; der genannte State verliert „The Dead Scar“ und „Shadow of the Dead Scar“, Fortschritt 1/6, Knopf wieder nutzbar.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-051 Deathholme und Zul'Aman abschließen (VA-020)
- **Schritte:** Konsole: `annex DEATHHOLME`, 1 Tag warten. Dann `annex AMANI_TRIBE` (Zul'Aman und Tor Watha), 1 Tag warten. Modifier-Liste von Silvermoon ansehen.
- **Erwartet:** Popup „Deathholme Falls“, Modifier „The Ghostlands Avenged“ (Prestige +25, 10 Jahre). Popup „Zul'Aman Taken“, Modifier „The Amani Broken“ (Prestige +25, 10 Jahre). Beide JEs abgeschlossen.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-052 error.log: Silvermoon-Ziele (Claude)
- **Schritte:** Nach T-049 bis T-051 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `VA_silvermoon.txt`, `va_silvermoon_buttons.txt`, `va_silvermoon_events.txt`, `va_silvermoon_modifiers.txt`, `va_silvermoon_values.txt`, `va_quel_thalas_triggers.txt`, `va_quel_thalas_effects.txt`, `va_silvermoon_l_english.yml`.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

## Runde 11 – Todesschneise heilen (Stand 2026-10-30)

Ticket: VA-046. Lint vor Freigabe: 0 neue Fehler (2026-10-30).

### T-053 Heil-JE für alle Besitzer (VA-046)
- **Schritte:** Kampagne als Silvermoon. Journal → Innere Angelegenheiten. Dann per Länderwechsel (Konsole `play DEATHHOLME`, `play WRETCHED_BLOODELFES`, `play TRANQUILLIEN`) dort ebenfalls ins Journal sehen.
- **Erwartet:** „Heal the Dead Scar (AI WRITTEN)“ aktiv bei allen Ländern mit State auf der Schneise (Silvermoon, Deathholme, Tranquillien, Wretched u. a.), sechs Balken mit Regionsnamen (0/20), Schalter „Begin Healing: …“ nur für Regionen, in denen das Land einen verdorbenen State hat. Beschreibung erklärt Kosten und 20 Monate. Länder ohne Schneisen-State (z. B. Stormwind) haben das JE nicht.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: Kono 2026-10-31: Heilen mit Teilbesitz klappt, nach Eroberung erscheinen die Schalter.

### T-054 Ritual an, aus, fertig (VA-046)
- **Schritte:** Als Silvermoon „Start Ritual: Sunwell Plateau“ drücken. State Sunwell Plateau → Gebäude ansehen, Haushalt (Ausgaben), Bürokratie, Mana-Markt. 3 Monate laufen lassen, dann „Stop Ritual“ drücken, 2 Monate warten, wieder einschalten. Danach bis 20 Monate vorspulen.
- **Erwartet:** Beim Einschalten sinkt die Staatskasse sofort um 100.000 (auch beim Wiedereinschalten). Danach steht eine „Ritual Site“ (staatlich, nicht erweiterbar) mit Clerks/Academics, Bürokratie sinkt um bis zu 25, Mana-Nachfrage +15, Papier-Nachfrage +10, Lohnkosten im Haushalt. Schalter-Tooltip und JE-Text nennen die Kosten. Status „Healing rituals are underway“. Balken +1 je Monat, beim Abschalten verschwindet das Gebäude und der Balken bleibt stehen. Im Mana-Entzug steht der Balken still (Status „stalled“). Bei 20: Popup „The Scar Recedes“ mit State-Namen, Ritual Site weg, „The Dead Scar“ und „Shadow of the Dead Scar“ verschwinden, der Schalter für die Region ist weg.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz: Kono 2026-10-31: Heilen klappt grundsätzlich; Kosten werden nachgeschärft, danach erneut testen.

### T-059 Heil-JE erst mit Quinine, Balken laufen (VA-046)
- **Schritte:** Neue Kampagne als Silvermoon. Prüfen, ob Quinine schon erforscht ist (Technologie-Baum, Gesellschaft Ära 2). Falls nicht: Journal ansehen, dann per Konsole `research quinine`, 1–2 Monate laufen lassen. Ein Ritual starten, 3 Monate vorspulen.
- **Erwartet:** Ohne Quinine ist „Curing the Path of Destruction“ nicht aktiv (höchstens als mögliches JE mit Quinine-Bedingung im Tooltip); spätestens einen Monat nach der Forschung wird es aktiv. Balken heißen nur noch nach der Region. Fehlt der Ritual Site Mana oder Papier (z. B. als Deathholme ohne Mana im Markt): Status „Stalled: … lacks Mana or Paper“, Balken-Tooltip ebenso, Balken steht. Mit voller Versorgung läuft er, auch ohne Mana-Abhängigkeit. Tooltip „Will become invalid if“ zeigt nur „We no longer hold any land on the Dead Scar“. Tooltip von „Stop Ritual“ ohne `BUG:`-Text. Balken der Region steigt jeden Monat um 1. Kein Eintrag `already has a journal entry of type je_va_dead_scar` im error.log.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: Kono 2026-11-01: Test erfolgreich.

### T-055 error.log: Todesschneise heilen (Claude)
- **Schritte:** Nach T-053 und T-054 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `va_dead_scar.txt`, `va_dead_scar_progress_bars.txt`, `va_dead_scar_buttons.txt`, `va_dead_scar_effects.txt`, `va_dead_scar_buildings.txt`, `va_dead_scar_production_method*.txt`, `va_dead_scar_events.txt`, `va_building_groups.txt`, `scope:journal_entry`, `scripted_bar_progress`, `create_building`, `remove_building`.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

## Runde 12 – Korridor nach Tranquillien (Stand 2026-10-31)

Ticket: VA-047. Lint vor Freigabe: 0 neue Fehler (2026-10-31).

### T-056 Korridor-JE und Marktzugang vorher (VA-047)
- **Schritte:** Kampagne als Silvermoon. Journal → Historische Inhalte. Dann Markt-Ansicht bzw. State Tranquillien (Tranquilliens Teil) → Marktzugang notieren.
- **Erwartet:** „The Road to Tranquillien (AI WRITTEN)“ aktiv, ein Balken „Logistics Operation“ 0/18, Schalter „Launch Logistics Operation“, Status „No operation is underway“. Beschreibung nennt Kosten, 18 Monate, Krieg als Alternative. Marktzugang Tranquillien notieren (Vergleich in T-057).
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-057 Drei Etappen per Logistik (VA-047)
- **Schritte:** Schalter drücken. Haushalt (−100.000), Bürokratie und Autorität prüfen. 18 Monate vorspulen, Karte der Geisterlande ansehen. Zweimal wiederholen. Einmal während einer Operation einen Krieg haben (oder per Konsole erklären) und Balken beobachten.
- **Erwartet:** Modifier „Logistics Operation“ (−25/−25), Schalter verschwindet solange. Balken +1/Monat, steht im Krieg (Status „stalls“). Bei 18: Popup „A Stretch of Road Secured“, Provinzen wechseln von Deathholme zu Silvermoon (Etappe 1: xFDDA71, x186841; Etappe 2: Bergprovinzen xCEF332, x2FC0FD; Etappe 3: xD536B6 bis an Tranquillien), die Provinzen der Todesschneisen-Grafik bleiben bei Deathholme, Balken wieder 0. Nach Etappe 3 Popup „The Road Is Open“, JE erfüllt, Modifier „The Road to Tranquillien“. Pops und Gebäude in den neuen Teil-States plausibel (nicht verdoppelt, nicht verschwunden). Marktzugang Tranquillien besser als in T-056.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-058 error.log: Korridor (Claude)
- **Schritte:** Nach T-056 und T-057 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `va_silvermoon_corridor_*.txt`, `VA_silvermoon.txt`, `va_silvermoon_events.txt`, `va_silvermoon_modifiers.txt`, `va_global_quel_thalas.txt`, `set_owner_of_provinces`, `p:x`, `cd:DEATHHOLME`, `va_corridor_stage`.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

## Runde 13 – Wretched (Stand 2026-11-03)

Ticket: VA-021. Lint vor Freigabe: 0 neue Fehler (2026-11-01, Schritt 1: 2026-11-03). T-060 bis T-062 prüfen die Grundfassung, T-064 bis T-067 Schritt 1 (Bedrohung, Raub-Events, Bruderkrieg).

### T-060 Wretched-JE und Mana-Pakt (VA-021)
- **Schritte:** Neue Kampagne als Silvermoon. Journal → Historische Inhalte. Per Konsole `play WRETCHED_BLOODELFES` kurz die Modifier der Wretched ansehen, zurück zu Silvermoon. Schalter „Offer a Mana Pact“ drücken. Danach einmal mit `play WRETCHED_BLOODELFES` vor dem Drücken testen, dass das Pakt-Event dort mit zwei Optionen erscheint (oder die KI entscheiden lassen).
- **Erwartet:** „The Wretched (AI WRITTEN)“ aktiv, Balken „Healing the Wretched“ 0/60, nur der Schalter „Offer a Mana Pact“ sichtbar, Status „still go their own way“. Wretched haben „Wretched Addiction“. Nach dem Drücken: bei Annahme Popup „The Wretched Accept“, Wretched sind Protektorat von Silvermoon, Status „under our protection“, statt des Pakt-Schalters „Absorb the Wretched“ und „Begin the Healing“. Bei Ablehnung Popup „The Wretched Refuse“, Schalter für ein Jahr gesperrt (Tooltip „not offered a pact in the last year“).
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03, Kono: Pakt, Protektorat und Jahressperre funktionieren.

### T-061 Weg 1: Eingliedern (VA-021)
- **Schritte:** Spielstand nach T-060 (Wretched sind Protektorat) sichern. „Absorb the Wretched“ drücken, einen Monat laufen lassen. Karte, Modifier von Silvermoon und States Sunstrider Isle, Ruins of Silvermoon, Sunsail Anchorage ansehen.
- **Erwartet:** Popup „The Wretched Absorbed“, Wretched verschwinden, ihre States gehören Silvermoon (eingegliedert, nicht „unincorporated“). Silvermoon hat „The Wretched Absorbed“ (10 Jahre, Legitimität −10, Radikale aus Bewegungen +25 %). Die drei States haben „Wretched Addicts“ (10 Jahre). JE erledigt.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-062 Weg 2: Heilen (VA-021)
- **Schritte:** Gesicherten Stand aus T-061 laden. „Begin the Healing“ drücken. Staatskasse, Bürokratie, Mana-Preis im Markt der Wretched ansehen. 3 Monate laufen lassen. Mana knapp machen oder abwarten, ob der Balken stillsteht; dann bis 60 vorspulen (Konsole oder lange laufen lassen).
- **Erwartet:** Sofort −100.000, Modifier „Healing the Wretched“ (Bürokratie −25), danach jeden Monat −10.000. Balken +1/Monat; im Krieg oder bei Mana-Knappheit im Markt der Wretched Stillstand mit Status- und Balken-Text. Schalter „Begin the Healing“ verschwindet, „Absorb“ bleibt. Bei 60: Popup „The Wretched Healed“, Annexion, Modifier „The Wretched Restored“ (Prestige +25), **keine** „Wretched Addicts“, kein „Absorbed“. JE erledigt.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-063 error.log: Wretched (Claude)
- **Schritte:** Nach T-060 bis T-062 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `va_silvermoon_wretched_*.txt`, `va_wretched_modifiers.txt`, `va_wretched_events.txt`, `VA_silvermoon.txt`, `va_global_quel_thalas.txt`, `va_wretched_suitor`, `annex_with_incorporation`, `WRETCHED_BLOODELFES`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03, Claude: error.log (20:28) ohne Zeilen zu Wretched-Dateien.

### T-064 Bedrohung und Ansprüche (VA-021, Schritt 1)
- **Schritte:** Neue Kampagne als Silvermoon. JE „The Wretched“ öffnen, Balken ansehen. Diplomatie/Karte: Ansprüche auf Ruins of Silvermoon, Sunsail Anchorage, Sunstrider Isle. 3 Monate laufen lassen und den Tooltip des Balkens „Wretched Threat“ ansehen.
- **Erwartet:** Zwei Balken: „Wretched Threat“ (rot, Start 40/100) und „Healing the Wretched“ (0/60). Silvermoon hat Ansprüche auf die drei Wretched-State-Regionen. Bedrohung steigt um 1 je Monat, solange Mana im Markt der Wretched knapp ist (Tooltip „The Wretched are free and starving for Mana“); sonst bleibt sie stehen. JE-Text erwähnt Bedrohung und Ansprüche.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-065 Raub-Events .10–.15 (VA-021, Schritt 1)
- **Schritte:** Als Silvermoon per Konsole nacheinander `event wretched_events.10` bis `wretched_events.15` auslösen, jeweils beide Optionen ansehen (Tooltips) und je eine wählen. Danach Bedrohung über 50 bringen (Konsole oder abwarten) und einige Jahre laufen lassen.
- **Erwartet:** Alle sechs Events mit Text und zwei Optionen. Bedrohungs-Tooltips („Wretched Threat −10“ usw.) ändern den Balken. .10 b: Modifier „Unsafe Road“ auf Silvermoons Teil von Sunstrider Isle. .11 b: Hinweis „may turn up again“, in der Hälfte der Fälle nach 6 Monaten .14. .12 a: Intelligenzija hat „Apprentices Disciplined“. .13: „Harbor Overrun“ auf Silvermoons Teil von Sunsail (2 bzw. 5 Jahre), danach kein zweites .13, solange er läuft. .14: „Breach in the Wall“ in der Hauptstadt. .15 b: Radikale unter Akademikern. Im Lauf: ab Bedrohung 50 höchstens ein Raub-Event je 6 Monate, keines im Protektorat.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03, Kono: Events nutzbar.

### T-066 Bruderkrieg und Eroberung (VA-021, Schritt 1)
- **Schritte:** Als Silvermoon den Wretched über die Ansprüche den Krieg erklären (Diplomatic Play). Nach Kriegsbeginn einen Monat laufen lassen, Modifier ansehen. Krieg gewinnen und alle Wretched-States nehmen (oder Konsole `annex WRETCHED_BLOODELFES`, dann prüfen nur das Ende), einen Monat laufen lassen.
- **Erwartet:** Im Krieg Modifier „War against Our Own“ (Legitimität −10, Unruhe-Folgen +25 %), nach Kriegsende weg. Gehen die Wretched unter, während Silvermoon ihr Land hält: Popup „War against Our Own“ (wretched_events.16), Silvermoon 5 J. „Scars of the Kinslaying“, die ehemaligen Wretched-States 10 J. „Wretched Addicts“, JE beendet.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03, Kono: Bruderkrieg-Modifier im Krieg, danach Folge-Modifier. Nebenbefunde: fehlende Einheiten-Icons → VA-058, Regionsname `region_searing_gorge` → VA-057.

### T-067 error.log: Wretched Schritt 1 (Claude)
- **Schritte:** Nach T-064 bis T-066 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `va_silvermoon_wretched_threat_bar`, `scripted_bar_progress`, `add_progress`, `add_claim`, `random_list`, `wretched_events.1x`, `va_silvermoon_kinslaying_*`, `va_silvermoon_unsafe_road`, `harbor_overrun`, `wall_breach`, `apprentices_disciplined`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03, Claude: error.log (20:28) ohne Zeilen zu den Objekten dieser Runde.

## Runde 15 – Wretched Schritt 2–4 (Stand 2026-11-03)

Ticket: VA-021. Lint vor Freigabe: 0 neue Fehler (2026-11-03). Neue Kampagne nötig (Charaktere und Sucht-Stufe kommen aus der Start-History).

### T-071 Sucht-Stufen (VA-021)
- **Schritte:** Neue Kampagne als Silvermoon. `play WRETCHED_BLOODELFES`, Modifier ansehen, zurück. Pakt anbieten (bzw. Konsole), 12 Monate Protektorat ohne Mana-Knappheit bei den Wretched laufen lassen. Gegenprobe: Wretched 12 Monate im Mana-Entzug.
- **Erwartet:** Wretched starten mit „Desperate Hunger (AI WRITTEN)“ (Stufe 3) statt „Wretched Addiction“. Nach 12 Monaten versorgtem Protektorat „Gnawing Hunger“ (Stufe 2), nie tiefer ohne Heilung. 12 Monate Entzug: eine Stufe höher.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-072 Heilen in drei Etappen und Rückfall (VA-021)
- **Schritte:** Protektorat, „Begin the Healing“. Balken bis 20, 40, 60 laufen lassen (Konsole/Zeit). Einmal Mana bei den Wretched 3 Monate knapp machen (Entzug).
- **Erwartet:** Start: Wretched „Supervised Withdrawal (AI WRITTEN)“. Bei 20: „The First to Recover“, Bedrohung −10, Sucht −1, Silvermoon „Growing Hope“ (Legitimität +5), Wretched „Clarity“. Bei 40: „Their Eyes Grow Clear“ mit Waldläufer (−15.000, „Healed Rangers“) oder Arbeiter („Healed Workers“), Sucht −1, Silvermoon „Families Reunited“, Wretched „Longing for Home“. Bei 60: „The Wretched Healed“, alle Etappen-Modifier weg. Nach 3 Monaten Entzug: „Relapse“ mit Notlieferung (−50.000) oder Balken −6.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-073 Eingliedern nach Sucht-Stufe (VA-021)
- **Schritte:** Je ein Spielstand mit Wretched auf Stufe 3 und Stufe 2 (siehe T-071), jeweils „Absorb the Wretched“.
- **Erwartet:** Stufe 3: States 10 J. „Wretched Addicts“, Silvermoon 10 J. „The Wretched Absorbed“ (Legitimität −10). Stufe 2: 6 J. Addicts, 6 J. Absorbed mit −5. Stufe 1: keine Addicts, 5 J. Legitimität −5. Nach etwa 2 Jahren „Plunder of the Mana Stores“ (hart: 1 J. „Mana Stores Guarded“; versorgen: −25.000, ein State verliert Addicts).
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-074 Anführer und Kopfgeld (VA-021)
- **Schritte:** Neue Kampagne. Wretched-Charaktere ansehen (Herrscher, Generäle, Agitatoren). Als Silvermoon die drei Kopfgeld-Schalter ansehen, einen drücken, bis Erfolg oder 12 Monate laufen lassen.
- **Erwartet:** Herrscher „Thaelis the Hungerer (AI WRITTEN)“, General „Aldaron the Reckless“, Agitator „Felendren the Banished“. Drei Schalter (WANTED Thaelis −30.000, Aldaron −25.000, Felendren −20.000), nur einer zugleich, gesperrt bei Krieg oder Protektorat. Erfolg: Popup, Anführer tot, Bedrohung −20, ggf. nach 2 Monaten „The Wretched Take Revenge“ (+10). Aldaron: „Harbor Overrun“ endet. Felendren: Wahl Splitter. 12 Monate ohne Erfolg: „The Hunt Has Failed“, Bedrohung +10, Schalter 1 Jahr gesperrt.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-075 Führungslos und 20-Jahre-Ablauf (VA-021)
- **Schritte:** Alle drei Anführer per Kopfgeld töten (Konsole/Zeit). Getrennt: JE 20 Jahre ohne Lösung auslaufen lassen.
- **Erwartet:** Nach dem dritten: „The Wretched Fall Apart“, Wretched-Land gehört Silvermoon, Devastation 50 in den ehemaligen Wretched-States, Addicts nach Stufe, keine Legitimitätsstrafe, JE erledigt. Ablauf: 10 J. „Our Own Left Behind“ (Prestige −10 %).
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-076 Mana-Aufstand (VA-021)
- **Schritte:** Silvermoon (oder anderes Land mit Mana-Kultur und mindestens 2 States) lange in Mana-Entzug halten, Konsole `set_variable` geht nicht → Mana-Preis hoch lassen. Einmal mit, einmal ohne bestehende Wretched.
- **Erwartet:** Nach 12 Monaten „Hungry in the Streets“ (Notprogramm −50.000 und Zähler −6, oder „Crackdown on the Hungry“ 2 J.). Nach 24 Monaten ohne Wretched: „Rise of the Wretched“, ein Nicht-Hauptstadt-State wird Wretched-Land (Stufe 3), Kriegs-Play zur Annexion; bei Silvermoon startet „The Wretched“ neu. Mit Wretched: „Flight to the Ruins“, Radikale in der Hauptstadt, Bedrohung +30, Wretched-Sucht +1.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-077 error.log: Wretched Schritt 2–4 (Claude)
- **Schritte:** Nach T-071 bis T-076 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `va_wretched_addiction_effects.txt`, `va_silvermoon_wretched_bounty_effects.txt`, `va_mana_uprising_effects.txt`, `va_mana_effects.txt`, `va_wretched_heal_events.txt`, `va_wretched_bounty_events.txt`, `va_mana_uprising_events.txt`, `va_wretched_characters.txt`, `va_eastern_kingdom.txt` (Charaktere), `has_template`, `kill_character`, `create_country`, `dp_annex_war`, `add_devastation`, `va_wretched_*_trigger`.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

## Runde 16 – error.log-Großputz (Stand 2026-11-03)

Ticket: VA-043 (mit VA-003, VA-026, VA-014, VA-007, VA-055). Lint vor Freigabe: 4 neue Fehler, alle Dubletten durch die Alt-Kopien, die Kono noch löschen muss (Liste in VA-043, 2026-11-03). Danach 0.

**Vorher (Kono):** die Dateien aus VA-043 „Von Kono zu löschen“ im Repo und in `mod\warcraft` löschen, `mod\warcraft` aus dem Repo neu befüllen (viele gelöschte Dateien, siehe ABLAUFPLAN „Erledigt“ 2026-11-03).

### T-078 Kampagne startet, Gebäude und Wirtschaft (VA-003)
- **Schritte:** Neue Kampagne starten, Silvermoon spielen. Gebäude-Menü öffnen, dann 2 Jahre laufen lassen.
- **Erwartet:** Kein Absturz. Silvermoon hat Waffenfabrik, Werft (statt Militärwerft), Artilleriegießerei, Marineverwaltung (statt Marinebasis), Textil- und Papierfabrik. Bauliste zeigt die 1.13-Gebäude (Kaserne, Kunstakademie, Munitionsfabrik) mit Namen statt Loc-Keys. In Outland steht das Dunkle Portal mit dem Namen „The Dark Portal (AI WRITTEN)“.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03 Kono: „läuft“.

### T-079 Startgesetze und Regierungsform (VA-014)
- **Schritte:** Kirin Tor Expedition und Wretched im Länder-Menü ansehen (Konsole `tag KIRINTOR_EXPEDITION`, Politik-Reiter).
- **Erwartet:** Kirin Tor: Herrscher-Titel „Archmage“, Regierungsform „Archmagocracy (AI WRITTEN)“. Wretched: Merkantilismus, Versammlungsrecht. Keine Länder mit Gesetzen, die sofort wechseln.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03 Kono: Kirin Tor passt, Startgesetze drin (werden später inhaltlich überarbeitet).

### T-080 Politische Bewegungen und Agitatoren (VA-003)
- **Schritte:** 5 Jahre laufen lassen, Politik-Reiter „Bewegungen“ bei Silvermoon und Stormwind ansehen.
- **Erwartet:** Bewegungen entstehen (1.13-Stand), keine historischen Erde-Agitatoren (Lenin, Mazzini …) tauchen auf.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03 Kono: Bewegungen gehen, z. B. Felendren als möglicher Agitator.

### T-082 Keine Festungsmodelle mehr (VA-060)
- **Schritte:** Kampagne starten, an Silbermond (Stadt) heranzoomen. (Test-Festungen dort hat Kono am 03.11. gesehen; jetzt entfernt.)
- **Erwartet:** Keine Festungsmodelle bei Silbermond oder sonst auf der Karte, kein Absturz.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03 Kono: passt.

### T-081 error.log: Großputz (Claude)
- **Schritte:** Nach T-078 bis T-080 und T-082 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `geographic_region_*`, `Invalid database object 'je_*'`, `country_law_manager`, `building_type.cpp` (fehlende Loc alter Gebäude), `modifier_type_definition_database`, `VA_pandaria.txt`, `VA_northrend_state.txt`, `23_north_kalimdor.txt`, `va_outlands.txt` (Pops), `infection_events.txt`, `VA_gilneas_infection.txt`, `Invalid character` in Loc-Keys, `bg_*_WIP`, `00_code_on_actions.txt`/`political_movements`/`flag_definitions` aus dem Mod. Keine `fortification_graphics`-Zeilen (VA-060), kein `Invalid right side during comparison 's'` (`08_monuments`, `10_canals`, `00_power_bloc_names`, `03_pan_national_movements`; Spiel dafür mindestens ein halbes Jahr laufen lassen), kein `Invalid building`, kein `does not have a valid namespace`/`unknown random event`, kein `is orphaned` (außer `french_pretenders.6`), kein `has_template … Invalid database object` (Erde-Vorlagen), keine `Failed to find country` aus `government_types`, keine Zeilen zu `common/achievements/`, `owned_*_region_states`, `iberian_treaty_ports`, `is_afghan_nation`, `company_is_zaibatsu`, keine Zeilen zu `00_spanish_new_world_scripted_effects`, `00_the_grand_collapse_scripted_effects`, `00_victoria_great_game_scripted_effects`, keine Meldung zu doppelt definierten Effekten aus `va_earth_effects.txt`, kein `already has a journal entry of type je_mana_hunger`. Gesamtzahl der Einträge deutlich unter 9.598 (Stand 03.11.).
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:
