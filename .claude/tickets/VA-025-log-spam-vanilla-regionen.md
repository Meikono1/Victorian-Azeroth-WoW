# VA-025: Log-Spam durch Vanilla-Scripts mit realen Regionen

- **Status:** erledigt
- **Typ:** bug
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Im laufenden Spiel schreiben Vanilla-Scripts, die reale Strategic Regions (`sr:region_*`) oder States (`s:STATE_*`) ansprechen, mehrere tausend Fehler pro Sekunde ins `error.log`. Die gibt es durch `replace_paths` nicht mehr. Folge: Das Log rotiert (6 × 512 KB) innerhalb von Sekunden, **die Ladefehler beim Spielstart sind danach verloren**. Damit ist der Log-Testfall jeder Runde (z. B. T-002) nicht auswertbar, und die KI-Trigger arbeiten mit kaputten Bedingungen.

Gemessen 2026-10-30 (alle sechs Logdateien decken nur 10:31:11–10:31:19 ab):

| Vanilla-Stelle | Treffer | Ursache |
|---|---|---|
| `events/natural_disasters_events.txt:478/559` → `00_scripted_triggers.txt:357–393` (`in_volcanic_zone` u. a.) | ~4.900 | `sr:region_indonesia` usw. |
| `common/scripted_triggers/00_ai_triggers.txt:619–634` aus `ai_strategies/00_default_strategy.txt:2124` | ~1.200 | `sr:region_north_china`/`south_china` |
| `common/political_movements/00_ideological_movements.txt:5672` | 814 | `has_law_or_variant` bekommt eine Gesetzesvariante (vermutlich aus Mod-Gesetzes-History, → VA-014) |
| `events/agitators_events/historic_agitator_events.txt:1207/1390` | 53 | reale Bezüge |
| `common/scripted_progress_bars/00_victoria_progress_bars.txt` | 42 | reale Bezüge |
| `events/brazil/misc_events.txt:116` | 28 | reale Bezüge |

## Lösungsansatz (Vorschlag)

- Reale Events/Inhalte, die in Azeroth nichts verloren haben, per leerer gleichnamiger Datei abschalten (`events/natural_disasters_events.txt`, `events/brazil/…`).
- Scripted Triggers, die global genutzt werden (`in_volcanic_zone`, KI-China-Trigger): gezielt per `REPLACE:` neutralisieren statt Datei kopieren; in der Doku prüfen, ob `scripted_triggers` `REPLACE:` unterstützt.
- `has_law_or_variant`: Ursache in der Gesetzes-History suchen (mit VA-014).
- Danach Testlauf und prüfen, dass das Log über einen Spielmonat unter der Rotationsgrenze bleibt.

## Notizen

### 2026-10-30 – umgesetzt

- `common/scripted_triggers/va_geography_triggers.txt`: `REPLACE:in_volcanic_zone = { always = no }` (TODO: Azeroth-Vulkangebiete). Die Naturkatastrophen-Events bleiben, feuern für Vulkane aber nicht mehr.
- `common/scripted_triggers/va_ai_triggers.txt`: `REPLACE:should_carve_up_china = { always = no }`.
- `has_law_or_variant = law_type:law_homesteading` → `has_law = law_type:law_homesteading` (in 1.13 ist Homesteading eine Variante von `law_peasant_proprietorship`; `has_law` behält die alte Bedeutung exakt bei). Betroffen: `common/political_movements/00_ideological_movements.txt` (2×), `events/agitators_events/agitators_election_events.txt` (8×), `events/agitators_events/land_ownership_law_events.txt` (3×), `events/brazil/misc_events.txt` (2×, dort zusätzlich `ig:ig_industrialists ?=` wie Vanilla 1.13).
- `common/on_actions/00_on_actions_yearly.txt`: `historical_agitators_yearly_events` geleert. Alle 23 historischen Agitatoren sind reale Personen mit Erde-Bezügen (`c:FRA`, `cu:polish`, `s:STATE_VOLHYNIA` …). Die On-Action bleibt definiert, weil `00_code_on_actions.txt` sie aufruft. Die Eventdatei liegt ungenutzt herum (Aufräumen mit VA-003).
- Lint: 0 neue Fehler.

### 2026-10-30 – Runde 2 (ein Jahr gelaufen)

- Die vier Gruppen von oben sind weg (T-014 OK). Jetzt rotiert das Log durch `is_oppressor_of_schleswig_holstein` (Vanilla `00_scripted_triggers.txt:1727`, aus `ai_strategies`), 11.071 Einträge in ~10 s.
- Scan aller Vanilla-`scripted_triggers`/`scripted_effects` auf `s:`/`sr:`-Verweise, die es im Mod nicht gibt: 17 Trigger, 32 Effekte.
- Neue Datei `common/scripted_triggers/va_earth_triggers.txt`: alle 17 Trigger per `REPLACE:` auf `always = no` (Schleswig-Holstein, griechische/byzantinische States, Balkan-Kriegsbeute, Meerengen, Europa-Interessen, Brasilien, Russland/Asien, Ungarn/Kroatien, Föderation Amerikas, Schottland-Wappen). `trade_center_construction_allowed` bleibt, die Erde-Teile sind dort an Kanton-/Sakoku-Gesetze gebunden.
- Die 32 Effekte (Japan-Daimyo, spanische Kolonien, Great Game, Ostkrise …) laufen nur aus Erde-Events/JEs und bleiben vorerst. Sollten sie im Log auftauchen: Aufrufer abschalten, nicht die Effekte.
- Lint: 0 neue Fehler. Test: T-015.

### 2026-10-30 – Abschluss

- Runde 3 (T-016/T-017 OK): Kein Laufzeit-Spam mehr, das Log bleibt über ein Spieljahr lesbar und enthält die Ladefehler. Reste (geographic_regions, power_bloc_names) → VA-026.

### Nicht angefasst / Nebenbefunde

- `common/power_bloc_names/00_power_bloc_names.txt:577` (19×, `Invalid right side during comparison`): nach T-015 ansehen.

- `00_victoria_progress_bars.txt` (Vanilla, 42×: `Invalid owner for scope type 0`, `has_variable … Scope: empty`) und `government_petition_events.txt` (3×, `add_journal_entry` braucht Kontext): gering, erst nach dem nächsten Log ansehen.
- `events/natural_disasters_events.txt` (Mod-Kopie, alter Stand) ruft `in_earthquake_zone` auf. Den Trigger gibt es weder in Vanilla 1.13 noch im Mod (Vanilla heißt jetzt `is_vulnerable_to_earthquakes`). Vermutlich ein Ladefehler, der bisher wegrotiert ist.
- In `va_geography_triggers.txt` sind die `REPLACE:`-Trigger leer (`is_vulnerable_to_droughts = { }` usw.). Ein leerer Trigger ist **wahr**, damit gelten alle States als dürre-, flut-, frost- und heuschreckengefährdet. Prüfen, ob das gewollt ist, sonst `always = no`.
- Grundproblem bleibt: Der Mod-Ordner `events/` ist eine veraltete Vollkopie von Vanilla mit Erde-Inhalten (VA-002/VA-003).

- Zusammenhang: VA-002 (replace_paths), VA-003 (Vanilla-Kopien), VA-014 (Gesetze).
