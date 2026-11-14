# VA-002: replace_paths verschlanken

- **Status:** wartet (Spieltest)
- **Typ:** technik
- **Priorität:** hoch
- **Erstellt:** 2026-10-29

## Beschreibung

`events`, `common/journal_entries`, `common/scripted_buttons`, `common/company_types`, `common/character_templates` aus `replace_paths` nehmen, damit allgemeine Vanilla-Mechanik (Wahlen, Gesetze, Streiks …) aktuell bleibt; nur Erde-Dateien leer überschreiben. `replace_paths` gilt nur für genau den Ordner, nicht für Unterordner. Vollständiger Verlauf (Teile 1–3, Klassifizierung, Ausnahmelisten): [verlauf/VA-002-replace-paths-verschlanken.md](verlauf/VA-002-replace-paths-verschlanken.md).

## Stand (2026-11-14)

- Teile 1–3 umgesetzt (Kono, 2026-10-30). In `replace_paths` stehen nur noch `common/history/*`, `common/strategic_regions`, `map_data`.
- Werkzeuge: `va_events.py` (Events) und `va_common_folders.py <ordner>` (übrige Ordner) stufen Vanilla-Dateien als Erde/allgemein ein und legen Stubs an. Ausnahmelisten im Skript: `GENERIC`, `GENERIC_GEO`, `EARTH`, `OVERRIDE`; Gruppe `stub-pruefen` bei Patches durchsehen.
- Standardvorlage `common/character_templates/00_default_template.txt` ist bewusster Override (Vanilla plus Lebensdauer und Staatsreligion, `VA:` markiert).
- Folgearbeit lief in VA-003 (alte Kopien) und VA-043 (Erde-Hüllen für JEs, Events, Vorlagen).

## Offen

- Spieltests **T-021** (Lebensdauer und Religion) und **T-022** (nur Basisfirmen). Danach `erledigt`.
- `events/iberia_events/ip4_election_rigging.txt` bleibt abgeschaltet (fragt das Brasilien-JE ab); Freigabe nur bei Bedarf.

## Notizen

- 2026-11-14 (VA-074): Ticket auf Stand gekürzt, alter Verlauf unter `verlauf/`. Status von `in Arbeit` auf `wartet (Spieltest)`, weil nur noch T-021/T-022 fehlen.
