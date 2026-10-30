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
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-002 error.log (Claude)
- **Schritte:** Nach T-001 Spiel beenden, Claude Bescheid geben. Claude prüft mit `python -I .claude/tools/va_errlog.py --filter …` auf: `26_va_north_eastern_kingdoms`, `VA_eastern_kingdoms_states`, `va_north_eastern_kingdoms`, `VA_eastern_kingdom.txt`, `va_eastern_kingdom_countries`, `va_goods`, `va_mana`, `va_building_groups`, `leyline`, `mana`, `va_countries_l_english`. Außerdem `python -I .claude/tools/va_check_states.py 26`.
- **Erwartet:** Keine Fehler aus diesen Dateien. Die Hub-Fehler für Gilneas City, The Headlands, Seradane, Scholomance, Northgate Woods und Tyr's Hand sind weg.
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

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
