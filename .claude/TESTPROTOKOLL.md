# Testprotokoll

Jede Änderung, die Claude macht, bekommt hier einen Testfall. Christian testet im Spiel und hakt ab. Ein Ticket gilt erst als `erledigt`, wenn alle seine Testfälle **OK** sind.

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

## Runde 4 – allgemeine Events zurück (Stand 2026-10-30)

Tickets: VA-002. Lint vor Freigabe: 0 neue Fehler (2026-10-30). Kann zusammen mit den offenen Tests aus Runde 1 laufen. `mod\warcraft` vorher neu befüllen; die zwei Dateien unten dürfen dort **nicht** mehr liegen.

### T-018 error.log: Sklavenaufstand und Anarchismus (Claude)
- **Schritte:** Kampagne starten, ein paar Monate laufen lassen, Spiel beenden, Claude Bescheid geben. Wieder aktiv aus Vanilla: `events/agitators_events/slave_revolt_events.txt`, `events/iberia_events/ip4_anarchism_events.txt`.
- **Erwartet:** Keine Fehler aus diesen beiden Dateien im `error.log`. Ob die Events im Spiel auftauchen, ist Zufall und kein Testkriterium.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

