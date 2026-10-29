# VA-002: replace_paths verschlanken

- **Status:** offen
- **Typ:** technik
- **Priorität:** hoch
- **Erstellt:** 2026-10-29

## Beschreibung

`events`, `events/india_events`, `events/soi_events`, `common/journal_entries`, `common/scripted_buttons`, `common/company_types`, `common/character_templates` aus `replace_paths` nehmen. Danach nur historisch-spezifische Vanilla-Dateien leer überschreiben, allgemeine Mechaniken (Wahlen, Gesetze, Streiks …) kommen wieder aktuell aus Vanilla und die eigenen Kopien in diesen Ordnern können weg.

Hinweis: `replace_paths` gilt nur für genau den Ordner, nicht für Unterordner.

## Notizen

