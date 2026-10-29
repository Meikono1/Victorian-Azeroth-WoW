# VA-003: Verbleibende Vanilla-Kopien abbauen

- **Status:** in Arbeit
- **Typ:** aufraeumen
- **Priorität:** hoch
- **Erstellt:** 2026-10-29

## Beschreibung

Stand nach Aufräumen 2026-10-29: 326 Dateien weichen von gleichnamigen Vanilla-1.13-Dateien ab, 63 leere Dateien schalten Vanilla ab (bleiben), 15 identische Kopien liegen in replace_paths-Ordnern (bis VA-002 nötig).

Ordnerweise vorgehen: `on_actions` → `scripted_effects/triggers` → `laws` → `buildings`/`production_methods(_groups)` → `interest_groups`/`ideologies` → Events. Echte WoW-Änderungen in `va_`-Dateien oder per `INJECT` verschieben, Rest löschen oder leer überschreiben. Bewusste Vollkopien in ABLAUFPLAN.md eintragen.

## Notizen

- 2026-10-29: Automatische Klassifizierung in `VA-003-klassifizierung.txt`: 7 Kopien mit WoW-Bezeichnern (behalten), ~340 ohne (Kandidaten), 85 in replace_paths-Ordnern. Grenze: Die Prüfung erkennt nur hinzugefügte Zeilen, nicht bewusst entfernte.
- 2026-10-29: Runde 2 gelöscht (37 Dateien): `interest_groups` (8), `ideologies` (5), `laws` (8), `government_types` ohne `01_monarchies` (5), `gfx/portraits/portrait_modifiers` (6), `ai_strategies` (5). Git-Historie zeigt nur Update-Commits, keine gezielten Kürzungen.
- Noch übrig aus diesen Ordnern: `common/laws/readme.md` (Vanilla-Doku-Kopie), `portrait_modifiers/01_shrink_body.txt` und `01_weight.txt` (bis auf Leerzeichen identisch mit Vanilla).
