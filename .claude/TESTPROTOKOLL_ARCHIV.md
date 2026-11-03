# Testprotokoll – Archiv

Abgeschlossene Testrunden aus `TESTPROTOKOLL.md`: alle Testfälle OK, entfallen oder per Folgetest bzw. Ticket erledigt. Nur zum Nachschlagen (Historie), bei der Arbeit nicht lesen. Runden nach Nummer sortiert.

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
