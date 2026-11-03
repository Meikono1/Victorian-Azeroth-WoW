# VA-057: Namen für Strategic Regions fehlen

- **Status:** erledigt
- **Typ:** loc
- **Priorität:** mittel
- **Erstellt:** 2026-11-03

## Beschreibung

Im Krieg zeigt die Karte das Hauptquartier mit rohem Key, z. B. `region_searing_gorge` (Spieltest Kono 2026-11-03, Thorium Brotherhood gegen Dark Iron). Von 171 Strategic Regions in `common/strategic_regions/*.txt` haben **130 keinen englischen Loc-Key**, darunter Land- (`region_eversong_woods`, `region_dun_morogh`) und Seeregionen (`region_eversong_sea`, `region_frozen_sea_lane_01`).

Umsetzung: eigene Datei `localization/replace/english/map/va_strategic_regions_l_english.yml` (Vorbild: Vanilla `localization/english/map/…` mit `region_<name>: "<Name>"`). Namen aus den WoW-Zonen ableiten, Seeregionen nach dem anliegenden Gebiet. Texte mit ` (AI WRITTEN)`, außer Kono gibt die Namen vor. Fehlende Keys per Skript ermitteln (Regionen aus `common/strategic_regions`, Keys aus allen englischen `.yml`).

## Notizen
- 2026-11-03, Claude: Zählung per Python, Liste beim Umsetzen neu erzeugen.
- 2026-11-03, Claude: Alle 130 fehlenden Namen in `localization/replace/english/map/va_strategic_regions_l_english.yml` (Landregionen nach WoW-Zone, Seeregionen nach Key mit korrigierten Schreibfehlern, bekannte Gewässer: The Great Sea, The Forbidding Sea, The Frozen Sea, Vashj'ir, Abyssal Breach, Korthun's End). Prüfskript: 0 fehlend, keine doppelten Keys. Lint 0 neue Fehler. Test T-068, T-069.
- Offen für Kono: `region_lost_isles` (State `LOST_ISLES_LEGION`) als „Broken Isles“ benannt; passt das? Durchnummerierte Seewege „Frozen Sea Passage I–IV“, „South Seas Passage I–V“ ggf. eigene Namen. Deutsch fehlt (optional). Der Marker „(AI WRITTEN)“ steht auch hier im Kartennamen; entfernen, sobald Kono die Namen abnimmt.
- Nebenbei: Der Key `region_dreanor` ist falsch geschrieben (Name im Spiel korrekt „Draenor“); die alte Datei `strategic_regions_l_english.yml` enthält noch Erde-Regionen.
- 2026-11-03, Kono: Namen übernommen. Claude: Marker „(AI WRITTEN)“ entfernt. Lost Isles, Draenor, Kul Tiras und Zandalar sind noch nicht gemappt; ihre Namen bleiben vorläufig (`region_lost_isles` = „Broken Isles“ bis zur Kartenarbeit).
- 2026-11-03: T-068, T-069 OK. Erledigt.
