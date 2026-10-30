# VA-006: Lokalisierung der Ländernamen

- **Status:** offen
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-10-29

## Beschreibung

Für die 319 Tags in `common/country_definitions/VA_eastern_kingdom.txt`, `VA_kalimdor.txt`, `VA_outlands.txt` gibt es keine Namen (`TAG`, `TAG_ADJ`). Englisch Pflicht, Deutsch optional. Claude kann einen Entwurf aus den Tag-Namen erzeugen, Christian korrigiert Lore-Namen.

## Notizen

- 2026-10-30: Datei `localization/replace/english/va_countries_l_english.yml` angelegt. Bisher nur `AMANI_TRIBE` = „Zul'Jarra“ (Lore-Name bis zur Reichsgründung, Entscheidung Christian).
- 2026-10-30: Testfälle im [Testprotokoll](../TESTPROTOKOLL.md), Runde 1: T-009.
