# Testprotokoll

Jede Änderung, die Claude macht, bekommt hier einen Testfall. Kono testet im Spiel und hakt ab. Ein Ticket gilt erst als `erledigt`, wenn alle seine Testfälle **OK** sind.

**Ablauf je Testrunde**
0. Claude: `va_lint.py` meldet 0 neue Fehler (Voraussetzung für die Freigabe).
1. Repo-Stand in den Mod-Ordner `mod\warcraft` kopieren.
2. Victoria 3 starten, Kampagne mit dem Mod laden, Tests unten durchgehen.
3. Spiel beenden und Claude Bescheid geben. Claude wertet `error.log` aus (Testfall „Log“ der Runde) und trägt das Ergebnis ein.
4. Ergebnis je Test eintragen: `[x] OK` oder `[x] Fehler` plus kurze Notiz (was stattdessen passiert ist, Screenshot-Name).

Einmal **OK** bestätigte Tests bleiben stehen (Historie). Bei einem Fehler legt Claude ein Ticket an oder öffnet das zugehörige wieder.

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
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-004 Seradane und Scholomance
- **Schritte:** Kartenmodus „States“ bzw. Mausover auf die Region zwischen Scholomance und Seradane (Hinterland).
- **Erwartet:** Seradane umfasst das Gebiet des Emerald-Entrance-Landes und der Revantusk. Scholomance (Cult of the Damned) ist kleiner und **keine** Küstenregion mehr.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-005 West Sanctum geteilt
- **Schritte:** State West Sanctum anklicken.
- **Erwartet:** Zwei Teilstaaten, Silvermoon und Grimscale-Murlocs. Keine Provinz flackert oder gehört beiden.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-006 Quel'Danas gehört Silvermoon
- **Schritte:** Sun's Reach, Magisters' Terrace und Sunwell Plateau anklicken.
- **Erwartet:** Besitzer Silvermoon, Bevölkerung Sin'dorei. Magisters' Terrace zeigt Gebirge/unpassierbare Provinzen, Sun's Reach nicht.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-007 Hauptstädte
- **Schritte:** Länderansicht bzw. Karte für die vier Länder öffnen.
- **Erwartet:** Wildhammer → Aerie Peak, Wretched → Ruins of Silvermoon, Frostwolf Highlands → Tarren Mill, Shadowpine → Dawnstar Spire. Keine Hauptstadt liegt außerhalb des eigenen Gebiets.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-008 Tranquillien
- **Schritte:** Tranquillien in der Länderauswahl bzw. Länderansicht öffnen, Reiter „Politik/Gesetze“.
- **Erwartet:** Gesetze wie bei Silvermoon gesetzt (u. a. Protektionismus, Pachtbauern, Sklaverei verboten), keine leeren oder ungültigen Gesetze.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-009 Zul'Jarra
- **Schritte:** Zul'Aman auf der Karte anklicken.
- **Erwartet:** Das Land heißt „Zul'Jarra“ (Adjektiv „Zul'Jarran“), kein roher Key `AMANI_TRIBE`.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-010 Ressourcen im neuen Format
- **Schritte:** State Sunwell Plateau, Silvermoon City und Koroth Den öffnen, Bereich „Ressourcen/Potenziale“.
- **Erwartet:** Ressourcen werden angezeigt (z. B. Eisen, Kohle, Holz, Fischerei, Farmen). Sunwell Plateau zeigt „Ley Line Tap“ mit 40, Silvermoon City mit 20.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-011 Leylinien-Gebäude baubar
- **Schritte:** Als Silvermoon in Silvermoon City „Ley Line Tap“ bauen. Nach Fertigstellung das Gebäude öffnen.
- **Erwartet:** Baubar ohne Technologie. Produktionsmethode „Focus Crystals“, Verbrauch Werkzeug, Produktion Mana, Arbeiter und Akademiker als Belegschaft. Texte ohne rohe Keys. Icons sind Platzhalter (Kohlemine/Strom), das ist gewollt.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-012 Mana am Markt
- **Schritte:** Marktansicht von Silvermoon öffnen, Gut „Mana“ suchen.
- **Erwartet:** Gut „Mana“ ist vorhanden, Angebot steigt nach T-011. Preis am Minimum ist **erwartet**, denn es gibt noch keine Abnehmer (VA-019).
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

---

## Runde 2 – Log-Spam (Stand 2026-10-30)

Tickets: VA-025. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Danach T-002 aus Runde 1 wiederholen.

### T-013 Log bleibt lesbar
- **Schritte:** Kampagne starten, auf höchster Geschwindigkeit etwa 2–3 Monate laufen lassen, Spiel beenden.
- **Erwartet:** Im Log-Ordner gibt es nur `error.log` oder wenige Rotationsdateien, und `error.log` beginnt mit den Ladefehlern vom Spielstart (nicht mit `Script system error!` aus dem laufenden Spiel).
- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-10-30 ein Jahr gelaufen, kein Absturz. Log rotiert weiter, jetzt durch `is_oppressor_of_schleswig_holstein` (11.071 Einträge in ~10 s). Behoben mit `va_earth_triggers.txt` → T-015.

### T-014 error.log (Claude)
- **Schritte:** Nach T-013 Claude Bescheid geben. Claude prüft mit `va_errlog.py`: keine Einträge mehr aus `00_scripted_triggers.txt:357–393` (`in_volcanic_zone`), `00_ai_triggers.txt:619–634` (`should_carve_up_china`), `has_law_or_variant`-Fehlern und `historic_agitator_events.txt`. Danach T-002 (Runde 1) mit dem vollständigen Log auswerten.
- **Erwartet:** Diese Fehlergruppen sind weg; die restlichen Fehler werden als neue Tickets erfasst.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30 alle vier Gruppen (Vulkan, China, has_law_or_variant, Agitatoren) sind weg. Rest: Fortschrittsbalken (72+), Power-Bloc-Namen `00_power_bloc_names.txt:577` (19), Petitions-Events (9), Archerus-Fischerei (7).

### T-015 Log bleibt lesbar (zweiter Anlauf) – entfällt, geht in Runde 3 auf
- **Schritte:** Wie T-013: Kampagne starten, ein paar Monate auf höchster Geschwindigkeit laufen lassen, Spiel beenden, Claude Bescheid geben. Neu seit T-013: `common/scripted_triggers/va_earth_triggers.txt` (17 Erde-Trigger auf „nie wahr“).
- **Erwartet:** Höchstens eine `error.log` ohne Rotationsdateien, beginnt mit den Ladefehlern. Keine Einträge aus `00_scripted_triggers.txt:1727` (Schleswig-Holstein). Danach wertet Claude T-002 vollständig aus.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

---

## Runde 3 – events aus replace_paths (Stand 2026-10-30)

Tickets: VA-002, VA-025. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Alte Kopien sind bereinigt (`va_events.py --apply-copies`, 2026-10-30). Runde 3 ersetzt T-015.

### T-016 Kampagne lädt und läuft
- **Schritte:** Repo in `mod\warcraft` kopieren (alte Dateien dort vorher löschen, sonst bleiben die gelöschten Kopien liegen). Kampagne als Silvermoon starten, 1 Jahr laufen lassen.
- **Erwartet:** Kein Absturz. Es tauchen allgemeine Events auf (Wahlen, Gesetzesdebatten, Petitionen o. Ä.), aber keine Erde-Events (Brasilien, Japan, Balkan …).
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30 ein Jahr bis 1. Januar gelaufen. Gesehen: „Request Market Control“ (13. Januar, Diplomatie-Aktion) und „Secret Societies“ (5. April, `autocracy.2` aus Vanilla 1.13). Beides allgemeine Mechaniken, keine Erde-Events.

### T-017 error.log (Claude)
- **Schritte:** Nach T-016 Claude Bescheid geben.
- **Erwartet:** Log rotiert nicht oder kaum, die Ladefehler vom Start sind lesbar. Claude wertet T-002 vollständig aus und legt für verbleibende Fehlergruppen Tickets an. Einmalige „unbekanntes Event“-Fehler aus `common/on_actions/00_*.txt` sind erwartet (VA-003).
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30 Log vollständig lesbar: Start 11:08:40 bis Ende 11:12:02, nur zwei Rotationen während des Ladens, im laufenden Spiel kein Spam mehr (`error.log` 487 KB über drei Minuten). Schleswig-Holstein nur noch 3× (REPLACE wirkt). T-002 damit ausgewertet. Restliche Fehlergruppen → VA-001 (Notizen) und VA-026.

---

## Runde 4 – allgemeine Events und JEs zurück (Stand 2026-10-30)

Tickets: VA-002. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Kann zusammen mit den offenen Tests aus Runde 1 laufen. `mod\warcraft` vorher neu befüllen; die zwei Dateien unten dürfen dort **nicht** mehr liegen.

### T-018 error.log: Sklavenaufstand und Anarchismus (Claude)
- **Schritte:** Kampagne starten, ein paar Monate laufen lassen, Spiel beenden, Claude Bescheid geben. Wieder aktiv aus Vanilla: `events/agitators_events/slave_revolt_events.txt`, `events/iberia_events/ip4_anarchism_events.txt`.
- **Erwartet:** Keine Fehler aus diesen beiden Dateien im `error.log`. Ob die Events im Spiel auftauchen, ist Zufall und kein Testkriterium.
- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-10-30 (ein Jahr gelaufen, kein Absturz): `slave_revolt_events.txt` fehlerfrei. `ip4_anarchism_events.txt:379` 1× `building_art_academy` unbekannt. Ursache liegt nicht in der Eventdatei: Die alten Mod-Kopien unter `common/buildings/` kennen die 1.13-Gebäude nicht → VA-003. Event-Datei bleibt aktiv.

### T-019 Journal: allgemeine JEs da, keine Erde-JEs
- **Schritte:** `mod\warcraft` **vorher leeren** und neu befüllen (viele Dateien gelöscht). Kampagne als Silvermoon starten, Journal öffnen (aktive und mögliche Einträge). Ein Jahr laufen lassen, Journal erneut ansehen.
- **Erwartet:** Allgemeine Einträge wie Kunstrichtungen (Romantik), Prestigegüter, Lebensstandard oder Interessengruppen-Agenden können auftauchen. Keine Einträge mit Erde-Bezug (Japan, Brasilien, Indien, Afrika, Expeditionen). Petitionen der Interessengruppen zeigen ihre Buttons („Verlängerung“, „Abweisen“) mit Text.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Silvermoon nach einem Jahr, Reiter „Potential“: Poverty Crisis, Religion/Autocracy/Nationality, Corn Laws, Path to Liberalism, Patronize Romanticism, Patronize Realist Art, From Farms to Factories, Urbanize. Alles allgemein, kein Erde-Eintrag. „Urbanize SILVERMOON“ zeigt den rohen Tag statt des Ländernamens → bekannt, VA-006. Petitions-Buttons nicht gesehen (keine Petition aktiv), bei Gelegenheit nachholen.

### T-020 error.log: JEs und Buttons (Claude)
- **Schritte:** Nach T-019 Claude Bescheid geben.
- **Erwartet:** Keine Fehler `Invalid journal entry type` mehr für `je_government_petition`, `je_law_imposition` und `je_divided_monarchists` aus Coup-Events. Die 26 Fehler „can only be used for country context“ aus `government_petition_events.txt` sind weg. Keine Ladefehler aus `common/journal_entries/0*.txt` oder `common/scripted_buttons/0*.txt`. Übrig bleiben dürfen Great-Game-Ziele (bekannt, VA-002 Notizen) und Gilneas (VA-007).
- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-10-30, 9.922 Einträge. **Behoben:** `je_government_petition` und `je_law_imposition` sind nicht mehr ungültig, „country context“ 0× (vorher 26×). **Erwartet geblieben:** Great-Game-Ziele, Gilneas. **Fehler:** (1) `has_journal_entry` auf abgeschaltete JEs erzeugt doch Ladefehler (712×, z. B. `je_divided_monarchists` in Vanilla-Gesetzen, -Ideologien und `government_conflicts_events.txt`); Annahme in VA-002 war falsch → Notiz dort. (2) Aus Vanilla-JEs: fehlende 1.13-Gebäude (`building_art_academy`, `building_steel_mill`, `building_barrack` in `coup_events.txt`) und fehlender Effekt `rebind_prestige_good_company` (`05_prestige_goods.txt`) – beides durch alte Mod-Kopien (`common/buildings/0*.txt`, `common/scripted_effects/00_scripted_effects.txt`) → VA-003. (3) Eigene JEs `VA_silvermoon.txt` und `VA_gilneas_infection.txt`: kein BOM, `should_be_pinned_by_default` gibt es in 1.13 nicht mehr, Gilneas zusätzlich `je_group_g` ungültig → VA-020 bzw. VA-007. (4) `events/scotland_yard.txt:16` fragt `STATE_HOME_COUNTIES` ohne `s:` ab; `va_events.py` erkennt solche Verweise nicht → VA-002.

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
- **Erwartet:** Keine neuen Fehler aus `common/history/buildings/26_north_eastern_kingdoms.txt` und `27_center_eastern_kingdoms.txt`, kein „Tried to create building … already exists“ außer dem bekannten Archerus-Fischkai (VA-024). Keine ungültigen Produktionsmethoden.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:
