# VA-044: KI stapelt Verwaltung und Bausektoren – Start-Gebäude fehlen

- **Status:** erledigt
- **Typ:** bug
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Kono 2026-10-30 (Spieltest T-037): Die meisten Staaten füllen ihre Bauliste mit Construction Sector und Government Administration (Stormwind 40+ Aufträge, 6 Jahre Bauzeit). Außerdem steht `building_paper_mills` ohne Lokalisierung in der Liste.

## Notizen

- 2026-10-30: Ursache: Start-Gebäude fehlen. Vanilla 1836 setzt Verwaltung und Bausektor in der Gebäude-History (FRA 50 / 7, GBR 35 / 9, PRU 20 / 7, SPA 18 / 5). Im Mod hatten nur 13 Länder Verwaltung (89 Stufen) und 20 einen Bausektor (30 Stufen); Stormwind und Ironforge keins von beiden. Bürokratie-Defizit und fehlende Baukapazität → KI baut genau das. Vorhandene Mod-Werte passen zum Vanilla-Maßstab (Undercity 19 Verwaltung bei 13,5 Mio. ≈ 1,4/Mio.).
- 2026-10-30: Werkzeug `.claude/tools/va_add_gov_buildings.py` (Probelauf ohne `--apply`). Regeln: nicht decentralized, Ära-1-Tech (Stufe 1–5), Gebäude noch nirgends vorhanden; in der Hauptstadt. Verwaltung 1,4 Stufen je Mio. Pops (1–25, ab 100.000 Pops), PM `pm_horizontal_drawer_cabinets` wie Vanilla. Bausektor 0,3 je Mio. (1–6, ab 1 Mio. Pops), `pm_wooden_buildings`. Angewandt auf 26–28: Verwaltung 93 Länder / 193 Stufen (Stormwind 21, Ironforge 15, Vashj'ir 15), Bausektor 29 Länder / 45 Stufen (Stormwind 5, Undercity 4). Lint 0 neue Fehler. Test T-039, Log T-038.
- Offen: Horizontal Drawers brauchen Papier (10 je Stufe). Papier kommt aus `building_paper_mills`, einem alten Gebäudenamen aus der Vanilla-Kopie `common/buildings/01_industry.txt` (1.13: `building_paper_mill`, daher die fehlende Loc) → gehört zu VA-003. Ohne Papier sinkt die Leistung um bis zu 75 %, bleibt aber über `pm_simple_organization` (12,5 statt 10 Bürokratie).
- Offen: Kalimdor (23–25) nach VA-038, Northrend/Outland/Pandaria bei Bedarf: `va_add_gov_buildings.py <Präfixe> --apply`.
- 2026-10-30, Kono nach Spieltest: Bausektoren stapelt die KI weiterhin. Mitursache: Es fehlen Probleme, die Geld kosten. Die KI hat Überschuss und baut Kapazität aus, Vanilla bremst das über Kriege, Krisen, JEs und Events mit Kosten. Gehört zu den globalen Problemen bzw. Eventgruppen (VA-034) und den Länder-JEs (Content-Fokus EK). Log T-038 sauber.
- 2026-10-30: T-039 OK (Kono: Verwaltung okay, nur wenig Mangel). Bausektor-Überschuss wird über Content mit Kosten gelöst (VA-034), nicht hier.
- Später: Falls die KI weiter stapelt, Bürokratie-Kosten je State prüfen (Defines `STATE_BUREAUCRACY_*`, viele kleine States).
