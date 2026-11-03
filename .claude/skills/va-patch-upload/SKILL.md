---
name: va-patch-upload
description: Checklisten für den Victorian-Azeroth-Mod bei einer neuen Victoria-3-Spielversion (Patch, Hotfix, supported_game_version) und vor einem Upload in den Steam Workshop (Release, neue Mod-Version, mod\warcraft befüllen, TODO-Durchgang). Nutzen, wenn Kono einen Patch meldet, die Spielversion sich geändert hat oder ein Upload ansteht.
---

# Patch-Wechsel und Workshop-Upload

Beide Checklisten werden jedes Mal **komplett** abgehakt. Ergebnis als Notiz in einem eigenen Ticket („Patch 1.x“ bzw. „Upload Version N“), nicht nur im Chat.
Diese Datei ist die einzige Quelle der Checklisten; der Ablaufplan verweist hierher.

## Checkliste: neue Spielversion (Patch)

- [ ] Version prüfen: `C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\launcher\launcher-settings.json` → `rawVersion`; `.metadata/metadata.json` → `supported_game_version` anpassen
- [ ] Kono: Spiel einmal starten, in der Konsole `script_docs` ausführen (aktualisiert `Documents\…\Victoria 3\docs\*.log`). Danach Datum der `effects.log` prüfen und den Doku-Hinweis in `.claude/KARTE.md` aktualisieren
- [ ] Jede Datei unter „Bewusste Vanilla-Overrides“ (`ABLAUFPLAN.md`) gegen die neue Vanilla-Datei vergleichen und Neuerungen übernehmen
- [ ] `common/defines/00_defines.txt` auf neue Werte mit Provinz-/State-IDs prüfen (Absturzgefahr wie `WORLD_MARKET_LOCATION`)
- [ ] Neue Vanilla-Ordner und -Dateien suchen, die Erde-States, -Tags oder -Kulturen referenzieren (`history`, `strait_definitions`, `geographic_regions`, `ai_strategies` …) → abschalten oder abfangen (VA-004)
- [ ] Neue Vanilla-Pflichtfelder/-Formate in Ordnern mit eigenen Objekten prüfen (State Regions, Gebäude, Güter, Kulturen, Länder), z. B. Ressourcen-Format 1.13
- [ ] `python -I .claude/tools/va_events.py --details`: neue Vanilla-Eventdateien mit Erde-Inhalt mit `--stubs` abschalten; bei „vanilla-allgemein“ und `GENERIC` von Hand gegenprüfen
- [ ] Dasselbe mit `python -I .claude/tools/va_common_folders.py common/journal_entries --details` und ebenso für `common/scripted_buttons`, `common/company_types`, `common/character_templates`; neue „vanilla-allgemein“-Dateien mit Erde-Thema in `EARTH` eintragen
- [ ] Hüllen neu erzeugen: `python -I .claude/tools/va_gen_geo_regions.py --apply` (leere Erde-`geographic_regions`) `python -I .claude/tools/va_gen_earth_je_stubs.py --apply` (nie aktivierbare Erde-JEs), `python -I .claude/tools/va_gen_earth_event_stubs.py --apply` (versteckte Erde-Events), `python -I .claude/tools/va_gen_earth_template_stubs.py --apply` (Erde-Charaktervorlagen) und `python -I .claude/tools/va_gen_earth_overrides.py --apply` (Vanilla-Bedingungen mit Erde-States, Liste `FILES`); auch nach neuen Stubs
- [ ] Vanilla-Vorbilder prüfen: Stimmen Pfade und Objekte in `.claude/skills/va-content/vanilla-vorbilder.md` noch (Datei vorhanden, Objekt per `grep` auffindbar)? Stand-Zeile dort aktualisieren
- [ ] `python -I .claude/tools/va_lint.py --regions 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35` → 0 neue Fehler
- [ ] Testrunde mit Kampagnenstart und `error.log`-Auswertung (`va_errlog.py --mod`, Skill `va-testrunde`)

Vorgehen beim Vergleich mit Vanilla: per `git diff --no-index <alt> <neu>` bzw. Datei-Datum (`ls -la --time-style=long-iso`) die geänderten Vanilla-Dateien eingrenzen, nicht alles lesen.

## Checkliste: Upload in den Workshop

- [ ] Letzte Testrunde im `TESTPROTOKOLL.md` komplett OK
- [ ] `va_lint.py` meldet 0 neue Fehler
- [ ] Alle Tickets dieser Version stehen auf `erledigt` oder bewusst offen (mit Notiz)
- [ ] TODO-Durchgang: alle `TODO` im Mod (ohne `.claude/`) durchsehen (`grep -rn "TODO" --include=*.txt --include=*.yml common events localization gfx map_data`); jedes gehört zu einem Ticket. Grafik-TODOs in VA-027 nachtragen bzw. erledigte dort austragen, übrige erledigen oder dem passenden Ticket als Notiz zuordnen
- [ ] `AI WRITTEN`-Durchgang: `grep -rc "AI WRITTEN" localization` zählen und Kono die Zahl nennen (Texte, die noch neu geschrieben werden sollen)
- [ ] `.metadata/metadata.json`: `version` hochgezählt, `supported_game_version` stimmt
- [ ] Mod-Ordner `mod\warcraft` vollständig aus dem Repo neu befüllt (ohne `.git`, `.claude`, `.gitignore`, `map_data/provinces.xcf`; gelöschte Repo-Dateien auch dort löschen) – macht Kono, Werkzeug geplant in VA-010
- [ ] Kurztest aus dem Mod-Ordner: Kampagne lädt
- [ ] Änderungen seit dem letzten Upload als Workshop-Text zusammengefasst (Quelle: „Erledigt“ im `ABLAUFPLAN.md` seit dem letzten Upload-Ticket; `git log` nur lesen)

Git bleibt dabei tabu für schreibende Aktionen (Commit, Tag macht Kono).

## Stolperfalle: alte Grafik-Kopien

- Vollkopien unter `gfx/map/` (z. B. `army_dioramas`, `front_entities`, `fleet_dioramas`) überdecken neue Vanilla-Stände und lassen nach Patches Soldaten bzw. Schiffe verschwinden (VA-058). Bei jedem Patch `gfx/map/`-Kopien gegen Vanilla diffen; ohne Mod-Inhalt löschen (auch in `mod\warcraft`).
