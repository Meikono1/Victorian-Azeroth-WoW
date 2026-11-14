# Ablaufplan Victorian Azeroth

Stand: 2026-11-14. Mod deklariert **1.15.\*** (`.metadata/metadata.json`), Spielversion prüfen laut `CLAUDE.md`.

Hier stehen Fahrplan, offene Entscheidungen und Grundsätzliches. Konkrete Aufgaben stehen als Tickets in [`tickets/`](tickets/README.md).

**Nächster Spieltest:** [Testprotokoll](TESTPROTOKOLL.md) enthält nur noch offene Testfälle (42); alles mit OK steht je Runde im [Archiv](TESTPROTOKOLL_ARCHIV.md) (Stand 2026-11-12). Release Quel'Thalas (Kono 2026-11-12: schnell, Blocker sind nur nicht feuernde Events und übrig gebliebene AI-WRITTEN-Texte): Sitzung 2 Wretched erledigt bis auf Rest (2026-11-12: T-073 Stufen-Frage, T-074/075 Felendren nach Exil-Fix, T-076 Mana-Aufstand), Sitzung 3 Zul'Jarra erledigt bis auf Rest (2026-11-12: T-113 drittes/viertes Loa, Nachtest T-131 Balance und Korridor-Abbruch), danach error.log (T-118, T-077) nach einem Silvermoon-Spiel. Formable Amani-Reich in Version 3 gescriptet (VA-017, Test T-132). Offene Buff-/Balance-Tests (T-108, T-120, T-129, T-130) blockieren den Release nicht. Rund 560 AI-WRITTEN-Texte in den Quel'Thalas-Loc-Dateien müssen vor dem Release von Kono abgenommen werden.

## Fokus: Release Silvermoon und Zul'Jarra (Stand 2026-11-12, vor Session-Schnitt)

Reihenfolge laut Kono:
1. **Testphase** (Kono): Runden 21 und 22 im Testprotokoll (T-111 bis T-124), dazu ältere Quel'Thalas-Fälle (Mana T-041 bis T-048, Ziele T-049 bis T-052, Todesschneise, Korridor, Wretched, T-021). T-042 OK. **T-123 erneut** (Mana-Grundbedarf wirkte nicht: Modifier-Typ fehlte, behoben). Kono nennt OK-Nummern, Claude hakt ab; danach error.log-Fälle T-041, T-115, T-118 auswerten.
2. **Texte** an die Ablaufdiagramme `ablauf/silvermoon.md` und `ablauf/amani.md` anpassen (Kono überarbeitet, Claude gleicht ab).
3. **Version fertig:** Upload-Ticket [VA-072](tickets/VA-072-upload-version-3.md) (angelegt 2026-11-12: Lint 0 neu, TODOs zugeordnet, 569 AI-WRITTEN, Release-Zahlen; Blocker-Tests dort als Tabelle). VA-063 abschließen.

Offen dabei: VA-067 (Sylvanas stirbt früh, Kono achtet auf Todesmeldung), VA-065 (Horde), VA-068 (Regent-Titel), VA-016 übrige Herrscher. Mana-Werte (Grundbedarf 3,0, Maßnahmen) sind Vorschläge, nach T-123/T-124 justieren (`common/script_values/va_mana_values.txt`).

## Nach dem Release Version 3 (Kono 2026-11-13)

1. Spieler-Feedback zum Release einsammeln; Nachtests T-073–T-076, T-113 (Rest), T-131, T-132, Log T-077/T-118. AI-WRITTEN-Abnahme (`abnahme/ai_written_version_3.md`).
2. Übrige Nord-EK-States durchgehen (VA-016 Herrscher u. a.).
3. Content-Fokus: **Gilneas** ist Schwerpunkt (Kono 2026-11-13). Ablauf `.claude/ablauf/gilneas.md` mit Kono durchgesprochen (2026-11-14): drei Fraktionen nach `je_divided_monarchists`, Paranoia, Fluch, Nachtelfen, Kataklysmus nach ~10 Jahren (VA-034), Kriegsausgänge. Tickets je JE angelegt (2026-11-14): VA-075 bis VA-082 unter Sammelticket VA-007, Reihenfolge in `tickets/README.md` „Als Nächstes“. Danach **Undercity** (VA-067 Sylvanas stirbt früh) und **Scarlet Crusade** (VA-041, VA-035).

## Offene Entscheidungen

- Welche Formables für Nord-EK, welche davon als Major Formation? (VA-017)
- Herrscher-Liste Nord-EK abnicken (VA-016)
- Pops Mittel-EK-Städte Ironforge, Gnomeregan, Grim Batol: kürzen oder über Markt versorgen (VA-024, VA-036)
- Allianz-Markt: Zollunion per Machtblock-Prinzip (DLC) oder andere Lösung (VA-036)
- Startevent oder Spielregeln für Eventgruppen (VA-034)
- Hungersnot (VA-029): Region für Region; Nord-, Mittel- und Süd-EK erledigt (Süd-EK mit Länderprofilen). Kalimdor erst nach dem Neuzeichnen (VA-038), Probelauf 24 liegt bereit; Vashj'ir-Ressourcen offen
- Scarlet Empire: Träger, Weg (Formable/JE), Verhältnis zu `LORDAERON` (VA-041)

## Aktueller Fokus (Kono, 2026-10-30)

- **Claude: Eastern Kingdoms.** Weltmarkt reparieren (VA-040), dann Content, damit man im Spiel etwas erlebt: Silvermoon wiederherstellen (VA-019/020), Amani-Reich in Zul'Aman gründen (VA-022), Scarlet Empire (VA-041), Ebon Blade gegen Scarlet (VA-035).
- **Kono nebenbei:** Kalimdor neu zeichnen (VA-038), Vashj'ir neu zeichnen (VA-030), Meereszugang einzelner EK-States (VA-037). Splitter-States im Süden bleiben liegen (VA-031).

## Fahrplan

1. **Grundgerüst** – erledigt: `CLAUDE.md`, Ablaufplan, Ticketsystem, Kartenkorrektur aus Jan./Feb. 2026 ins Repo geholt, erstes Aufräumen.
2. **Spielbar auf 1.13** – VA-001, VA-002, VA-003, VA-004, VA-005
3. **Priorität Nord-EK** – VA-015 (Mechanik), VA-016 (Herrscher), VA-017 (Formables), Start-Gebäude; Prüfung mit `.claude/tools/va_check_states.py 26`. Quel'Thalas-Content nach [`konzepte/quel_thalas.md`](konzepte/quel_thalas.md): VA-019 (Grundbausteine) → VA-020 (Silvermoon) → VA-021 (Wretched) → VA-022 (Amani, Deathholme)
4. **Fehlende Texte** – VA-006, VA-007
5. **Content-Werkstatt** – VA-009, danach Content-Tickets (VA-008 …)
6. **Komfort** – VA-010

## Erledigt

Ausgelagert nach [`ERLEDIGT.md`](ERLEDIGT.md) (neueste oben). Neue Einträge dort oben anfügen.

## Content-Ideen

_(Region, Länder, Kurzbeschreibung. Ausgereifte Ideen werden zu Tickets.)_

- Gilneas: Worgen-Fluch (begonnen, VA-007)
- Quel'Thalas: Silvermoon, Wretched, Amani, Deathholme – ausgearbeitet in `konzepte/quel_thalas.md`, Tickets VA-019 bis VA-022
- Quel'Danas: Kael'thas flieht dorthin und will Kil'jaeden beschwören → Shadowsword und eine kleine Gruppe der Shattered Sun entstehen (Eventreihe, später)
- Deathholme: Ausharren und Unterwerfung unter den Lichkönig, sobald Northrend ein Geißel-Land hat (zurückgestellt, VA-022)

## Bewusste Vanilla-Overrides

_(Nur hier gelistete Vollkopien werden bei Patches nachgezogen. Format: Datei – Grund.)_
- `common/scripted_triggers/00_gfx_buildings_graphics_triggers.txt` – die 6 Stadtgrafik-Trigger aus Vanilla zeigen auf Erde-States. Ersetzt durch `always = no`. Bei Patches prüfen, ob Vanilla neue Trigger hinzufügt (sonst fehlen sie).
- `common/strait_definitions/strait_definitions.txt` – leer, Vanilla-Kanäle zeigen auf Erde-Provinzen.
- `common/character_templates/00_default_template.txt` – Vanilla-Standardvorlage plus WoW-Lebensdauer und Staatsreligion (mit `VA:` markiert). Ein `INJECT` würde `trait_generation` komplett ersetzen, also keine Ersparnis. Bei Patches Vanilla-Teil neu übernehmen.
- `common/scripted_effects/00_dynamic_state_names.txt` – beide Vanilla-Effekte (`evaluate_and_assign_state_hub_dynamic_names`, `assign_state_hub_dynamic_names`) leer, sie benennen Erde-Hubs um. Bei Patches prüfen, ob Vanilla weitere Effekte in der Datei ergänzt.
- `common/geographic_regions/0*.txt` – erzeugt von `va_gen_geo_regions.py` (gleiche Schlüssel, leer). Bei Patches neu erzeugen.
- `common/buildings/08_monuments.txt`, `10_canals.txt`, `common/power_bloc_names/00_power_bloc_names.txt`, `common/political_movements/03_pan_national_movements.txt`, `common/government_types/01_monarchies.txt`, `01_regencies.txt`, `01_social_monarchies.txt`, `05_council_republics.txt`, `common/achievements/*.txt`, `common/flag_definitions/00_flag_definitions.txt` – erzeugt von `va_gen_earth_overrides.py` (Vanilla mit `always = no` in Bedingungen mit Erde-States, -Regionen oder -Tags). Bei Patches neu erzeugen.
- `events/va_earth_event_stubs/`, `common/journal_entries/va_earth_je_stubs.txt`, `common/character_templates/va_earth_template_stubs.txt` – erzeugte Hüllen (`va_gen_earth_event_stubs.py`, `va_gen_earth_je_stubs.py`, `va_gen_earth_template_stubs.py`). Bei Patches und nach neuen Stubs neu erzeugen.
- `common/on_actions/va_on_actions_earth.txt` – keine Vollkopie, aber ein `trigger` an Vanilla-On-Actions (`historical_agitators_yearly_events`). Bei Patches prüfen, ob Vanilla dort selbst einen Trigger setzt (dann Konflikt).
- `common/defines/va_OVERWRITE_defines.txt` → `NEconomy.WORLD_MARKET_LOCATION` – Vanilla zeigt auf den Nordatlantik (Absturz). Bei Patches prüfen, ob neue Defines mit Provinz-IDs dazukommen.

## Checklisten Patch und Upload

Stehen im Skill `.claude/skills/va-patch-upload/SKILL.md` (einzige Quelle, seit 2026-11-01). Jedes Mal komplett abhaken, Ergebnis als Notiz in einem eigenen Ticket.
