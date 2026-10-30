# VA-023: Lint-Altlasten abbauen

- **Status:** offen
- **Typ:** aufraeumen
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

`python -I .claude/tools/va_lint.py` fand beim ersten Lauf 921 Fehler und 71 Warnungen. Alle stehen als bekannt in `.claude/tools/va_lint_baseline.txt` und blockieren keine Testrunde. Ziel: Baseline schrittweise leeren. Nach jedem Abbau `--update-baseline` laufen lassen, damit behobene Einträge verschwinden.

| Gruppe | Anzahl | Hinweis |
|---|---|---|
| Loc fehlt: Ländernamen (`TAG`, `TAG_ADJ`) | 636 | = VA-006 |
| Loc fehlt: State Regions (`STATE_…`, inkl. Meeresregionen) | 237 | Namen erscheinen sonst als roher Key auf der Karte |
| Loc fehlt: Kulturen | 26 | u. a. `arakkoa`, `centaur`, `harpy` |
| Loc fehlt: Events/JEs | 15 | Gilneas (VA-007), Silvermoon-Gerüst (VA-020) |
| Loc fehlt: Gebäude | 2 | `building_feliron_mine`, `building_eternium_mine` |
| Unbekannter Verweis | 5 | `cu:murloc` in `va_murloc_charakters.txt:5` (welche Murloc-Kultur?), `s:STATE_SK` in Northrend-History/Pops/Gebäude (Tippfehler oder fehlender State), `s:STATE_DISTRICT_OF_COLUMBIA` in `gilneas_events/infection_events.txt:1001` (Erde-Rest) |
| Warnung: Script-Datei ohne UTF-8-BOM | 71 | Projektregel verlangt BOM, Spiel lädt sie aber |

## Notizen
