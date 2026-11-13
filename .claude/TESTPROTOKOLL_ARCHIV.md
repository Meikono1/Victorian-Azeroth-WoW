# Testprotokoll – Archiv

Abgeschlossene Testrunden aus `TESTPROTOKOLL.md`: alle Testfälle OK, entfallen oder per Folgetest bzw. Ticket erledigt. Nur zum Nachschlagen (Historie), bei der Arbeit nicht lesen. Runden nach Nummer sortiert.

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

### T-023 error.log: Firmen und Charaktervorlagen (Claude)

- **Schritte:** Nach T-021/T-022 Claude Bescheid geben.

- **Erwartet:** Keine Fehler aus `common/character_templates/` (insbesondere kein doppeltes `default`), keine aus `common/company_types/` außer bekannten Gebäudenamen aus den alten Gebäudekopien (VA-003). Vanilla-Vorlagen für Kolonialgouverneure (`colonial_governor_templates.txt`) laden ohne Fehler.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, 7 Jahre gelaufen, Log ab Ladebeginn vollständig (14.051 Einträge). Keine Fehler aus `common/character_templates/`, kein doppeltes `default`. `99_basic_companies.txt` 27× `is_building_type` (erwartet: Vanilla-Datei lädt, alte Kopie noch nicht zurückgeholt, VA-003). Bekannt und unverändert: `has_template` auf Erde-Vorlagen aus Vanilla-Scripts (~450, waren vorher schon fehlende Vorlagen) und `is_company_type` in `00_company_charter_types.txt`. Beim Lauf aufgefallen: weltweite Hungersnot → VA-029.

---

## Runde 7 – Neue History-Ordner abgefangen (Stand 2026-10-30)

Tickets: VA-004. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Kann mit Runde 5 und 6 laufen. `mod\warcraft` neu befüllen (inkl. `.metadata/metadata.json`).

### T-034 History-Ordner ohne Erde-Inhalte (VA-004)

- **Schritte:** Kampagne starten. Bei Stormwind und Silvermoon im Politik-Fenster die politischen Bewegungen ansehen. Im Kulturfenster (z. B. Kultur von Stormwind) den Fervor ansehen.

- **Erwartet:** Länder haben Start-Bewegungen (Royalisten, religiöse und kulturelle Mehrheit, ggf. Pro-Sklaverei). Kulturen haben Fervor ≥ 5. `error.log` ohne Zeilen aus `common/history/military_deployments/`, `common/history/diplomatic_plays/`, `common/history/governments/`, `common/history/cultures/00_cultures.txt`, `common/history/political_movements/00_movements.txt` und ohne neue Zeilen aus `va_movements.txt`, `va_cultures.txt`, `va_ai_strategy.txt` (Claude). Zeilen aus `history/conscription/` bleiben bis VA-003.

- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-10-30, Kono: Bewegungen vorhanden. Fervor Blood Elf startet bei **0** (Ziel 7), `va_cultures.txt` greift also nicht → T-035. Log 18:21 (4 Dateien, 19.584 Zeilen, ab Ladebeginn): keine Zeilen mehr aus `military_deployments`, `diplomatic_plays`, `military_formations`, `governments`, `cultures`, `political_movements`, `ai`; nichts aus den neuen `va_`-Dateien. Übrig nur 2× `is_building_type` in `conscription/00_conscription_center.txt` (erwartet, VA-003).

### T-035 Start-Fervor (VA-004)

- **Schritte:** `common/history/cultures/va_cultures.txt` in `mod\warcraft` kopieren. Kampagne starten (neu, kein Spielstand), im ersten Tag pausiert lassen. Gesellschaft → Kulturen: Fervor („Current“) von Blood Elf (Silvermoon), Stormwindian (Stormwind) und Bronzebeard (Ironforge) ablesen.

- **Erwartet:** Blood Elf 10 (Kontrollwert), Stormwindian und Bronzebeard 5. Auswertung: Blood Elf 10 und Rest 0 → Schleife über `every_country` greift nicht, Claude stellt auf Direktwerte je Kultur um. Alles 0 → Fervor-History wirkt gar nicht (zu früh/überschrieben). `error.log` ohne Zeilen aus `va_cultures.txt` (Claude).

- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-10-30, Kono: Blood Elf 10, Stormwindian 0, Bronzebeard 0 → nur Direktaufruf `cu:` wirkt, Schleife nicht. Log 18:27 ohne Zeilen aus `history/cultures`. Umgestellt auf Direktwerte → T-036.

### T-036 Start-Fervor je Kultur (VA-004)

- **Schritte:** `common/history/cultures/va_cultures.txt` in `mod\warcraft` kopieren. Neue Kampagne starten, am ersten Tag pausiert lassen. Gesellschaft → Kulturen: Fervor („Current“) von Blood Elf (Silvermoon), Stormwindian (Stormwind) und Bronzebeard (Ironforge) ablesen.

- **Erwartet:** Alle drei bei 5. `error.log` ohne Zeilen aus `va_cultures.txt` (Claude).

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: alle drei bei 5. Log 18:47 ohne Zeilen aus `history/cultures`.

## Runde 8 – Handelszentralen für den Weltmarkt (Stand 2026-10-30)

Ticket: VA-040. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Zum Testen am besten als **Stormwind** spielen.

### T-037 Handel in Eastern Kingdoms (VA-040)

- **Schritte:** Kampagne starten. In Stormwind, Undercity, Ironforge und Booty Bay im Staatenfenster der Hauptstadt die Handelszentrale ansehen. Handels-Lens bzw. Marktfenster von Stormwind öffnen (Importe/Exporte). 1 Jahr laufen lassen, dann erneut Handelsrouten und Food Security in Nord- und Süd-EK ansehen.

- **Erwartet:** 46 EK-Länder haben eine Handelszentrale in der Hauptstadt (Stormwind, Undercity, Ironforge, Vashj'ir je 10 Stufen, Booty Bay 7, Silvermoon 5). Booty Bay und Hammerfall haben jetzt einen Hafen. Nach kurzer Zeit laufen Importe und Exporte, mindestens Getreide/Nahrung wird zwischen Märkten gehandelt. Länder mit Isolationismus (Amani, Defias, Murloc-Stämme u. a.) handeln weiterhin nicht. Merchant-Marine-Engpass in großen Zentralen möglich, Kono notiert ihn.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: Handel sitzt, die Länder nutzen ihn. Nebenbefund: KI stapelt Construction Sector und Government Administration (Stormwind 40+ Aufträge), `building_paper_mills` ohne Loc → VA-044.

### T-038 error.log: Handelszentralen, Verwaltung, Bausektor (Claude)

- **Schritte:** Nach T-037 und T-039 Claude Bescheid geben.

- **Erwartet:** Keine neuen Zeilen zu `building_trade_center`, `building_government_administration`, `building_construction_sector` oder deren PMs aus `common/history/buildings/26_*`, `27_*`, `28_*`.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: Log 30.10. 20:26 (`va_errlog.py`, 4 Dateien, 9.616 Einträge): keine Zeilen zu den drei Gebäuden oder aus `history/buildings/26–28`. Übrig nur bekannte Altlasten (VA-003, VA-026, VA-043).

### T-039 Verwaltung und Bausektor zum Start (VA-044)

- **Schritte:** Kampagne starten als Stormwind. Bürokratie (Länderübersicht) und Bauliste ansehen, Stormwind-Hauptstadt im Staatenfenster öffnen. Danach Ironforge und ein kleines Land (z. B. Menethil) ansehen. 2 Jahre laufen lassen, Bauliste von Stormwind und 2–3 KI-Ländern erneut ansehen.

- **Erwartet:** Stormwind startet mit 21 Stufen Government Administration und 5 Stufen Construction Sector, Bürokratie nicht (stark) negativ. Die KI-Baulisten bestehen nicht mehr überwiegend aus Verwaltung und Bausektor. Papiermangel in der Verwaltung möglich (bekannt, VA-003), Kono notiert ihn.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: Verwaltung okay, nur wenige Stellen mit Mangel. Bausektor stapelt die KI weiterhin, liegt aber auch daran, dass es keine Probleme gibt, die Geld kosten (KI hat Überschuss und steckt ihn in Bau). Rest über Content (VA-034).

## Runde 9 – Mana als Obsession der Elfen (Stand 2026-10-30)

Ticket: VA-019. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Zum Testen am besten als **Silvermoon** spielen.

### T-040 Mana-Nachfrage durch Elfen (VA-019)

- **Schritte:** Kampagne starten als Silvermoon. Kulturfenster `Sin'dorei` und `Quel'dorei` öffnen (Obsessionen). Marktfenster Silvermoon → Mana: Angebot, Nachfrage, Preis. Ein Pop der Blutelfen öffnen → Bedürfnis „Intoxicants“. Zum Vergleich Marktfenster Stormwind → Liquor/Tobacco. 1 Jahr laufen lassen, Mana-Preis erneut ansehen.

- **Erwartet:** Beide Elfenkulturen haben die Obsession Mana. Mana hat im Silvermoon-Markt Pop-Nachfrage, der Preis liegt nicht mehr am Minimum. Im Bedürfnis Intoxicants steht Mana **zusätzlich** zu Liquor, Tobacco, Opium und Wine (wichtig: `INJECT` darf die Vanilla-Einträge nicht ersetzen; in Stormwind wird weiter Liquor/Tobacco konsumiert). Andere Kulturen kaufen Mana höchstens in kleinen Mengen.

- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-10-30, Kono: andere Rauschmittel gehen weiter, Mana erscheint mit 1.3. Effekt aber zu schwach. KI baut Ley Line Taps selbstständig. → Mana aus Intoxicants raus und nur noch in Stimulants (Kono: kein Rauschmittel), T-042. 2026-11-12, Claude: erledigt durch Folgetests (Mana-Grundbedarf T-123 OK).

### T-041 error.log: Mana-Obsession (Claude)

- **Schritte:** Nach T-040 Claude Bescheid geben.

- **Erwartet:** Keine Zeilen zu `common/pop_needs/va_pop_needs.txt`, `va_goods.txt`, `obsessions` in `va_elfen_cultures.txt` oder „unknown goods mana“.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Claude: error.log ohne Mana-Zeilen.

### T-042 Mana-Nachfrage verstärkt (VA-019)

- **Schritte:** Wie T-040: Kampagne als Silvermoon, Marktfenster Mana (Nachfrage, Preis), Blutelfen-Pop → Bedürfnisse Intoxicants und Stimulants. Marktfenster Stormwind → Mana, Tea, Tobacco. 2 Jahre laufen lassen, Mana-Preis und Zahl der Ley Line Taps in Silvermoon ansehen.

- **Erwartet:** Mana steht nur noch in Stimulants (neben Sugar, Tea, Coffee, Tobacco), nicht mehr in Intoxicants. Mana-Nachfrage in Silvermoon deutlich höher als in T-040, Preis über Grundpreis (40) oder zumindest klar über dem Minimum. Nebenwirkung: Auch Menschen u. a. kaufen spürbar Mana (Gewicht wie Tobacco). Kono notiert, ob das zu viel ist; dann sinkt das Grundgewicht wieder und die Elfen bekommen einen eigenen Hebel (Baustein 2).

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12 (Kono): Silvermoon fragt Mana rund 8-mal so stark nach wie andere Länder, guter Wert. Quel'Danil Lodge (Hochelfen) ebenfalls abhängig, schwächer als Blutelfen. Mana-Obsession aktualisiert sich nach dem ersten Monat.

### T-043 Mana-Angebot zum Start (VA-019)

- **Schritte:** Kampagne als Silvermoon. Staatenfenster Sunwell Plateau ansehen. Marktfenster Silvermoon → Mana (Angebot, Nachfrage, Preis). Marktfenster Stormwind → Mana. 1 Jahr laufen lassen, erneut ansehen.

- **Erwartet:** Sunwell Plateau hat 1 Stufe Ley Line Tap (Silvermoon, PM Focus Crystals), voll besetzt (10.000 Sin'dorei im State, Bedarf 4.000 Arbeiter + 500 Akademiker). Silvermoon-Markt bietet ab Start bis zu 20 Mana an; die Nachfrage (Werte 0.65/0.1) liegt dort jetzt höher als 11, weil Angebot da ist. Überschuss geht über die Handelszentrale in andere Märkte, Stormwind importiert ggf. Mana. Preis nicht am Minimum.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Sunwell Plateau besetzt, Mana wird hergestellt; kleiner Werkzeugmangel (später lösen).

### T-044 Todesschneise (VA-019)

- **Schritte:** Kampagne als Silvermoon. Staatenfenster von Sunwell Plateau, Ruins of Silvermoon, West Sanctum, East Sanctum, Tranquillien und Deathholme öffnen (Modifier-Liste), Tooltip lesen. Zum Vergleich Silvermoon City, Sanctum of the Sun und Farstrider Retreat. Wo Ackerbau steht: Durchsatz ansehen.

- **Erwartet:** Die sechs States tragen „The Dead Scar“ (Platzhalter-Icon Feuer): Ackerbau-Durchsatz −30 %, Infrastruktur −15 %, Baugeschwindigkeit −15 %. Zusätzlich „Shadow of the Dead Scar“ (Sterblichkeit +10 %, Migrationssog −50 %) **nur** dort, wo Lebende die Mehrheit stellen: Sunwell Plateau, Ruins of Silvermoon, West Sanctum, Silvermoons Teile von East Sanctum und Tranquillien, Tranquilliens Teil. **Nicht** in Deathholmes Teilen (Banshees). Andere States ohne Modifier. Wird der Zweitmodifier zum Start nicht gesetzt, aber nach einem Jahr schon, läuft nur die On-Action (dann Startaufruf prüfen). Kono notiert, ob die Auswahl der States und die Stärke passen.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: Untote Bereiche ohne Lebenden-Malus, Elfen-Bereiche mit. Effekte greifen gut. Infrastruktur auf −30 % erhöht (nur Wert, kein neuer Test nötig).

### T-045 error.log: Mana-Angebot, Todesschneise (Claude)

- **Schritte:** Nach T-043 und T-044 Claude Bescheid geben.

- **Erwartet:** Keine Zeilen zu `building_leyline_tap` aus `history/buildings/26_*`, zu `va_dead_scar`, `va_quel_thalas_modifiers.txt`, `history/global/va_global_quel_thalas.txt` `va_quel_thalas_l_english.yml`, `va_undead_triggers.txt`, `va_undead_values.txt` (`total_size`, `this = cu:`), `va_quel_thalas_effects.txt`, `va_on_actions_quel_thalas.txt` oder `culture_percent_state`.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Claude: keine Zeilen zu Mana-Angebot/Todesschneise.

### T-046 Todesschneise bei Eroberung (VA-019)

- **Schritte:** Kampagne als Silvermoon. Zum Start die sechs Schneisen-States wie in T-044 ansehen (beide Modifier wie vorher). Dann per Konsole oder Krieg einen Deathholme-Teil übernehmen, z. B. Deathholmes Teil von Tranquillien oder East Sanctum (`annex DEATHHOLME` oder Friedensvertrag). Direkt danach und nach 1 Monat den State ansehen.

- **Erwartet:** Zum Start unverändert: „The Dead Scar“ auf allen sechs States, „Shadow of the Dead Scar“ nur bei Elfen-Mehrheit. Nach der Übernahme steht „The Dead Scar“ weiter auf dem State (auch wenn er mit dem Silvermoon-Teil verschmilzt). „Shadow of the Dead Scar“ passt sich sofort bzw. spätestens nach einem Monat an die neue Mehrheit an, nicht erst nach einem Jahr.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono: Anpassung nach Übernahme nahezu sofort.

### T-047 Mana-Hunger als Journal Entry (VA-019)

- **Schritte:** Kampagne als Silvermoon. **Sofort zum Start** das Journal öffnen (Innere Angelegenheiten), danach die Länder-Modifier. Dasselbe kurz für Tranquillien und Wretched (Länderfenster → Journal bzw. Modifier). Zum Vergleich Stormwind. Dann per Konsole oder Abriss den Ley Line Tap auf Sunwell Plateau entfernen bzw. Mana-Preis steigen lassen und 1–2 Monate warten.

- **Erwartet:** „The Mana Hunger (AI WRITTEN)“ ist ab Tag 1 aktiv und angeheftet, die Beschreibung erklärt die drei Stufen mit Preisgrenzen. Die Statuszeile zeigt die aktuelle Stufe (grün Arcane Abundance, neutral Stable, rot Scarcity/Withdrawal) und passt zum Länder-Modifier. Stufen: ≤ 40 Arcane Abundance (Forschung +10 %, Lebensstandard +1), 41–49 keine, ≥ 50 Mana Scarcity (Lebensstandard −1, Radikale/Loyale aus Lebensstandard +10 %), ≥ 68 Mana Withdrawal (Lebensstandard −2, Radikale/Loyale +25 %, Sterblichkeit +5 %, Durchsatz −10 %). Wechsel spätestens einen Monat nach Preisänderung. Stormwind hat weder JE noch Modifier.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-10-30, Kono (Screenshot Highvale): JE aktiv, Status „Mana Withdrawal“ mit passenden Werten. Bedingungen zeigten „culture_this_equal has no localization“ → per `custom_tooltip` behoben, beim nächsten Start Tooltip erneut ansehen. `HIGHVALE_HIGHELFES_ADJ` ohne Loc → VA-006. 2026-11-12, Kono: JE ab Spielstart, Fortschritt monatlich, Modifier kommen.

### T-048 error.log: Mana-Abhängigkeit (Claude)

- **Schritte:** Nach T-047 Claude Bescheid geben.

- **Erwartet:** Keine Zeilen zu `va_mana_modifiers.txt`, `va_mana_triggers.txt`, `va_mana_effects.txt`, `journal_entries/va_mana.txt`, `je_mana_hunger`, `add_journal_entry`, `market_goods_pricier`, `market_capital` oder `mg:mana`.

- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Claude: keine Zeilen zu Mana-Abhängigkeit.

## Runde 10 – Silvermoon-Ziele (Stand 2026-10-30)

Ticket: VA-020. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Als **Silvermoon** spielen.

### T-049 Silvermoon-JEs zum Start (VA-020)
- **Schritte:** Kampagne als Silvermoon. Journal → Historischer Inhalt öffnen. Danach Karte: Ansprüche auf Deathholme, Windrunner Village, Tranquillien, East Sanctum, Suncrown Village, Zul'Aman, Tor Watha.
- **Erwartet:** Drei JEs aktiv und angeheftet: „Drive Out Deathholme“ (Ziel: Deathholme existiert nicht, Ablauf 15 Jahre), „Raze Zul'Aman“ (Ziel: Zul'Aman und Tor Watha vollständig besitzen, Ablauf 20 Jahre), das Heil-JE prüft jetzt T-053. Alle Texte enden mit „(AI WRITTEN)“. Ansprüche auf den sieben States vorhanden.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Drive Out Deathholme läuft, Straße wird nach und nach gebaut. Korridor-Bürokratie zu billig → −25 auf −50 (va_silvermoon_corridor_logistics).

### T-050 Heilritual der Todesschneise (VA-020) – entfällt, ersetzt durch T-053/T-054 (VA-046)
- **Schritte:** Knopf „Fund a Healing Ritual“ drücken (kostet 25.000, Gold muss reichen). Tooltip des Knopfs vorher ansehen. 24 Monate laufen lassen (Konsole `tick` oder schnell vorspulen). Optional: Mana-Preis in „Mana Withdrawal“ treiben und prüfen, dass das Ritual ruht.
- **Erwartet:** Knopf zeigt Bedingungen lesbar (kein Ritual aktiv, eigener State auf der Schneise, Gold). Danach Status „A healing ritual is underway“, im Mana-Entzug „The ritual has stalled …“. Nach 24 Monaten Popup „The Scar Recedes“ mit State-Namen; der genannte State verliert „The Dead Scar“ und „Shadow of the Dead Scar“, Fortschritt 1/6, Knopf wieder nutzbar.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-051 Deathholme und Zul'Aman abschließen (VA-020)
- **Schritte:** Konsole: `annex DEATHHOLME`, 1 Tag warten. Dann `annex AMANI_TRIBE` (Zul'Aman und Tor Watha), 1 Tag warten. Modifier-Liste von Silvermoon ansehen.
- **Erwartet:** Popup „Deathholme Falls“, Modifier „The Ghostlands Avenged“ (Prestige +25, 10 Jahre). Popup „Zul'Aman Taken“, Modifier „The Amani Broken“ (Prestige +25, 10 Jahre). Beide JEs abgeschlossen.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Annex Deathholme per Konsole → „Quel'Thalas Avenged“, +25 Prestige.

### T-052 error.log: Silvermoon-Ziele (Claude)
- **Schritte:** Nach T-049 bis T-051 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `VA_silvermoon.txt`, `va_silvermoon_buttons.txt`, `va_silvermoon_events.txt`, `va_silvermoon_modifiers.txt`, `va_silvermoon_values.txt`, `va_quel_thalas_triggers.txt`, `va_quel_thalas_effects.txt`, `va_silvermoon_l_english.yml`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Claude: keine Zeilen zu Silvermoon-Zielen.

## Runde 11 – Todesschneise heilen (Stand 2026-10-30)

Ticket: VA-046. Lint vor Freigabe: 0 neue Fehler (2026-10-30).

### T-053 Heil-JE für alle Besitzer (VA-046)
- **Schritte:** Kampagne als Silvermoon. Journal → Innere Angelegenheiten. Dann per Länderwechsel (Konsole `play DEATHHOLME`, `play WRETCHED_BLOODELFES`, `play TRANQUILLIEN`) dort ebenfalls ins Journal sehen.
- **Erwartet:** „Heal the Dead Scar (AI WRITTEN)“ aktiv bei allen Ländern mit State auf der Schneise (Silvermoon, Deathholme, Tranquillien, Wretched u. a.), sechs Balken mit Regionsnamen (0/20), Schalter „Begin Healing: …“ nur für Regionen, in denen das Land einen verdorbenen State hat. Beschreibung erklärt Kosten und 20 Monate. Länder ohne Schneisen-State (z. B. Stormwind) haben das JE nicht.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: Kono 2026-10-31: Heilen mit Teilbesitz klappt, nach Eroberung erscheinen die Schalter.

### T-054 Ritual an, aus, fertig (VA-046)
- **Schritte:** Als Silvermoon „Start Ritual: Sunwell Plateau“ drücken. State Sunwell Plateau → Gebäude ansehen, Haushalt (Ausgaben), Bürokratie, Mana-Markt. 3 Monate laufen lassen, dann „Stop Ritual“ drücken, 2 Monate warten, wieder einschalten. Danach bis 20 Monate vorspulen.
- **Erwartet:** Beim Einschalten sinkt die Staatskasse sofort um 100.000 (auch beim Wiedereinschalten). Danach steht eine „Ritual Site“ (staatlich, nicht erweiterbar) mit Clerks/Academics, Bürokratie sinkt um bis zu 25, Mana-Nachfrage +15, Papier-Nachfrage +10, Lohnkosten im Haushalt. Schalter-Tooltip und JE-Text nennen die Kosten. Status „Healing rituals are underway“. Balken +1 je Monat, beim Abschalten verschwindet das Gebäude und der Balken bleibt stehen. Im Mana-Entzug steht der Balken still (Status „stalled“). Bei 20: Popup „The Scar Recedes“ mit State-Namen, Ritual Site weg, „The Dead Scar“ und „Shadow of the Dead Scar“ verschwinden, der Schalter für die Region ist weg.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: Kono 2026-10-31: Heilen klappt grundsätzlich; Kosten werden nachgeschärft, danach erneut testen. 2026-11-12, Kono: Ritual an/aus und Durchlauf (5 Jahre) funktionieren.

### T-059 Heil-JE erst mit Quinine, Balken laufen (VA-046)
- **Schritte:** Neue Kampagne als Silvermoon. Prüfen, ob Quinine schon erforscht ist (Technologie-Baum, Gesellschaft Ära 2). Falls nicht: Journal ansehen, dann per Konsole `research quinine`, 1–2 Monate laufen lassen. Ein Ritual starten, 3 Monate vorspulen.
- **Erwartet:** Ohne Quinine ist „Curing the Path of Destruction“ nicht aktiv (höchstens als mögliches JE mit Quinine-Bedingung im Tooltip); spätestens einen Monat nach der Forschung wird es aktiv. Balken heißen nur noch nach der Region. Fehlt der Ritual Site Mana oder Papier (z. B. als Deathholme ohne Mana im Markt): Status „Stalled: … lacks Mana or Paper“, Balken-Tooltip ebenso, Balken steht. Mit voller Versorgung läuft er, auch ohne Mana-Abhängigkeit. Tooltip „Will become invalid if“ zeigt nur „We no longer hold any land on the Dead Scar“. Tooltip von „Stop Ritual“ ohne `BUG:`-Text. Balken der Region steigt jeden Monat um 1. Kein Eintrag `already has a journal entry of type je_va_dead_scar` im error.log.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: Kono 2026-11-01: Test erfolgreich.

### T-055 error.log: Todesschneise heilen (Claude)
- **Schritte:** Nach T-053 und T-054 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `va_dead_scar.txt`, `va_dead_scar_progress_bars.txt`, `va_dead_scar_buttons.txt`, `va_dead_scar_effects.txt`, `va_dead_scar_buildings.txt`, `va_dead_scar_production_method*.txt`, `va_dead_scar_events.txt`, `va_building_groups.txt`, `scope:journal_entry`, `scripted_bar_progress`, `create_building`, `remove_building`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Claude: keine Zeilen zu Todesschneise heilen.

## Runde 12 – Korridor nach Tranquillien (Stand 2026-10-31)

Ticket: VA-047. Lint vor Freigabe: 0 neue Fehler (2026-10-31).

### T-056 Korridor-JE und Marktzugang vorher (VA-047)
- **Schritte:** Kampagne als Silvermoon. Journal → Historische Inhalte. Dann Markt-Ansicht bzw. State Tranquillien (Tranquilliens Teil) → Marktzugang notieren.
- **Erwartet:** „The Road to Tranquillien (AI WRITTEN)“ aktiv, ein Balken „Logistics Operation“ 0/18, Schalter „Launch Logistics Operation“, Status „No operation is underway“. Beschreibung nennt Kosten, 18 Monate, Krieg als Alternative. Marktzugang Tranquillien notieren (Vergleich in T-057).
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: dauert recht lange, ist aber ok; Märkte verbunden, Folge-JE kommt.

### T-057 Drei Etappen per Logistik (VA-047)
- **Schritte:** Schalter drücken. Haushalt (−100.000), Bürokratie und Autorität prüfen. 18 Monate vorspulen, Karte der Geisterlande ansehen. Zweimal wiederholen. Einmal während einer Operation einen Krieg haben (oder per Konsole erklären) und Balken beobachten.
- **Erwartet:** Modifier „Logistics Operation“ (−25/−25), Schalter verschwindet solange. Balken +1/Monat, steht im Krieg (Status „stalls“). Bei 18: Popup „A Stretch of Road Secured“, Provinzen wechseln von Deathholme zu Silvermoon (Etappe 1: xFDDA71, x186841; Etappe 2: Bergprovinzen xCEF332, x2FC0FD; Etappe 3: xD536B6 bis an Tranquillien), die Provinzen der Todesschneisen-Grafik bleiben bei Deathholme, Balken wieder 0. Nach Etappe 3 Popup „The Road Is Open“, JE erfüllt, Modifier „The Road to Tranquillien“. Pops und Gebäude in den neuen Teil-States plausibel (nicht verdoppelt, nicht verschwunden). Marktzugang Tranquillien besser als in T-056.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: richtige Provinzen, JE funktioniert.

### T-058 error.log: Korridor (Claude)
- **Schritte:** Nach T-056 und T-057 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `va_silvermoon_corridor_*.txt`, `VA_silvermoon.txt`, `va_silvermoon_events.txt`, `va_silvermoon_modifiers.txt`, `va_global_quel_thalas.txt`, `set_owner_of_provinces`, `p:x`, `cd:DEATHHOLME`, `va_corridor_stage`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Claude: 76 Zeilen va_silvermoon_corridor_buttons.txt:8 (visible), alle in 3 Sekunden beim Laden mit ungültigem Land-Scope (Country 4294967295) – UI-Auswertung vor dem Länder-Setup, nicht aus dem Script heraus; sonst sauber. Beobachten.

## Runde 13 – Wretched (Stand 2026-11-03)

Ticket: VA-021. Lint vor Freigabe: 0 neue Fehler (2026-11-01, Schritt 1: 2026-11-03). T-060 bis T-062 prüfen die Grundfassung, T-064 bis T-067 Schritt 1 (Bedrohung, Raub-Events, Bruderkrieg).

### T-060 Wretched-JE und Mana-Pakt (VA-021)
- **Schritte:** Neue Kampagne als Silvermoon. Journal → Historische Inhalte. Per Konsole `play WRETCHED_BLOODELFES` kurz die Modifier der Wretched ansehen, zurück zu Silvermoon. Schalter „Offer a Mana Pact“ drücken. Danach einmal mit `play WRETCHED_BLOODELFES` vor dem Drücken testen, dass das Pakt-Event dort mit zwei Optionen erscheint (oder die KI entscheiden lassen).
- **Erwartet:** „The Wretched (AI WRITTEN)“ aktiv, Balken „Healing the Wretched“ 0/60, nur der Schalter „Offer a Mana Pact“ sichtbar, Status „still go their own way“. Wretched haben „Wretched Addiction“. Nach dem Drücken: bei Annahme Popup „The Wretched Accept“, Wretched sind Protektorat von Silvermoon, Status „under our protection“, statt des Pakt-Schalters „Absorb the Wretched“ und „Begin the Healing“. Bei Ablehnung Popup „The Wretched Refuse“, Schalter für ein Jahr gesperrt (Tooltip „not offered a pact in the last year“).
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03, Kono: Pakt, Protektorat und Jahressperre funktionieren.

### T-063 error.log: Wretched (Claude)
- **Schritte:** Nach T-060 bis T-062 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `va_silvermoon_wretched_*.txt`, `va_wretched_modifiers.txt`, `va_wretched_events.txt`, `VA_silvermoon.txt`, `va_global_quel_thalas.txt`, `va_wretched_suitor`, `annex_with_incorporation`, `WRETCHED_BLOODELFES`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03, Claude: error.log (20:28) ohne Zeilen zu Wretched-Dateien.

### T-064 Bedrohung und Ansprüche (VA-021, Schritt 1)
- **Schritte:** Neue Kampagne als Silvermoon. JE „The Wretched“ öffnen, Balken ansehen. Diplomatie/Karte: Ansprüche auf Ruins of Silvermoon, Sunsail Anchorage, Sunstrider Isle. 3 Monate laufen lassen und den Tooltip des Balkens „Wretched Threat“ ansehen.
- **Erwartet:** Zwei Balken: „Wretched Threat“ (rot, Start 40/100) und „Healing the Wretched“ (0/60). Silvermoon hat Ansprüche auf die drei Wretched-State-Regionen. Bedrohung steigt um 1 je Monat, solange Mana im Markt der Wretched knapp ist (Tooltip „The Wretched are free and starving for Mana“); sonst bleibt sie stehen. JE-Text erwähnt Bedrohung und Ansprüche.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: zwei Balken, Bedrohung steigt monatlich, Events wirken, Balken steigen und fallen.

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

## Runde 13 – Wretched (Stand 2026-11-03)

Ticket: VA-021. Lint vor Freigabe: 0 neue Fehler (2026-11-01, Schritt 1: 2026-11-03). T-060 bis T-062 prüfen die Grundfassung, T-064 bis T-067 Schritt 1 (Bedrohung, Raub-Events, Bruderkrieg).

### T-061 Weg 1: Eingliedern (VA-021)
- **Schritte:** Spielstand nach T-060 (Wretched sind Protektorat) sichern. „Absorb the Wretched“ drücken, einen Monat laufen lassen. Karte, Modifier von Silvermoon und States Sunstrider Isle, Ruins of Silvermoon, Sunsail Anchorage ansehen.
- **Erwartet:** Popup „The Wretched Absorbed“, Wretched verschwinden, ihre States gehören Silvermoon (eingegliedert, nicht „unincorporated“). Silvermoon hat „The Wretched Absorbed“ (10 Jahre, Legitimität −10, Radikale aus Bewegungen +25 %). Die drei States haben „Wretched Addicts“ (10 Jahre). JE erledigt.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Absorbed, Legitimität, Radikale, Addicts, 10-Jahres-Malus, JE erledigt. (Stand war 2 Monate vor Heil-Ende, siehe Frage bei T-073.)

### T-062 Weg 2: Heilen (VA-021)
- **Schritte:** Gesicherten Stand aus T-061 laden. „Begin the Healing“ drücken. Staatskasse, Bürokratie, Mana-Preis im Markt der Wretched ansehen. 3 Monate laufen lassen. Mana knapp machen oder abwarten, ob der Balken stillsteht; dann bis 60 vorspulen (Konsole oder lange laufen lassen).
- **Erwartet:** Sofort −100.000, Modifier „Healing the Wretched“ (Bürokratie −25), danach jeden Monat −10.000. Balken +1/Monat; im Krieg oder bei Mana-Knappheit im Markt der Wretched Stillstand mit Status- und Balken-Text. Schalter „Begin the Healing“ verschwindet, „Absorb“ bleibt. Bei 60: Popup „The Wretched Healed“, Annexion, Modifier „The Wretched Restored“ (Prestige +25), **keine** „Wretched Addicts“, kein „Absorbed“. JE erledigt.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Bürokratiekosten da, Heilung durchgelaufen, automatische Annexion, „Quel'Thalas Is Whole Again“, „The Wretched Restored“ mit Prestige.

## Runde 14 – Namen der Strategic Regions (Stand 2026-11-03)

Ticket: VA-057. Lint vor Freigabe: 0 neue Fehler (2026-11-03).

### T-068 Regionsnamen auf der Karte (VA-057)
- **Schritte:** Neue Kampagne. Kartenmodus Militär bzw. einen Krieg ansehen (z. B. Thorium Brotherhood gegen Dark Iron), Hauptquartier-Marker und Tooltip einer Strategic Region ansehen. Dazu einige Seeregionen (Flotten-Hauptquartier, Seegebiet anklicken).
- **Erwartet:** Statt `region_searing_gorge` steht „Searing Gorge“, ebenso z. B. „Eversong Woods“, „The Great Sea“, „Frozen Sea Passage I“ (Namen von Kono abgenommen, ohne AI-Marker). Kein Regions-Key mehr roh sichtbar.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03, Kono: „Eversong Woods HQ“ sichtbar.

### T-069 error.log: Regionsnamen (Claude)
- **Schritte:** Nach T-068 Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `va_strategic_regions_l_english.yml` oder doppelten `region_`-Keys.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03, Claude: error.log (20:48) ohne Zeilen zu `va_strategic_regions_l_english.yml`; nur bekannte Erde-Regionen aus Vanilla-Effekten.

### T-070 Soldaten an Front und in Schlachten (VA-058)
- **Schritte:** Nachdem `gfx/map/army_dioramas`, `front_entities`, `fleet_dioramas`, `fleet_entities` und `map_modes` im Repo und in `mod\warcraft` gelöscht sind: Kampagne laden bzw. neu starten, einen Krieg mit Front und Schlacht nah heranzoomen (z. B. Silvermoon gegen Wretched), dazu eine Seeschlacht oder Flotte.
- **Erwartet:** 3D-Soldaten an der Front und im Schlacht-Diorama wie in Vanilla, Formations-Symbole sichtbar; Flotten mit Schiffen. error.log ohne Zeilen zu `fleet_dioramas`, `army_dioramas`, `front_entities`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-03, Kono: Formations-Marker mit Flaggen da (nach Löschen von `map_modes` und den Dioramen-Kopien). error.log ohne `fleet_dioramas`-Zeilen.

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

## Runde 18 – Todesschneise als Gebäude, Test East Sanctum (Stand 2026-11-04)

Ticket: VA-062. Lint 26: 0 neue Fehler (2026-11-04). Vorher nach `mod\warcraft` kopieren: `common/terrain/`, `common/terrain_manipulators/` (neu), `common/buildings/va_dead_scar_buildings.txt`, `common/building_groups/va_building_groups.txt`, `common/production_method_groups/va_dead_scar_production_method_groups.txt`, `common/production_methods/va_dead_scar_production_methods.txt`, `common/scripted_effects/va_dead_scar_effects.txt`, `common/scripted_effects/va_quel_thalas_effects.txt`, `gfx/map/masks/manifest.json`, `gfx/map/masks/mask_dynamic_va_dead_scar.png` (neu), `gfx/map/terrain/mask_devastation_mud_01.png`, `localization/replace/english/va_dead_scar_regions_l_english.yml`, `localization/replace/english/va_terrain_l_english.yml`.

### T-086 Schneise in East Sanctum kommt vom Gebäude (VA-062)
- **Schritte:** Kampagne starten, East Sanctum und eine Nachbarregion (z. B. Tranquillien) heranzoomen; State-Fenster East Sanctum öffnen; Provinz-Tooltip auf der Schneise.
- **Erwartet:** Kein Absturz. In East Sanctum ist die Schneise sichtbar wie vorher (Schlammtextur, kaum Bäume), in den anderen Regionen unverändert (noch fest gemalt). Im State-Fenster „Dead Scar (AI WRITTEN)“ mit Stufe 5. Gelände der Schneisen-Provinzen ggf. „Dead Scar (AI WRITTEN)“. error.log: keine Zeilen zu `mask_dynamic_va_dead_scar`, `va_dead_scar_land`, `building_va_dead_scar`, `va_terrain_manipulators.txt`; die `checksum no longer match`-Warnung ist harmlos.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono (alter Spielstand): Schneise komplett sichtbar.

### T-087 Schneise in East Sanctum schrumpft mit der Heilung (VA-062)
- **Vorher (2026-11-04):** zusätzlich `common/terrain/va_terrain.txt` (Material wieder Schlamm), `common/scripted_effects/va_quel_thalas_effects.txt` und `va_dead_scar_effects.txt` (50 Stufen) kopieren; neue Kampagne. Nach dem ersten Abschnitt (4 Monate) Claude Bescheid geben (debug.log).
- **Zuerst prüfen:** Schlamm deckt jetzt die ganze frühere Schneise in East Sanctum, auch x1C0EED und xF017F6.
- **Schritte:** Als Besitzer von East Sanctum (Konsole `research quinine` falls nötig) das Ritual in East Sanctum starten, 20 Monate laufen lassen; alle 4 Monate Stufe im State-Fenster und die Karte ansehen.
- **Erwartet:** Stufe 50 → 40 → 30 → 20 → 10 (seit 2026-11-04), die Schlammfläche wird jeweils kleiner (Provinzen fallen nacheinander weg). Nach der Heilung ist das Gebäude weg und keine Schneise mehr sichtbar; darunter der normale Boden. error.log ohne Zeilen zu `va_dead_scar_set_level_effect`, `create_building`, `remove_building`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-04 Schrumpfen laut debug.log korrekt (50→10), Karte zeigt es erst nach Speichern/Laden – Engine-Verhalten, in Vanilla genauso (Kono). x1C0EED/xF017F6 nie umgewandelt (offen in VA-062).

### T-088 Schneise über die Bergbau-Maske (VA-062)
- **Vorher:** nach `mod\warcraft` kopieren: `gfx/map/masks/mask_dynamic_mining.png`, `common/terrain_manipulators/va_terrain_manipulators.txt`, `common/terrain/va_terrain.txt`, `common/buildings/va_dead_scar_buildings.txt`, `common/scripted_effects/va_quel_thalas_effects.txt`. In `mod\warcraft` `gfx/map/masks/mask_dynamic_va_dead_scar.png` löschen (gibt es im Repo nicht mehr).
- **Schritte:** Neue Kampagne, East Sanctum heranzoomen; Gelände-Tooltip einer Provinz, auf der früher die Schneise lag.
- **Erwartet:** Auf der früheren Schneise in East Sanctum erscheinen Felder (Test-Material statt Schlamm), Gelände „Dead Scar (AI WRITTEN)“. Keine Felder außerhalb der Schneise durch das Gebäude. debug.log: „VA-062: Dead Scar angelegt“.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-04 Felder in Schneisenform sichtbar (Kono). Danach Material auf Schlamm zurückgestellt.

### T-089 Knopf „Refresh Terrain (TEST)“ zeichnet dynamisches Terrain neu (VA-062)
- **Vorher:** `gui/va_terrain_refresh.gui` und `gui/ingame_hud.gui` (Override, 2026-11-04 nachgereicht: eigenes Fenster erschien nicht) nach `mod\warcraft` kopieren.
- **Schritte:** Kampagne laden, oben rechts den Knopf „Refresh Terrain (TEST)“ suchen. Ritual East Sanctum laufen lassen, bis die Schneise laut State-Fenster kleiner ist (oder in Vanilla-Art Farmen bauen), dann Knopf drücken, einige Sekunden warten.
- **Erwartet:** Knopf sichtbar. Nach dem Klick passt sich die Bodentextur ohne Neuladen an. error.log: keine Zeile zu `va_terrain_refresh.gui` oder `UpdateDynamicTerrainInAllProvinces` (Meldung „unknown function“ o. ä. hieße: Funktion nur im Map-Editor).
- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-11-04 Knopf ohne Wirkung, error.log ohne Meldung (Kono). Knopf und Override `gui/ingame_hud.gui` wieder entfernt. 2026-11-12, Claude: entfällt, Knopf entfernt.

### T-090 Mana-Icon (VA-027)
- **Vorher:** `common/goods/va_goods.txt` und `gfx/interface/icons/goods_icons/va_mana.dds` nach `mod\warcraft` kopieren.
- **Schritte:** Kampagne laden, Markt-/Güterübersicht öffnen, Gut „Mana“ suchen (z. B. Silbermond, Ley Line Tap).
- **Erwartet:** blaue Mana-Kugel statt Strom-Blitz, auch klein in Gebäude-/Bedarfslisten erkennbar. error.log: nichts zu `va_mana.dds`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Mana-Icon vorhanden, sieht gut aus.

## Runde 19 – Patch 1.15 (Stand 2026-11-06)

Ticket: VA-063. Lint alle Regionen: 0 neue Fehler (2026-11-06). Vorher nach `mod\warcraft` kopieren: `common/travel_network/naval_network.txt` (neu), `common/flag_definitions/00_flag_definitions.txt` (neu), neu erzeugt aus Vanilla 1.15: `common/achievements/*.txt`, `common/government_types/01_monarchies.txt`, `01_regencies.txt`, `01_social_monarchies.txt`, `05_council_republics.txt`, `common/political_movements/03_pan_national_movements.txt`, `common/power_bloc_names/00_power_bloc_names.txt`, `common/buildings/08_monuments.txt`, `10_canals.txt`.

### T-094 Kupfer-Vorkommen in EK und Kalimdor (VA-064)
- **Vorher:** nach `mod\warcraft` kopieren: `map_data/state_regions/23_va_north_kalimdor.txt`, `24_va_center_kalimdor.txt`, `26_va_north_eastern_kingdoms.txt`, `27_va_center_eastern_kingdoms.txt`, `28_va_south_eastern_kingdoms.txt`. Lint 23/24/26/27/28: 0 neue Fehler.
- **Schritte:** Kampagne starten. State-Fenster von Gol'Bolar-Steinbruch (Dun Morogh), Thelsamar, Todesminen, Drygulch Ravine öffnen und die Ressourcen ansehen; Kartenmodus Ressourcen bzw. Bau-Menü „Kupfermine“ als Ironforge oder Orgrimmar (nach `shaft_mining`, Konsole `research shaft_mining`). Nach einigen Jahren Marktpreis Kupfer ansehen.
- **Erwartet:** Kupfermine in 62 States baubar (Gol'Bolar 24, Thelsamar/Todesminen 20, …), andere Ressourcen unverändert. Kupfer nicht dauerhaft auf Höchstpreis. error.log ohne Zeilen zu `building_copper_mine` oder zu den fünf State-Dateien.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-06 „Kupfer passt“ (Kono).

### T-091 Leeres Seewege-Netz (VA-063)
- **Schritte:** Kampagne starten. Eine Flotte (z. B. Kul Tiras oder Stormwind) über mehrere Seezonen schicken; eine Armee per Schiff auf einen anderen Kontinent verlegen (Marine-Invasion oder Truppenverlegung).
- **Erwartet:** Kein Absturz. error.log ohne `naval node`, `Harbor node … no port node` und ohne die ~3.300 `Referencing non-existent province!` mit leerem Dateinamen (Gesamtzahl deutlich unter 16.000). Offen ist, ob Schiffe ohne Netz noch Wege finden: Wenn Flotten nicht losfahren oder Seewege fehlen, Fehler notieren, dann baut Claude einen eigenen Generator.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-06 error.log 4.249 beim Start, 4.307 nach 1 Jahr (vorher ~16.000); naval-/harbor-Zeilen weg. Neu: ~150× `hq.cpp: Failed to find a travel position for HQ … no coastal state … has a port travel position` → Häfen haben ohne Netz keine Seeposition, Seefahrt vermutlich kaputt. 2026-11-06 Kono: in Silvermoon Flotte (2 Fregatten, 1 Großkampfschiff) gebaut, Truppentransport funktioniert, Truppen bleiben am Ziel → OK; die hq.cpp-Meldungen bleiben als Schönheitsfehler offen (VA-063).

## Runde 20 – Todesschneise ganz, Deathholme-Fluch (Stand 2026-11-06)

Ticket: VA-062. Lint 26: 0 neue Fehler. Nach `mod\warcraft` kopieren: `gfx/map/masks/mask_dynamic_mining.png`, `common/journal_entries/va_dead_scar.txt`, `common/scripted_buttons/va_dead_scar_buttons.txt`, `common/scripted_progress_bars/va_dead_scar_progress_bars.txt`, `common/scripted_effects/va_dead_scar_effects.txt`, `common/scripted_effects/va_quel_thalas_effects.txt`, `common/scripted_triggers/va_quel_thalas_triggers.txt`, `common/script_values/va_dead_scar_values.txt` (neu), `common/static_modifiers/va_quel_thalas_modifiers.txt`, `common/on_actions/va_on_actions_quel_thalas.txt`, `common/history/global/va_global_quel_thalas.txt`, `common/building_groups/va_building_groups.txt`, `localization/replace/english/va_dead_scar_regions_l_english.yml`. In `mod\warcraft` löschen: `gui/` (Test-Knopf). Neue Kampagne. Karte zeigt Änderungen erst nach Speichern/Laden.

### T-096 Schneise in allen sechs Regionen, auch x1C0EED und xF017F6 (VA-062)
- **Schritte:** Kampagne starten, die sechs Regionen ansehen; Gelände-Tooltip in x1C0EED und xF017F6 (East Sanctum); Infrastruktur eines Schneisen-States.
- **Erwartet:** Schlamm auf der ganzen Schneise in allen sechs Regionen, auch in den beiden Provinzen (Gelände „Dead Scar (AI WRITTEN)“). Kein Schlamm in Silvermoon City. Infrastruktur nicht mehr durch „Dead Scar“ belegt. error.log ohne Zeilen zu `va_dead_scar`, `va_terrain`, `va_building_groups`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-06 16 Provinzen fehlten (Farmen belegten sie). Nachbesserung siehe T-098. Nachtest 2026-11-06 (Kono): alle sechs Regionen mit Gelände und Modifier, Untote ohne Lebenden-Malus.

### T-097 Deathholme: Fluch-Buff je Region, Heilung bei null (VA-062)
- **Schritte:** Konsole `observe`/`play DEATHHOLME`: Landes-Modifier ansehen. Als Silvermoon im JE prüfen, dass es keinen Deathholme-Balken/-Schalter mehr gibt. Eine Region heilen (Ritual 20 Monate), Modifier erneut ansehen. Zum Schnelltest alle fünf Regionen heilen (oder per Konsole), dann Deathholme ansehen (nach Speichern/Laden).
- **Erwartet:** Start: „Tide of the Scourge (AI WRITTEN)“ mit 5× Werten (Angriff +20 %, Verteidigung +40 %, Moral-Erholung +25 %, Durchsatz +30 %; seit 2026-11-06). Nach jeder geheilten Region ein Fünftel weniger, Schneise in Deathholme 10 Stufen kleiner. Bei null: Modifier weg, Deathholme ohne Schneisen-Modifier und ohne Schneise, JE „Curing the Path of Destruction“ erfüllt. Länder, die nur Deathholme-States haben, bekommen das Heil-JE nicht. error.log ohne Zeilen zu `va_update_deathholme_scourge_effect`, `va_dead_scar_cursed_regions`, `va_deathholme_scourge_tide`, `on_monthly_pulse`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: Nachtest 2026-11-06 (Kono): Buff vorhanden, sinkt nach Heilung einer Region um den Betrag.

### T-098 Fehlende Schneisen-Provinzen nachgebessert (VA-062)
- **Vorher:** `gfx/map/masks/mask_dynamic_mining.png`, `mask_dynamic_farmland.png`, `mask_dynamic_forestry.png`, `common/static_modifiers/va_quel_thalas_modifiers.txt` nach `mod\warcraft`; neue Kampagne.
- **Schritte:** Die 16 Provinzen aus T-096 ansehen (Sunwell x4E496D x3E6CAE xB6E6AB x21A7AB xEB9D1D, Ruins x6DAC1E, East x1C0EED xF017F6, Tranquillien x537223 x1F97B1, Deathholme x3AAD13 xF29779 x142D60 xA28A0D x203FF1 x9A04F7), Gelände-Tooltip.
- **Erwartet:** Alle mit Schlamm und Gelände „Dead Scar (AI WRITTEN)“, keine Felder mehr auf der Schneise. Farmen der States erscheinen daneben. Fehlt eine Provinz weiter: Gelände im Tooltip notieren (Farmland/Mining/…).
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-06 sechs Provinzen fehlen weiter (x4E496D, x3E6CAE, x6DAC1E Bergbau, x3AAD13, xF29779, x142D60). Nachbesserung T-099. Nachtest 2026-11-06 (Kono): 16 Provinzen mit Schneise.

### T-099 Vorrang vor Bergbau und mehr Stufen (VA-062)
- **Vorher:** In `mod\warcraft` `common/terrain_manipulators/va_terrain_manipulators.txt` **löschen** und `00_va_terrain_manipulators.txt` kopieren; dazu `common/scripted_effects/va_quel_thalas_effects.txt`, `va_dead_scar_effects.txt`, `common/buildings/va_dead_scar_buildings.txt`. Neue Kampagne.
- **Schritte:** x4E496D, x3E6CAE (Sunwell), x6DAC1E (Ruins), x3AAD13, xF29779, x142D60 (Deathholme) ansehen, Gelände-Tooltip; Leyline-Tap in Sunwell Plateau noch mit Bergbau-Optik?
- **Erwartet:** Alle sechs mit Schlamm und Gelände „Dead Scar (AI WRITTEN)“. Bleibt eine mit „Mining“, entscheidet die Lade-Reihenfolge nicht; bleibt der Farm-Hub x4E496D leer, sind Hubs ausgenommen. Gelände je Provinz notieren.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-06 fast alles OK; x2B1415 zu schwach (nachgebessert), x6DAC1E weiter „Mining“ (Quelle offen). Nachtest 2026-11-06 (Kono): Leyline-Taps ohne Bergbau-Optik, alles Schlamm.

### T-100 Leyline-Tap ohne Bergbau-Optik, Schneise vollständig (VA-062)
- **Vorher:** `common/buildings/va_mana_buildings.txt`, `gfx/map/masks/mask_dynamic_mining.png`, `mask_dynamic_farmland.png`, `mask_dynamic_forestry.png` nach `mod\warcraft`; neue Kampagne.
- **Schritte:** x2B1415 und x21A7AB (Sunwell), x6DAC1E (Ruins, Silvermoons Teil) ansehen; Gelände-Tooltip. Leyline-Tap in Sunwell bauen/ansehen.
- **Erwartet:** Alle drei mit Schlamm und „Dead Scar (AI WRITTEN)“, kein „Mining“ mehr. Leyline-Taps funktionieren wie bisher, nur ohne Tagebau auf der Karte. error.log ohne Zeilen zu `va_mana_buildings.txt`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-06 x6DAC1E weiter Mine (Kohlemine der Wretched). Nachbesserung T-101. Nachtest 2026-11-06 (Kono): sieht gut aus.

### T-104 Ruins of Silvermoon ohne Start-Kohlemine (VA-062)
- **Vorher:** `common/history/buildings/26_north_eastern_kingdoms.txt`, `gfx/map/masks/*`, neu `tools/mapeditor/mask_painter/` nach `mod\warcraft`; neue Kampagne.
- **Schritte:** State Ruins of Silvermoon (Wretched-Teil): Gebäudeliste. x6DAC1E ansehen, speichern/laden, Gelände-Tooltip. Map-Editor öffnen: zeigt die Bergbau-Maske jetzt die Schneise?
- **Erwartet:** Keine Kohlemine beim Start; x6DAC1E „Dead Scar (AI WRITTEN)“. Editor zeigt unsere Masken statt der Erdmasken. error.log ohne neue Zeilen zu `26_north_eastern_kingdoms.txt`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Ruins of Silvermoon ohne Kohle.

### T-105 Keine Schneise außerhalb der Schneise (VA-062)
- **Vorher:** `gfx/map/masks/mask_dynamic_*.png` und `tools/mapeditor/mask_painter/` nach `mod\warcraft`; neue Kampagne.
- **Schritte:** West Sanctum x4BFDA4 und x5B9E0E ansehen (speichern/laden), Stichprobe xDD304F/xC63C98 (Ruins), xA9ACB2 (East Sanctum), xD6BF4D (Tranquillien). Schneise selbst kurz überfliegen.
- **Erwartet:** Diese Provinzen ohne Schlamm und ohne „Dead Scar (AI WRITTEN)“; die Schneise selbst unverändert.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: nach Laufzeit und Speichern/Laden weiterhin korrekt.

### T-106 Texte: Schneise stärkt Deathholme (VA-062)
- **Vorher:** `localization/replace/english/va_dead_scar_regions_l_english.yml`, `va_silvermoon_l_english.yml` nach `mod\warcraft`.
- **Schritte:** Als Silvermoon JE „Curing the Path of Destruction“ und „Drive Out Deathholme“ lesen; eine Region heilen (Event „The Scar Recedes“), per Konsole `event dead_scar_events.2` ansehen.
- **Erwartet:** Alle vier Texte erwähnen, dass die Schneise Deathholme stärkt bzw. die Heilung es schwächt, mit „(AI WRITTEN)“; keine Loc-Keys im Klartext, error.log ohne Zeilen zu den beiden Dateien.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Tide of the Scourge bei Deathholme, sinkt beim Heilen durch Silvermoon.

### T-107 Gebäude-Icon Ley Line Tap (VA-027)
- **Vorher:** `common/buildings/va_mana_buildings.txt`, `gfx/interface/icons/building_icons/va_ley_line_tap.dds` nach `mod\warcraft`.
- **Schritte:** Sunwell Plateau: Gebäudeliste und Bau-Menü, Ley Line Tap ansehen (groß und klein, z. B. Outliner/Tooltip).
- **Erwartet:** Konos Bild statt Kohlemine, scharf, transparente Ecken; error.log ohne Zeilen zu `va_ley_line_tap.dds`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Gebäude-Icon sieht gut aus.

### T-101 Minen weichen der Schneise aus; Forst/Bergbau in EK (VA-062, VA-061)
- **Vorher:** `gfx/map/masks/mask_dynamic_mining.png`, `mask_dynamic_forestry.png`, `mask_dynamic_farmland.png` nach `mod\warcraft`; neue Kampagne.
- **Schritte:** x6DAC1E (Ruins of Silvermoon) ansehen, einige Monate laufen lassen (Kohlemine der Wretched), speichern/laden. Stichproben in EK: Holzfäller (z. B. Elwynn) und Minen zeigen Rodung/Tagebau nahe ihrer Hubs.
- **Erwartet:** x6DAC1E mit „Dead Scar (AI WRITTEN)“; Kohlemine zeigt Tagebau am Mine-Hub bzw. in den Bergen, nicht auf der Schneise. In EK mehr Rodungen und Tagebaue als vorher, keine auf der Schneise.
- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-11-06 x6DAC1E weiter Mine (Silvermoons Teil-State hatte keine andere Bergbaufläche). Nachbesserung T-102. Nachtest 2026-11-06 (Kono, Kohlemine per Fastbuild): Tagebau liegt woanders, gut. Aber West Sanctum x4BFDA4 und x5B9E0E zeigen Schneise – das sind die Ausweichflächen aus T-102 (Schneisen-Gebäude wandelt jede Bergbau-Fläche im State um). Nachbesserung T-105. 2026-11-12, Claude: erledigt durch T-104 (OK).

### T-102 Ausweichflächen je Besitzer-Teil (VA-062)
- **Vorher:** `gfx/map/masks/mask_dynamic_mining.png` (und die beiden anderen Masken) nach `mod\warcraft`; neue Kampagne.
- **Schritte:** Wie T-101: x6DAC1E nach Bau der Kohlemine ansehen (speichern/laden). Tagebau soll auf xDD304F oder xC63C98 liegen.
- **Erwartet:** x6DAC1E „Dead Scar (AI WRITTEN)“, Tagebau auf einer der Ausweich-Provinzen.
- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-11-06 x6DAC1E weiter Kohlemine. Nachbesserung T-103. 2026-11-12, Claude: erledigt durch T-104 (OK).

### T-103 Schneise schwächer als Minen-Ausweichflächen (VA-062)
- **Vorher:** `gfx/map/masks/mask_dynamic_mining.png` (und die beiden anderen Masken) nach `mod\warcraft`; neue Kampagne.
- **Schritte:** x6DAC1E (Ruins of Silvermoon) ansehen, einige Monate laufen lassen bis die Kohlemine steht, speichern/laden, Gelände-Tooltip. Stichprobe: xCCFE72, x4E852C (Schneise im Wretched-Teil) ebenfalls ansehen.
- **Erwartet:** Alle drei „Dead Scar (AI WRITTEN)“. Tagebau der Kohlemine auf Mine-Hub x33B5DA, einem Berg oder xDD304F/xC63C98.
- **Ergebnis:** [ ] OK  [x] Fehler – Notiz: 2026-11-06 x6DAC1E weiter Kohlemine. Maskenstärke ist nicht die Ursache. Nachbesserung T-104. 2026-11-12, Claude: erledigt durch T-104 (OK).

## Runde 22 – Quel'Thalas: Bevölkerung und Figuren (Stand 2026-11-10)

Tickets: VA-049, VA-024, VA-016, VA-066, VA-021. Lint vor Freigabe: 0 neue Fehler (2026-11-10, `--regions 26`).

### T-116 Gemischte Bevölkerung in Quel'Thalas (VA-049, VA-024)
- **Schritte:** Neue Kampagne. Pops ansehen in Silvermoon City, Sun's Reach, Magisters' Terrace, Sunwell Plateau, Tranquillien, Deathholme, Zul'Aman, Tor'Watha; Nahrungs- und Arbeitslosen-Lage in Silvermoon City nach einem Jahr.
- **Erwartet:** Silvermoon City mit Sin'dorei, Quel'dorei, Goblins, Dalaraner, Verlassenen, Orcs (Orgrimmari) und Darkspear-Trollen. Quel'Danas statt je 10.000 nun 180.000 / 120.000 / 60.000. Ghostlands mit Banshees und Zombies, Tranquillien mit Verlassenen, Amani mit Dire Trolls. Gesamtzahl je State sonst wie vorher, keine neue Hungersnot.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Dalaranian, Forsaken, Ogrimari, Goblin, Dschungeltroll sichtbar; Forsaken passt zur Lore. Ogrimari später anpassen. Sprache „Elven“ und Tradition „Magical Lowlands“ ohne Text → Loc-Key korrigiert, Rest der fehlenden Namen VA-069.

### T-117 Historische Figuren (VA-016, VA-066, VA-022)
- **Schritte:** Kampagne aus T-116. Silvermoon: Herrscher, General, IG-Anführer Intelligenzija und Fromme ansehen. Deathholme und Zul'Jarra: Herrscher und Fromme. Als Zul'Jarra `event amani_loa_events.6`, Option „Give them Malacrass.“
- **Erwartet:** Silvermoon: Lor'themar Theron (Herrscher), Halduron Brightwing (General), Rommath the Grand Magister, Liadrin the Blood Matriarch. Tranquillien: Auriferous Dame (Herrscherin), Mavren the High Executor (General, Verlassener). Deathholme: Dar'Khan Drathir. Zul'Jarra: Zul'jin the Warlord, Malacrass the Hex Lord. Elfen mit Lebensdauer-Eigenschaft wie T-021. Nach der Option ist Malacrass tot.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Lor'themar, Halduron, Rommath (Intelligenzija), Liadrin (Fromme), Auriferous (Princess), Darkhan Drathir, Mavren, Zul'jin sichtbar; Lebensdauer-Traits passen. Lor'themar trägt „König“ → VA-068.

### T-119 Gebäude Quel'Danas und KI-Gewicht Ley Line Tap (VA-019, VA-024)
- **Schritte:** Kampagne aus T-116. Gebäudeliste von Sun's Reach, Magisters' Terrace, Sunwell Plateau ansehen; Ley Line Tap in Sunwell öffnen (beide PM-Gruppen). Zehn Jahre als Beobachter laufen lassen: baut die KI in Silvermoon neue Ley Line Taps?
- **Erwartet:** Sun's Reach: Reisfarm 1, Fischerei 1; Magisters' Terrace: Reisfarm 1; Sunwell: Ley Line Tap 1 mit Focus Crystals und No Attunement. Die KI erweitert bzw. baut Taps (vorher ohne `ai_value`).
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: KI baut Ley Line Taps, sehr langsam, aber stetig.

### T-121 Nachbesserung nach Kono-Test 12.11.: Hafen, Nahrung, Pops (VA-024, VA-049)
- **Schritte:** Neue Kampagne als Silvermoon (ohne Annex All). Sun's Reach, Magisters' Terrace, Sunwell Plateau: Marktzugang. Tranquillien und Sanctum of Sun: Nahrungspreise und Hungersnot nach 1–2 Jahren. Pops in Silvermoon City, Ghostlands, Zul'Aman, Dawnstar Spire, Sanctum of Sun ansehen.
- **Erwartet:** Sun's Reach hat Hafen 1, alle drei Insel-States am Markt (sonst Insel-States nicht über Land verbunden → Claude melden). Tranquillien: Roggenfarm 2 im eigenen State, 1 im Sanctum; Außenposten: Roggenfarm 1, Baumwolle 1, ohne Färberei und Verwaltung (Kono 2026-11-12), nur noch rund 35.000 Nachtelfen, Gebäude weitgehend besetzt; keine Hungersnot. Pop-Zahlen krumm. Banshees in den Ghostlands rund drei Viertel, in Deathholme Zombies stärker als anderswo. Elfen-Sklaven in allen Troll-States, Zul'Aman mit Sin'dorei- und Quel'dorei-Sklaven. Goblins nur noch in Silvermoon City.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Quel'Danas-Inseln im gemeinsamen Markt, Roggenfarm Tranquillien, Nachtelfen passen, auch nach längerem Lauf keine Hungersnot.

### T-122 Bürokratie, Bausektor, Zul'Aman-Wirtschaft (VA-024, VA-049)
- **Schritte:** Neue Kampagne. Bürokratie-Saldo zum Start bei Silvermoon, Deathholme, Zul'Jarra, Wretched, Grimscale Murlocs, Tranquillien. Bauliste der KI nach einem Jahr (Silvermoon: baut sie Ley Line Taps statt nur Verwaltung?). Zul'Aman: Arbeitslose und Sklaven.
- **Erwartet:** Bürokratie aller sechs bei oder über 0 (Werte notieren). Silvermoon Verwaltung 13 + 1 + 1 und Bausektor 2 in Silvermoon City (+1 Farstrider). Deathholme Verwaltung 9, Bausektor 1 (Techs Bureaucracy und Centralization neu). Zul'Jarra Verwaltung 3 mit Horizontal Drawer Cabinets. Zul'Aman ohne Troll-Sklaven, Opium 3, Baumwolle 4, Holz 5; deutlich weniger als 500.000 Arbeitslose.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Bürokratie-Salden passen; Silvermoon leicht im Minus wegen Papiermangel, selbst ausgleichbar.

### T-123 Mana-Grundbedarf je State (VA-019)
- **Schritte:** Neue Kampagne als Silvermoon. Einen Monat laufen lassen (der Bedarf wird monatlich gesetzt). State-Modifier in Silvermoon City und Quel'Danil Lodge ansehen; Mana-Markt: Nachfrage, Angebot, Preis, Mana-Stufe im JE. Vergleich Stormwind (kein Elfenland): unverändert.
- **Erwartet:** States mit Blut- oder Hochelfen tragen „Mana Upkeep (AI WRITTEN)“: 3,0 Mana je 100.000 Elfen, unabhängig von Forschung. Silvermoon gesamt rund 156 zusätzlich, Nachfrage gesamt rund 170. Start-Tap in Sunwell: 2 Stufen Arcane Conduits = 80 Angebot. Ohne Maßnahmen Preis am Maximum, Stufe „Mana Withdrawal“ – gewollt, Gegenmittel in T-124. Werte anpassbar in `common/script_values/va_mana_values.txt`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: Grundbedarf da, passt sich an, JE-Maßnahmen senken ihn.

### T-124 Mana-Maßnahmen im Mana-JE (VA-019)
- **Schritte:** Kampagne als Silvermoon, Mana-JE öffnen. (1) Disenchantment: siehe T-125 (2026-11-12 umgebaut). (2) „Ration Mana“: Lebensstandard −1, Radikale unter Elfen sofort und nach 6 Monaten; Bedarf −25 %; „End Mana Rationing“ beendet, danach 1 Jahr gesperrt. (3) „Drain the Fauna of Sunstrider Isle“ und weitere Regionen: je −15 % für 1 Jahr, State-Modifier „Fauna Drained/Depleted/Recovering“ (zusammen −30 % Agrar, gestaffelt bis 5 Jahre), Schalter je Region 1,5 Jahre gesperrt. Nach 1,5 Jahren erneut aussaugen: zweiter Modifier-Satz kommt dazu, Agrar-Malus stapelt (z. B. −50 % direkt danach). Alles zusammen: Bedarf fällt bis auf 0, nie darunter. Gegenprobe Wretched/Quel'Danil Lodge: nur Regionen im eigenen Besitz sichtbar.
- **Erwartet:** Zahlen wie beschrieben, Texte mit „(AI WRITTEN)“, keine Loc-Keys. KI (Beobachter) nutzt Disenchantment und Fauna bei Scarcity/Withdrawal, Rationierung nur im Entzug.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: KI (Silvermoon) nutzt die Maßnahmen aktiv, in Ruins of Silvermoon alle Fauna-Malusse gleichzeitig – eher aggressiv, bleibt vorerst so. Rest offen. 2026-11-12, Kono: Rationierung und Fauna funktionieren.

### T-125 Disenchantment erzeugt Mana (VA-019)
- **Schritte:** Kampagne als Quel'Danil Lodge (QUEL_DANIL), Mana-JE öffnen, „Disenchantment (AI WRITTEN)“ drücken. Gebäude „Disenchantment Workshop (AI WRITTEN)“ im Hauptstadt-State prüfen (Stufe 1, 100 Arbeiter, PM „Breaking Heirlooms“), Mana-Angebot im Markt nach 1–2 Monaten. Mana Upkeep bleibt unverändert. Ein Jahr weiterlaufen lassen: Werkstatt verschwindet im Monat nach Ablauf, Schalter erst nach 2 Jahren wieder frei. Gegenprobe Silvermoon: Werkstatt in Silvermoon City.
- **Erwartet:** Rund +10 Mana Angebot, sobald die 100 Stellen besetzt sind (Quel'Danil-Bedarf rund 11). Prestige −10 für 2 Jahre. Gebäude nicht baubar/erweiterbar, keine Infrastruktur-Kosten. Texte mit „(AI WRITTEN)“, keine Loc-Keys. error.log ohne Zeilen zu `building_va_disenchantment`, `bg_va_disenchantment`, `pm_heirloom_breaking_building_va_disenchantment`, `va_mana_disenchant_remove_effect`.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono (Quel'Danil, Beobachter): KI drückt den Schalter selbst, Gebäude erscheint, 100 Arbeiter, rund 10 Mana, nach 1 Jahr wieder weg.

### T-126 Silvermoon: weniger Verwaltung (VA-024)
- **Schritte:** Kampagne als Silvermoon, Silvermoon City: Government Administration 10 statt 13 Stufen. Haushalt und Papierbilanz in den ersten Jahren beobachten.
- **Erwartet:** Kein Bankrott durch Papierkosten; Bürokratie darf knapp sein (Startmalus ohnehin vorhanden). Papier-Eigenproduktion (rund 63) deckt den Bedarf annähernd.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono: kein Bankrott, rund +400 zum Start.

### T-128 Wretched greifen bei Bedrohung 100 an (VA-021)
- **Schritte:** Kampagne als Silvermoon, Wretched-JE: Bedrohung auf 100 bringen (laufen lassen ohne Pakt/Mana, oder per Kopfgeld-Fehlschlägen). Im Folgemonat prüfen.
- **Erwartet:** Popup „The Wretched March (AI WRITTEN)“. Wretched starten einen Diplomatic Play „Frenzy of the Wretched (AI WRITTEN)“ um Silvermoons Teil von Ruins of Silvermoon oder Sunsail Anchorage, der zum Krieg wird. Wretched haben drei Modifier „Wretched Frenzy“ (zusammen +30 % Angriff/Verteidigung), nach 6 Monaten zwei, nach 1 Jahr einer, nach 2 Jahren keiner. Bedrohung fällt auf 70; erneut erst nach 5 Jahren. Bei Sieg Silvermoons mit Annexion: wie bisher `.16` und Bruderkrieg-Folgen.
- **Ergebnis:** [x] OK  [ ] Fehler – Notiz: 2026-11-12, Kono (per Konsole): Buff kommt und läuft ab, Krieg erklärt. KI-Silvermoon gewinnt klar (Line Infantry gegen Bauern-Milizen); als Spieler mit Aufrüstung gewinnbar – so gewollt.
