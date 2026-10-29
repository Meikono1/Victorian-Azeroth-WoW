# Victorian Azeroth – Projektregeln

Total-Conversion-Mod für Victoria 3: Azeroth (World of Warcraft) statt der realen Welt.
Workshop-ID `3300564446`. Fahrplan und offene Entscheidungen stehen in `.claude/ABLAUFPLAN.md`, konkrete Aufgaben als Tickets in `.claude/tickets/` (Format und Übersicht in `.claude/tickets/README.md`). Projekt-Doku gehört nach `.claude/`, nicht in den Mod-Root. Vor größerer Arbeit dort reinschauen; danach Ticket-Status, Notizen und die Übersichtstabelle aktualisieren. Neue Aufgaben, die nebenbei auffallen, als Ticket anlegen statt sie nur im Chat zu erwähnen.

## Pfade

| Was | Pfad |
|---|---|
| Repo (Quelle der Wahrheit) | `C:\Users\Christian\Desktop\Projekte\Victorian-Azeroth-WoW` |
| Vanilla-Spiel (nur lesen) | `C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game` |
| Vom Spiel geladener Mod / Upload-Stand | `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\mod\warcraft` – bewusst eine **Kopie**, die Christian von Hand aus dem Repo befüllt (ohne `.git`, `.claude`, `.gitignore`, `map_data/provinces.xcf`). Nur dieser Ordner wird hochgeladen. Weder lesen noch schreiben, außer Christian verlangt es ausdrücklich. |
| Logs | `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\logs\error.log` |
| Script-Doku | `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\docs\` (`effects.log`, `triggers.log`, `modifiers.log`, `on_actions.log`, `event_targets.log`); per Konsole `script_docs` neu erzeugen |

Zugriff unter `Documents\Paradox Interactive\Victoria 3`: nur `logs\` und `docs\` lesen (freigegeben 2026-10-29). Alles andere dort, insbesondere `mod\`, Spielstände und Einstellungen, nicht ohne ausdrückliche Erlaubnis öffnen.

Spielversion prüfen: `launcher\launcher-settings.json` → `rawVersion`. Der Mod deklariert sie in `.metadata/metadata.json` → `supported_game_version`.

## Vanilla ist die Referenz

- Syntax immer an Vanilla-Dateien der aktuellen Version und an der Script-Doku prüfen, nicht aus dem Gedächtnis schreiben. Vic3-Script ändert sich zwischen Patches.
- **Keine ganzen Vanilla-Dateien kopieren, um sie zu ändern.** Genau das hat den Mod bisher bei jedem Patch zurückgeworfen.
- Vanilla-Inhalt **abschalten**: gleichnamige Datei mit leerem Inhalt anlegen (nur BOM/Kommentar). Das ist billig und patchsicher.
- Vanilla-Inhalt **ändern**: eigenes Objekt in eigener `va_`-Datei anlegen, wo möglich mit `INJECT:`/`REPLACE:`/`TRY_INJECT:` statt Dateikopie (Unterstützung pro Ordner in der Doku/Wiki prüfen).
- Lässt sich eine Vollkopie nicht vermeiden: in `.claude/ABLAUFPLAN.md` unter „Bewusste Vanilla-Overrides“ mit Grund eintragen. Nur was dort steht, wird bei Patches nachgezogen.
- `replace_paths` in `.metadata/metadata.json` wirft den ganzen Vanilla-Ordner weg. Nur für Ordner, die wirklich komplett ersetzt werden (Karte, History, Strategic Regions).

## Konventionen

- Eigene Dateien: Präfix `va_` bzw. `VA_` (z. B. `common/cultures/va_orc_cultures.txt`, `common/history/states/VA_kalimdor_states.txt`). Neue Dateien klein geschrieben mit `va_`.
- Länder-Tags: ausgeschriebene Großbuchstaben-Namen (`AHNQIRAJ`, `SILVERMOON`), Definition in `common/country_definitions/VA_<kontinent>.txt`.
- States: `STATE_<NAME>` in `map_data/state_regions/NN_va_<region>.txt`, History in `common/history/states/VA_<region>.txt`.
- Events: `namespace = <thema>_events`, IDs `<namespace>.<n>`, Loc-Keys `<id>.t` / `.d` / `.f` / `.a`, `.b` …
- Journal Entries: `je_<thema>`, Datei `common/journal_entries/VA_<thema>.txt`.
- Lokalisierung: `localization/replace/<sprache>/…_l_<sprache>.yml`, **UTF-8 mit BOM**, erste Zeile `l_english:`, Einträge mit zwei Leerzeichen eingerückt. Englisch ist Pflicht, Deutsch optional.
- Script-Dateien (`.txt`) ebenfalls UTF-8 mit BOM, Einrückung mit Tabs wie in Vanilla.

## Content-Ablauf (Events, JEs, Entscheidungen)

1. Christian liefert die Idee (Lore, beteiligte Länder/States, gewünschter Effekt).
2. Claude sucht ein passendes Vanilla-Vorbild (gleicher Mechanik-Typ) und prüft Effekte/Trigger in der Script-Doku.
3. Claude schreibt Script **und** englische Lokalisierung zusammen. Keine Loc-Keys ohne Text, keine Texte ohne Key.
4. Platzhalter-Grafiken (Icons, `event_image`) aus Vanilla verwenden und als `# TODO:` markieren, wenn eigene Grafik gewünscht ist.
5. Christian testet im Spiel, Claude wertet danach `error.log` aus (nur Zeilen mit Mod-Pfaden sind relevant).

## Arbeitsweise

- Die Datei `error.log` ist die einzige verlässliche Prüfung; ein Parser/Build existiert nicht. Nach Änderungen um einen Spielstart bitten statt Korrektheit zu behaupten.
- Große Binärdateien (Karte, Heightmap, `.bin`, `.dds`) nicht anfassen, außer ausdrücklich verlangt.
- Achtung: Der Ingame-Map-Editor schreibt in den geladenen Mod-Ordner (`mod\warcraft`), nicht ins Repo. Nach Kartenarbeit daran erinnern, die Dateien ins Repo zurückzuholen.
- Git: nur lesen (siehe globale Vorgaben).
