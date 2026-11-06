# Victorian Azeroth – Projektregeln

Total-Conversion-Mod für Victoria 3: Azeroth (World of Warcraft) statt der realen Welt.
Workshop-ID `3300564446`. Fahrplan und offene Entscheidungen stehen in `.claude/ABLAUFPLAN.md`, konkrete Aufgaben als Tickets in `.claude/tickets/` (Format und Übersicht in `.claude/tickets/README.md`). Projekt-Doku gehört nach `.claude/`, nicht in den Mod-Root. Vor größerer Arbeit dort reinschauen; danach Ticket-Status, Notizen und die Übersichtstabelle aktualisieren. Neue Aufgaben, die nebenbei auffallen, als Ticket anlegen statt sie nur im Chat zu erwähnen.

## Zuerst: Karte und Skills (Token sparen)

- **`.claude/KARTE.md`** sagt, wo jedes System, jede Region und jedes Werkzeug liegt. Vor jeder Suche dort nachsehen, dann gezielt öffnen. Repo und Vanilla nicht breit durchsuchen.
- **Skills** (`.claude/skills/`) enthalten die Abläufe: `va-content` (Events, JEs, Loc, Vanilla-Vorbilder), `va-testrunde` (Lint, Testfälle, error.log, Ticket schließen), `va-karte` (States, Provinzen, Startwerte), `va-patch-upload` (Checklisten).
- Große Dateien nie ganz lesen: `TESTPROTOKOLL.md` (per `grep -n "^## Runde\|^### T-"` springen), State-/History-Dateien, Loc-Namenslisten, `province_terrains.txt`, `error.log` (über `va_errlog.py --mod`), `va_lint_baseline.txt`, `TESTPROTOKOLL_ARCHIV.md` und `tickets/archiv/` (nur für Historie).

## Wissenspflege (Kono, 2026-11-01)

Claude pflegt Karte und Skills **eigenständig, ohne Nachfrage**, als Teil jeder Aufgabe: neue/umbenannte/gelöschte Dateien und Objekte → `KARTE.md`; neues Vanilla-Vorbild → `skills/va-content/vanilla-vorbilder.md`; Fehler mit allgemeiner Ursache → „Stolperfallen“ im passenden Skill; geänderter Ablauf oder neues Werkzeug → Skill. Skills knapp halten (unter 150 Zeilen, Details in Zusatzdateien), nichts doppelt führen. Im Chat nur kurz erwähnen.

## Pfade

| Was | Pfad |
|---|---|
| Repo (Quelle der Wahrheit) | `%USERPROFILE%\Desktop\Projekte\Victorian-Azeroth-WoW` |
| Vanilla-Spiel (nur lesen) | `C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game` |
| Vom Spiel geladener Mod / Upload-Stand | `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\mod\warcraft` – bewusst eine **Kopie**, die Kono von Hand aus dem Repo befüllt (ohne `.git`, `.claude`, `.gitignore`, `map_data/provinces.xcf`). Nur dieser Ordner wird hochgeladen. Weder lesen noch schreiben, außer Kono verlangt es ausdrücklich. |
| Logs | `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\logs\error.log` |
| Script-Doku | `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\docs\` (`effects.log`, `triggers.log`, `modifiers.log`, `on_actions.log`, `event_targets.log`); per Konsole `script_docs` neu erzeugen (Stand 2026-11-06, 1.15.0) |

Zugriff unter `Documents\Paradox Interactive\Victoria 3`: nur `logs\` und `docs\` lesen (freigegeben 2026-10-29). Alles andere dort, insbesondere `mod\`, Spielstände und Einstellungen, nicht ohne ausdrückliche Erlaubnis öffnen.

Spielversion prüfen: `launcher\launcher-settings.json` → `rawVersion`. Der Mod deklariert sie in `.metadata/metadata.json` → `supported_game_version`.

## Vanilla ist die Referenz

- Syntax an Vanilla-Dateien der aktuellen Version und der Script-Doku prüfen, nie aus dem Gedächtnis (Vic3-Script ändert sich je Patch).
- **Keine ganzen Vanilla-Dateien kopieren, um sie zu ändern** (hat den Mod bei jedem Patch zurückgeworfen).
- **Abschalten:** gleichnamige leere Datei (nur BOM/Kommentar). **Ändern:** eigenes Objekt in eigener `va_`-Datei, wo möglich `INJECT:`/`REPLACE:`/`TRY_INJECT:`.
- Unvermeidbare Vollkopie → `ABLAUFPLAN.md` „Bewusste Vanilla-Overrides“ mit Grund; nur die werden bei Patches nachgezogen.
- `replace_paths` wirft den ganzen Vanilla-Ordner weg; nur für komplett ersetzte Ordner (Karte, History, Strategic Regions).

## Konventionen

- Eigene Dateien: Präfix `va_` bzw. `VA_` (z. B. `common/cultures/va_orc_cultures.txt`, `common/history/states/VA_kalimdor_states.txt`). Neue Dateien klein geschrieben mit `va_`.
- Länder-Tags: ausgeschriebene Großbuchstaben-Namen (`AHNQIRAJ`, `SILVERMOON`), Definition in `common/country_definitions/VA_<kontinent>.txt`.
- States: `STATE_<NAME>` in `map_data/state_regions/NN_va_<region>.txt`, History in `common/history/states/VA_<region>.txt`.
- Events: `namespace = <thema>_events`, IDs `<namespace>.<n>`, Loc-Keys `<id>.t` / `.d` / `.f` / `.a`, `.b` …
- Journal Entries: `je_<thema>`, Datei `common/journal_entries/VA_<thema>.txt`.
- Lokalisierung: `localization/replace/<sprache>/…_l_<sprache>.yml`, **UTF-8 mit BOM**, erste Zeile `l_english:`, Einträge mit zwei Leerzeichen eingerückt. Englisch ist Pflicht, Deutsch optional.
- **AI-WRITTEN-Markierung** (Kono, 2026-10-30): Jeder Text, den Claude schreibt (Loc: Namen, Beschreibungen, Event-Texte, Tooltips), endet sichtbar mit ` (AI WRITTEN)`, z. B. `va_dead_scar: "The Dead Scar (AI WRITTEN)"`. Runde Klammern, weil `[…]` Script ist. Ausnahme: von Kono vorgegebene oder abgenommene Texte.
- Script-Dateien (`.txt`) ebenfalls UTF-8 mit BOM, Einrückung mit Tabs wie in Vanilla.
- **Objekt-Namen:** eigene Objekte mit Präfix `va_` (Modifier, Variablen, Effekte, Trigger, Flags). Ausgenommen vorgegebene Formen: Länder-Tags, `STATE_…`, `je_…`, Event-Namespaces, `building_…`, `pm_…`, `pmg_…`, `bg_…`, Güter, Kulturen, Religionen; dort vorher prüfen, dass Vanilla den Namen nicht benutzt (`language_naga` kollidierte).
- **Kopfzeile:** jede neue `va_`-Datei beginnt mit Kommentar: Zweck, Ticket, Vanilla-Vorbild (`# Mana-Förderung an Leylinien (VA-019). Vorbild: Vanilla building_coal_mine (03_mines.txt).`).

## Content-Ablauf (Kurzfassung, Details im Skill `va-content`)

Kono liefert die Idee → Claude plant im Ablaufdiagramm `.claude/ablauf/<land>.md` (je Land 25–40 Jahre JEs, danach globale Eventgruppen VA-034) → Vanilla-Vorbild, Script **und** englische Loc zusammen → Platzhalter-Grafik mit `# TODO` und Eintrag in VA-027 → Testfälle, Kono testet, Claude wertet `error.log` aus.

## Arbeitsweise

- Die Datei `error.log` ist die einzige verlässliche Prüfung; ein Parser/Build existiert nicht. Nach Änderungen um einen Spielstart bitten statt Korrektheit zu behaupten.
- **Testprotokoll:** jede Änderung bekommt einen Testfall in `.claude/TESTPROTOKOLL.md`. Ticket erst `erledigt`, wenn Kono alle seine Testfälle mit OK bestätigt hat, bis dahin `wartet (Spieltest)`.
- **Lint vor jeder Testrunde:** `python -I .claude/tools/va_lint.py --regions <NN>` muss **0 neue Fehler** melden. `--update-baseline` nur nach Abbau von Altlasten oder mit Konos Zustimmung.
- Python-Tools: nur Standardbibliothek plus vorhandenes `numpy`/`Pillow`; nichts nachinstallieren, keine venvs.
- Große Binärdateien (Karte, Heightmap, `.bin`, `.dds`) nur auf ausdrücklichen Wunsch anfassen.
- Der Ingame-Map-Editor schreibt in `mod\warcraft`; nach Kartenarbeit ans Zurückholen erinnern.
- **Provinzen löschen nur vollständig** (Farbe und jede Referenz, sonst Absturz bzw. weißer Fleck), siehe Skill `va-karte`.
- Git: nur lesen (siehe globale Vorgaben).
