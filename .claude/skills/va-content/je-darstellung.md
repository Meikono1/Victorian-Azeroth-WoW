# Journal Entries: Darstellungsmöglichkeiten (Stand 1.15.0)

Ausgewertet 2026-11-09 aus Vanilla `common/journal_entries/` (184 Dateien), `journal_entries.md`, `scripted_buttons.md`, `scripted_progress_bars.md`, `gui/journal_entry.gui`, `gui/journal.gui`, `gui/outliner_ongoing_types.gui` und der Script-Doku. Zahlen in Klammern = Häufigkeit in Vanilla; was VA davon nutzt, steht in Abschnitt 8.

**Screenshot-Abgleich offen:** Abschnitt 7 listet, was Kono im Spiel fotografieren soll. Bis dahin ist die Reihenfolge aus `journal_entry.gui` abgeleitet, nicht gesehen.

## 1. Wo ein JE überall auftaucht

| Ort | Was dort steht | Gesteuert über |
|---|---|---|
| Journal-Liste (`journal.gui`) | Name, Icon, Fortschrittsbalken, Tooltip `<key>_goal` | `group` (+ `themed = yes` → Gruppe mit Illustration), `highlight = yes` (größerer Knopf, 1×), `weight` (Sortierung) |
| JE-Panel (`journal_entry.gui`) | alles aus Abschnitt 2 | siehe dort |
| Outliner (angepinnt) | Name, Status-Text, „mögliche Aktionen“ (Zahl klickbarer Buttons), Script-Balken, normaler Balken | `should_be_pinned_by_default_uninvolved_or_context = yes` (406), `should_be_pinned_by_default_involved` (30, nur kontextlos) |
| Goal-Tracker oben | das aktive JE mit höchstem `weight` | `weight` (416) |
| Karten-Modus | Färbung je State + Hover-Tooltip | `map_color`, `map_color_second` (Streifen), `map_tooltip` (14), Root = State |
| Lobby (Länderwahl) | JE als Vorschau | `is_shown_in_lobby = { … }` (85, undokumentiert) |
| Abgeschlossen-Reiter | Name ohne Scope, `conclusion_desc`, Marke „historisch“ | `<key>_concluded` (statischer Name), `outcome.flags = { historical }` (11) |

## 2. Aufbau des JE-Panels (von oben nach unten)

Laut `gui/journal_entry.gui`. Die `.md`-Doku lässt `custom_widget_container_buttons` und die Modifier-Liste aus.

| # | Element | Quelle im Script | sichtbar wenn |
|---|---|---|---|
| 1 | Titel | Loc `<key>` | immer |
| 2 | Icon **oder** Widget `custom_widget_container_je_icon` | `icon = "…dds"` (442), sonst Default aus `00_interfaces.txt` | Widget ersetzt Icon |
| 2a | Gruppen-Illustration hinter dem Icon | `illustration` der Gruppe | Gruppe hat eine |
| 2b | Symbol „läuft“ | `is_progressing = { … }` (37) | Trigger wahr |
| 2c | Modifier-Liste (Skalierend + Zeitlich) | `scaling_modifiers_while_active` (3), `add_modifier` im JE-Scope (`scope:journal_entry`) | Liste nicht leer |
| 2d | DLC-Plakette | `dlc = …` (197, sperrt nichts) | gesetzt |
| 3 | `custom_widget_container_1` | `widget` | |
| 4 | Ablauf-Zeit | `timeout = <Tage>` (88) | gesetzt |
| 5 | Status-Text | `status_desc = { first_valid = { triggered_desc … } }` (76), sonst Loc `<key>_status` | Text nicht leer |
| 6 | `custom_widget_container_2` | | |
| 7 | Buttons **oder** `custom_widget_container_buttons` | `scripted_button = …` (289, mehrfach) | Widget ersetzt Buttons |
| 8 | `custom_widget_container_3` | | |
| 9 | Script-Balken (alle, immer sichtbar) | `scripted_progress_bar = …` (73, mehrfach) | mind. einer |
| 10 | Standard-Fortschrittsbalken + „Fortschritt: x %“ | `progressbar = yes` (67) mit `current_value`/`goal_add_value`; `display_progressbar_as_months = yes` (1) bzw. `…_as_weeks` (laut GUI) zeigt Zeit statt Prozent | `progressbar = yes` und aktiv |
| 10a | aufklappbar „Fortschrittsbedingungen“ (Vorwärts/Rückwärts) | `progress_condition` mit `desc` in Script-Balken | mind. ein Eintrag |
| 11 | `custom_widget_container_4` | | |
| 12 | Beschreibung | `reason = { … }` (1) oder Loc `<key>_reason` | immer |
| 13 | `custom_widget_container_5` | | |
| 14 | Beteiligte Länder (Flaggen) | kontextlose JEs, `should_be_involved`, `add_involved_country` | Liste nicht leer |
| 15 | `custom_widget_container_6` | | |
| 16 | Fortschrittstext über den Ausgängen | `progress_desc` (2) oder Loc `<key>_progress` | Text nicht leer |
| 17 | Ausgänge in Deklarationsreihenfolge: Kopf, Bedingungen, Effekt | `outcome` (927), Details Abschnitt 3 | nicht `hidden` |
| 18 | `custom_widget_container_7` | | |
| 19 | Knöpfe „Wie?“/„Warum?“ | `how_tutorial`, `why_tutorial` (Tutorial-Lektionen) | gesetzt |

Abgeschlossen zeigt das Panel nur Name (`<key>_concluded`, falls vorhanden), Marke „historisch“ und `conclusion_desc`; Widgets verschwinden.

## 3. Ausgänge (`outcome`)

- `header` (Wie erreichen) / `effect_header` (Was passiert): Standard `je_standard_completion_header`/`je_standard_on_completion_header` (Erfolg), `je_standard_failure_header`/`…on_failure_header` (Fehlschlag), `JOURNAL_ENTRY_TIMEOUT`/`JOURNAL_ENTRY_ON_TIMEOUT` (Zeitablauf). Eigene Keys erlaubt (Meiji, Red Summer: je Fraktion ein Kopf); Effekt-Loc mit `$EFFECT$`.
- `color`: `gold_positive` (438), `blue_negative` (218), außerdem `red_outcome`, `pink_outcome`, `green_outcome`, `white_outcome` → mehr als zwei Ausgänge farblich trennen.
- Bedingungstext = automatisch aus `trigger`; lesbar machen mit `custom_tooltip = { text = …_tt <trigger> }`.
- Effekttext = automatisch aus `effect`; Zusatzzeilen `event_outcome_desc` (Loc, `first_valid`) bzw. `event_outcome_effect_desc` (Effekte nur als Tooltip, 103).
- Flags: `hidden`, `invalid_outcome` (nur mit `hidden`), `timeout` (ohne `trigger`, Pflicht bei `timeout`), `fails_subgoal`, `historical`.
- Für den Aktivierungszeitpunkt: `event_outcome_activated_desc` / `event_outcome_activated_effect_desc` (2, Spanien).

## 4. Buttons (`common/scripted_buttons/`)

| Feld | Vanilla | Wirkung in der Anzeige |
|---|---|---|
| `name`, `desc` | 269 | Beschriftung, Tooltip |
| `visible` / `possible` | 266 / 257 | ausgeblendet / ausgegraut |
| `selected` | 132 | anderes Aussehen + Tooltip, bleibt klickbar → Schalter (an/aus) |
| `cooldown` | 58 | Sperrzeit nach Klick |
| `autocomplete = yes` | 21 | kein Klick, läuft selbst bei visible+possible; eigenes Aussehen („erledigt“ über `selected`). KI klickt nie |
| `icon` | 9 | Bild auf dem Knopf (beliebiger Pfad) |
| `cost` | 9 | **nur Anzeige**, Abzug selbst in `possible`/`effect` |
| `short_desc`, `tags` | 9 / 1 | nur für eigene Widgets (Tsarpoints-Dekrete, Porträt per Tag `unlocked_by_ruler/favorite/heir`) |

Outliner zeigt nur die Zahl möglicher Buttons, nicht die Buttons selbst.

## 5. Script-Balken (`common/scripted_progress_bars/`)

- Fertige Looks: `default = yes` (blau), `default_green`, `default_bad` (rot).
- Eigener Look (16): `progress_texture`, `background_texture`, `glow_texture`, `glow_line_texture` aus `gfx/interface/progressbar/progressbar_<farbe>*.dds` (`default`, `gold`, `green`, `bad`, `white`), `color = { r g b a }` tönt alles (mit `progressbar_white`), `marker = yes` (Schieber „zwischen zwei Polen“, 12), `left_icon`/`right_icon` (nur im Panel; Vorbilder `tokugawa_marker`, `qing_dynasty_marker`, `greatgame_lion/bear_marker`, `twospains_*_marker`).
- Texte: `desc` links, `second_desc` rechts im Balken (14).
- `is_inverted = yes`: Ziel ist, den Wert niedrig zu halten.
- `min_value`/`max_value` dürfen Script-Werte sein.
- **`progress_condition` statt `if`** in `weekly/monthly/yearly_progress`: erscheint in der aufklappbaren Vorwärts/Rückwärts-Liste mit Haken bzw. leerem Kästchen, auch wenn nicht erfüllt → zeigt dem Spieler, was fehlt. Nur mit `desc`. Kein `format =` darin.
- Kein Sichtbarkeitsfeld; Effekte `add_progress`, `set_bar_progress`, Trigger `scripted_bar_progress`.

## 6. Eigene GUI-Widgets (`widget = { gui name container }`)

Nur 5 Vanilla-JEs (Meiji, Great Game, Rlit, Tsarpoints). Dateien in `gui/journal_entry_widgets/*.gui`; Mod-Datei wäre `gui/journal_entry_widgets/va_<thema>_widgets.gui`. Möglich ist alles, was die GUI-Sprache kann: Porträts (`[JournalEntry.GetCountry.GetRuler]`, Vorlage `custom_widgets.gui` mit `je_widget_ruler_large`), Listen anderer JEs, eigene Button-Leisten (`custom_widget_container_buttons` ersetzt die Standard-Buttons), Modifier-Anzeigen, Routen-Listen.

Aufwand und Risiko deutlich höher als Script: kein Lint, Fehler nur im `error.log`, Datenfunktionen (`JournalEntry.Get…`) sind nicht dokumentiert, nur aus Vanilla-`.gui` ablesbar. Vorbild zuerst `custom_widgets.gui` (63 Zeilen), dann `great_game_widgets.gui` (41).

## 7. Für Kono: Screenshots zum Abgleich

1. Ein JE mit vielen Elementen, z. B. **Meiji-Restauration** (Japan, Widgets + Balken) oder **Tsarpoints** (Russland, Buttons mit Kosten/Porträt): ganzes Panel, gescrollt.
2. **Opium-Kriege** (China): Balken als Monate.
3. Ein JE mit `marker`-Balken und Seiten-Icons (Great Game oder Two Spains).
4. Aufgeklappte „Fortschrittsbedingungen“ an einem Balken mit `progress_condition`.
5. Outliner mit angepinntem JE, Goal-Tracker oben, Journal-Liste mit themed Gruppe.
6. Eines unserer JEs (`je_silvermoon_wretched`, mehrere Balken + Schalter) zum Vergleich.

Screenshots nach `.claude/screenshots/je/` legen, dann Abschnitt 2 bestätigen bzw. korrigieren.

## 8. Was VA heute nutzt

Ohne Erde-Hüllen nutzt VA: `icon`, `group`, `scripted_button` (17), `scripted_progress_bar` (8), `status_desc` (4), `timeout` (4), `weight` (7), Pinning (6), Farbe nur `gold_positive`. **Ungenutzt:** eigene Kopf-Keys und Ausgangsfarben, `event_outcome_*_desc`, `progress_condition`, eigene Balken-Looks/Marker/Icons, Button-`icon`/`cost`/`autocomplete`, `progressbar`/`current_value`, `scaling_modifiers_while_active`, Karten-Modus, `is_shown_in_lobby`, themed Gruppen mit Illustration, Widgets.

## 9. Abweichungen der Vanilla-Doku

- Undokumentiert, aber benutzt: `activation_description` (449, fast immer `always = yes`), `is_shown_in_lobby` (85), `should_update_on_player_command` (8, Tutorial), `display_progressbar_as_months` (1), `should_be_pinned_by_default_involved` (30).
- Loc `<key>_goal`: Tooltip am Fortschritt in der Liste (`GetGoalDesc`), nicht in der `.md`.
- GUI-Reihenfolge in der `.md` ohne `custom_widget_container_buttons` und Modifier-Liste.
