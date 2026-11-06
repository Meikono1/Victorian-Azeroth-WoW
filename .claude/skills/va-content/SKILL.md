---
name: va-content
description: Content für Victorian Azeroth schreiben – Events, Journal Entries (JE), Decisions, Scripted Buttons, Progress Bars, Static Modifiers, Scripted Effects/Trigger, On-Actions, Diplomatic Plays, Formables und die zugehörige Lokalisierung. Nutzen, sobald Kono eine Content-Idee liefert, ein Ablaufdiagramm in .claude/ablauf/ geplant wird oder ein Content-Ticket umgesetzt wird.
---

# Content schreiben (Victorian Azeroth)

Ziel: neues Script plus englische Loc in einem Durchgang, ohne Vanilla oder das Repo breit zu durchsuchen.

## 1. Orientieren (billig zuerst)

1. `.claude/KARTE.md` lesen: wo das betroffene System liegt, welche Objekte es schon gibt.
2. Ticket lesen (`.claude/tickets/VA-NNN-*.md`), bei Länder-Content `.claude/ablauf/<land>.md`.
3. Vanilla-Vorbild aus [vanilla-vorbilder.md](vanilla-vorbilder.md) nehmen, **nicht** suchen. Erst wenn die Tabelle nichts hat: `grep -rl` in genau einem Vanilla-Ordner, und das Ergebnis danach in die Tabelle eintragen.
4. Effekte, Trigger und Modifier in der Script-Doku prüfen, nur gezielt greppen (Befehle in `.claude/KARTE.md`, Abschnitt „Vanilla und Script-Doku“; die Dateien sind bis 920 KB groß). Verwendung in der Vorbild-Datei zeigt die Syntax im Zusammenhang.
5. Eigene, schon getestete Dateien sind die beste Vorlage für den Hausstil (Kommentare, Reihenfolge der Felder): Muster in [vorlagen.md](vorlagen.md).

## 2. Erst planen (Event-Ablaufplan)

Neue JEs und Events zuerst in `.claude/ablauf/<land>.md` eintragen (Mermaid plus Tabelle). Je Knoten: Bedingung/Auslöser, Folge (Folge-JE, Event, Diplomatic Play, Modifier), Dauer im Spiel (`timeout`), gedachter Aufwand für den Spieler. Pro Land 25–40 Jahre JE-Inhalt, danach Übergang zu globalen Eventgruppen (VA-034). Vorlage: `.claude/ablauf/silvermoon.md`. Werte als Vorschlag kennzeichnen, offene Punkte unter „Offen“ für Kono.

## 3. Scripten

**Dateien und Namen**
- Neue Datei: `va_<thema>_<art>.txt` im passenden `common/`-Ordner bzw. `events/va_<thema>_events.txt`, JEs in `common/journal_entries/VA_<thema>.txt` oder `va_<thema>.txt`. UTF-8 **mit BOM**, Tabs.
- Erste Zeile: Kommentar mit Zweck, Ticket und Vanilla-Vorbild (`# … (VA-NNN). Vorbild: Vanilla <objekt> (<datei>).`).
- Objekte: `va_`-Präfix für Modifier, Variablen, Effekte, Trigger, Buttons, Balken, Script-Werte, Flags. Vorgegebene Formen: `je_…`, `building_…`, `pm_…`, `pmg_…`, `bg_…`, Namespace `<thema>_events`, IDs `<namespace>.<n>`. Vor neuem Kultur-/Gut-/Gebäudenamen prüfen, dass Vanilla ihn nicht benutzt (`grep -rw <name>` im Vanilla-`common/`).
- Vanilla ändern: `REPLACE:`/`INJECT:`/`TRY_INJECT:` in eigener `va_`-Datei, nie Vollkopie. Unvermeidbare Vollkopie in `ABLAUFPLAN.md` → „Bewusste Vanilla-Overrides“.
- **Nicht** in die alten Vollkopien `common/buildings/0x_*`, `production_methods/0x_*` schreiben (VA-003), eigene `va_`-Dateien anlegen.
- Generierte Dateien (Todesschneise: `va_gen_dead_scar.py`) nur über das Skript ändern.

**Grafik-Platzhalter**
Vanilla-Bild/-Icon nehmen, Zeile mit `# TODO: eigenes Bild (VA-027)` bzw. `# TODO: eigenes Icon (VA-027)` markieren und in `.claude/tickets/VA-027-platzhalter-grafiken.md` eintragen (Größe, Zielpfad, Bildidee). Auswahl gängiger Werte in [vorlagen.md](vorlagen.md).

**JE starten**
Start-JEs zum Spielstart in `common/history/global/va_global_<region>.txt` (`GLOBAL = { c:TAG ?= { add_journal_entry = { type = je_… } } }`). Später hinzukommende per On-Action oder Event. Vic3 aktiviert JEs auch selbst, sobald `possible` erfüllt ist: Sperren (Tech, Kultur) deshalb **auch** ins `possible`, und beim Hinzufügen `NOT = { has_journal_entry = je_… }` prüfen.

## 4. Lokalisieren

- Datei `localization/replace/english/va_<thema>_l_english.yml`, UTF-8 mit BOM, erste Zeile `l_english:`, Einträge mit zwei Leerzeichen.
- Jeder Key, den das Script nennt, bekommt Text, kein Text ohne Key. Pflicht-Keys je Typ in [vorlagen.md](vorlagen.md) (z. B. JE: Name, `_reason`, Button `_desc`, Modifier `_desc`, Event `.t .d .f .a`).
- Jeder von Claude geschriebene Text endet mit ` (AI WRITTEN)`, auch Tooltips und Buttons. Ausnahme: von Kono vorgegebene oder abgenommene Texte (dann Marker entfernen, im Ticket notieren).
- Keine eckigen Klammern im Freitext, `[…]` ist Script. Anführungszeichen im Text als `\"`.
- Deutsch optional, nur wenn Kono es will.

## 5. Abschließen

1. `python -I .claude/tools/va_lint.py` (mit `--regions NN`, wenn States betroffen) → 0 neue Fehler.
2. Testfälle anlegen und Ticket nachziehen: Skill `va-testrunde`.
3. `.claude/KARTE.md` um neue Dateien/Objekte ergänzen; neue Vorbilder in `vanilla-vorbilder.md`; neue Stolperfalle unten eintragen.
4. Ablaufdiagramm auf den gebauten Stand bringen (Knoten „geplant“ → „gescriptet“).

## Stolperfallen (aus error.log und Spieltests)

- Gebäudegruppe mit `parent_group = bg_government` erbt 1 Infrastruktur und 20 Urbanisierung je Stufe. Reine Deko-/Script-Gebäude → eigene Gruppe wie Vanilla `bg_monuments_hidden` mit `infrastructure_usage_per_level = 0` (VA-062).
- Die `.md`-Doku in Vanilla-Ordnern (z. B. `common/buildings/buildings.md`) ist teils veraltet: `generates_residences` gibt es nicht (VA-062). Felder immer an echten Vanilla-Objekten prüfen.
- Ein Event-Namespace gehört in genau eine Datei (Vanilla teilt keinen). Neue Event-Datei → eigener Namespace (VA-021: `wretched_heal_events` usw.).
- Vanilla vergleicht keine `flag:`-Werte in Variablen; lieber je Zustand eine eigene Variable (`va_wretched_hunt_thaelis`).
- `scripted_progress_bar` → `monthly_progress`: Scope ist schon das Land. Kein `owner = { … }` drumherum (Balken blieben bei 0, VA-046).
- Seit 1.15 gibt es kein `complete`/`fail`/`invalid`/`on_timeout` mehr (`Unexpected token: invalid`), nur `outcome = { … }`; mit `timeout` braucht das JE genau ein `outcome` mit `flags = { timeout }`. Muster in [vorlagen.md](vorlagen.md).
- Balken haben kein Sichtbarkeitsfeld; mehrere Balken in einem JE sind erlaubt (`00_antarctica.txt`), aber immer alle sichtbar.
- Stillstand muss im Spiel erkennbar sein: im Balken ein `add = { desc = …_stalled_desc value = 0 }`-Zweig plus Status-Text im JE.
- Ungültig-/Bedingungs-Tooltips zeigen rohe Trigger („All SILVERMOON_ADJ States …“) → `custom_tooltip = { text = …_tt <trigger> }`.
- `add_journal_entry` doppelt (Global-History und `on_state_created` am selben Tag) → error.log `already has a journal entry`. Immer `NOT = { has_journal_entry = … }`.
- Zustand, der Eroberung und Teilung überleben soll, an die **State-Region** hängen (`s:STATE_X = { set_variable = … }` bzw. `state_region = { has_variable = … }`), nicht an den State.
- Länder-Modifier wirken auf alle Pops des Landes; Kultur-Modifier gibt es nicht.
- Vanilla-Trigger mit Erde-Bezug spammen das Log in Sekunden voll (VA-025): neue Funde in `va_earth_triggers.txt` per `REPLACE:` auf `always = no` setzen.
- Mod-Gebäudekopien kennen 1.13-Gebäude nicht (z. B. `building_art_academy` unbekannt) → VA-003, nicht im Event „reparieren“.
- `navigation` Stufe 6/7 und Hafen in der History → Ladefehler „must have invented Navigation“.
- Vanilla-Scripts fragen abgeschaltete Erde-JEs und -Regionen weiter ab (über 1.400 Zeilen `Invalid database object je_*`) → nicht die Aufrufer kopieren, sondern Hüllen neu erzeugen (`va_gen_earth_je_stubs.py`, `va_gen_geo_regions.py`, `va_gen_earth_event_stubs.py`, `va_gen_earth_template_stubs.py`, VA-043). Hüllen nur für **aufgerufene** Objekte, sonst meldet das Spiel z. B. `Event … is orphaned`.
- `va_common_folders.py` empfiehlt bei Kernordnern (On-Actions, Bewegungen, Flaggen, Custom Loc) „kopie-erde → leeren“. Dort **löschen**, nicht leeren, sonst fehlen Mechaniken. Erde-Abschaltung einzelner On-Actions per `trigger` in `va_on_actions_earth.txt`.
- Loc-Keys nur ASCII: `’`, `Ö` usw. im Key → „Invalid character“, Eintrag fehlt (Namenslisten, `STATE_SKÖRN`). Im Text sind sie erlaubt.
