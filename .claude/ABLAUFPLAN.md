# Ablaufplan Victorian Azeroth

Stand: 2026-10-29. Spiel: **1.13.11**, Mod deklariert: **1.13.\***. Letzter Commit: 2025-12-02.

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
3. Danach Content-Fokus: **Undercity** (dabei VA-067 Sylvanas stirbt früh), **Scarlet Crusade** (VA-041, VA-035) und **Gilneas** (VA-007), ggf. Gilneas als Schwerpunkt.

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

- 2026-11-13: **Release Version 3 vorbereitet** (VA-072): Zul'Jarra-Runde getestet, Balance Shadowpine/Schatzjäger, Korridor-Abbruch, Formable `AMANI_EMPIRE` (13 States, 9 nötig, Wappen getauscht), 554 von 571 AI-WRITTEN-Texten von Kono abgenommen (Troll-, Wretched- und Hochelfen-Ton, Stilregel im Skill `va-content`), Ländernamen Quel'Thalas, erstes eigenes Event-Bild (`va_eversong_road_home.dds`), `metadata.json` Version 3, Workshop-Text `releases/version_3_workshop.md`. Nachtests nach dem Release: T-073–T-076, T-113 Rest, T-131, Log T-077/T-118. Offen: 17 Texte außerhalb Quel'Thalas, `mod\warcraft` befüllen (Kono).
- 2026-11-03: error.log-Großputz (VA-043/VA-003/VA-026/VA-014, wartet auf Spieltest): 30 alte Vanilla-Kopien gelöscht (On-Actions, politische Bewegungen, Scripted Effects, Flaggen, Machtblock-Namen, Custom Loc, Terrain …), 5 Erde-Decisions abgeschaltet, `gov_archmage` nach `00_va_monarchies.txt`; Erde-`geographic_regions` und 268 Erde-JEs als leere Hüllen (Werkzeuge `va_gen_geo_regions.py`, `va_gen_earth_je_stubs.py`); Startgesetze nach Spiel-Fallback, History-Provinzen in Pandaria/Northrend, Kalimdor-PMs, Gilneas-Kopien, Loc-Keys mit `’`/`Ö`. Gebäude-Kopien warten auf Löschung durch Kono.
- 2026-11-01: Token-Optimierung: Code-Karte `KARTE.md` und vier Skills unter `skills/` (`va-content`, `va-testrunde`, `va-karte`, `va-patch-upload`); Checklisten in den Skill verschoben; `CLAUDE.md` gestrafft, Regel „Wissenspflege“ (Claude pflegt Karte und Skills selbst). `TESTPROTOKOLL.md` von 18.084 auf 516 Zeilen (Leerzeilen). `va_errlog.py --mod`. Vorlagen erfüllen VA-009 (wartet auf Kono). Script-Doku neu erzeugt (VA-052 erledigt). Archiv eingeführt: abgeschlossene Testrunden in `TESTPROTOKOLL_ARCHIV.md`, erledigte/verworfene Tickets in `tickets/archiv/`. Gefunden: veraltete Script-Doku (VA-052), Länderfarbe 487 (VA-043). Community Mod Framework geprüft und verworfen: Kompatibilitätsschicht für Erde-Mods, überschreibt Parteien/War Goals/GUI.
- 2026-10-30: Todesschneise heilen (VA-046, wartet auf Spieltest): JE `je_va_dead_scar` für jeden Besitzer, sechs Balken à 20 Monate, Schalter je Region, Kosten über staatliche Ritual Site (Löhne, Mana, Bürokratie). Ersetzt das Silvermoon-Ritual aus VA-020. Werkzeug `va_gen_dead_scar.py`.
- 2026-10-30: Silvermoon-Ziele (VA-020, wartet auf Spieltest): drei JEs ab Spielstart – Deathholme vertreiben, Zul'Aman zerstören, Todesschneise per Heilritual (Knopf, 24 Monate je Region, ruht im Mana-Entzug) heilen. Events `silvermoon_events.1`–`.4`. Wretched folgt mit VA-021, Sunwell-Projekt später. Ablauf `.claude/ablauf/silvermoon.md`.
- 2026-10-30: Quel'Thalas-Grundbausteine (VA-019, wartet auf Spieltest): Mana als Stimulans mit Obsession der Elfen, Start-Ley-Line-Tap auf Sunwell Plateau, Todesschneise an State-Regionen (Lebenden-Malus nur ohne untote Mehrheit, monatlich und bei Besitzwechsel), Dauer-JE `je_mana_hunger` mit drei Preisstufen. Neue Regel: Claude-Texte enden sichtbar mit „(AI WRITTEN)“. Ablauf `.claude/ablauf/silvermoon.md`. Test-Icon im Schiffsbau → VA-045.
- 2026-10-30: KI stapelte Verwaltung und Bausektoren (VA-044): Start-Gebäude fehlten fast überall. Verwaltung für 93 EK-Länder (193 Stufen), Bausektor für 29 (45 Stufen), Werkzeug `va_add_gov_buildings.py`. Test T-039.
- 2026-10-30: Weltmarkt (VA-040): kein Land hatte eine Handelszentrale, 1.13 handelt nur darüber. 46 Start-Zentralen (134 Stufen) in den EK-Hauptstädten, Werkzeug `va_add_trade_centers.py`. `va_add_ports.py` zählte Häfen je State statt je Land, dadurch neue Häfen für Booty Bay (Steamwheedle) und Hammerfall. Kalimdor folgt nach VA-038. Test T-037, T-038.
- 2026-10-30: Editor-Stand aus `mod\warcraft` ins Repo geholt (Kalimdor-History, `23_va_north_kalimdor.txt`, `provinces.png`, Splines, Locators; VA-038). 70 Strategic Regions mit eigener Farbe statt Gelb, Kleidung über `va_clothes_triggers.txt` (VA-042). 8 leere `add_ownership` in Nord-EK-Gebäuden gefüllt, 70 Mod-Dateien mit BOM versehen, Rest aus dem Log → VA-043. Tests T-031 bis T-033.

- 2026-10-30: 106 Start-Häfen (21–28), Ackerland für fünf Nord-EK-States, Pops gekürzt in Undercity, Scholomance, Shadowfang Keep (VA-029, VA-024).
- 2026-10-30: Süd-EK Start-Gebäude mit Länderprofilen: +319 Stufen; 296 Fischerei-Platzhalter im Binnenland entfernt (VA-029). Werkzeug `va_profiles.py`.

- 2026-10-30: Neue History-Ordner seit 1.11 abgefangen (VA-004): `history/ai`, `diplomatic_plays`, `government_setup`, `governments`, `lobbies`, `military_deployments`, `military_formations`, `trade`, `treaties` in `replace_paths` (reine Erde-Inhalte). `cultures` und `political_movements` per leerer Datei abgeschaltet, allgemeiner Teil als `va_cultures.txt`/`va_movements.txt`. `conscription` bleibt Vanilla (allgemein).

- 2026-10-30: Mittel-EK Start-Gebäude nach Maßstab Frankreich: +388 Stufen (VA-029).

- 2026-10-30: Nord-EK Start-Gebäude nach Maßstab Frankreich 1836: +85 Stufen; Eisen 27 → 14, Holz 99 → 77, Fischerei 45 → 27 gekürzt (VA-029). Werkzeuge `va_region_overview.py`, `va_fill_buildings.py`.

- 2026-10-30: `common/company_types` und `common/character_templates` aus `replace_paths` genommen (VA-002 Teil 3). 223 Erde-Dateien per leerer Datei abgeschaltet, Standardvorlage als `00_default_template.txt` auf 1.13 gebracht. Offen: alte `99_basic_companies.txt` zurückholen (siehe VA-002).

- 2026-10-30: `common/journal_entries` und `common/scripted_buttons` aus `replace_paths` genommen (Entscheidung Kono). 178 Erde-Dateien per leerer Datei abgeschaltet, 20 alte Kopien gelöscht, 7 allgemeine Eventdateien wieder aktiv (VA-002 Teil 2).
- 2026-10-30: `events`, `events/india_events`, `events/soi_events` aus `replace_paths` genommen (Entscheidung Kono). 122 Erde-Eventdateien per leerer Datei abgeschaltet. 119 alte Kopien gelöscht, 27 geleert (VA-002).

- 2026-10-29: 29 Kartendateien und Menü-Video aus dem Upload-Ordner ins Repo geholt (noch nicht committet).
- 2026-10-29: 134 Dateien gelöscht (noch nicht committet, Kategorien überschneiden sich teilweise):
  - 67 leere Platzhalter in `replace_paths`-Ordnern (wirkungslos, Vanilla-Ordner ist dort ohnehin ersetzt), darunter die leeren `character_templates/va_*_charakters.txt`
  - 29 Kopien identisch mit Vanilla 1.13 außerhalb von `replace_paths`
  - 25 alte Vanilla-Kopien, deren Original Vanilla inzwischen umbenannt hat und die dadurch doppelt luden: `laws/00_*` (15), `tech_events` (5), `scripted_effects/00_ip3_victoria_scripted_effects.txt`, `events/subject_interaction_evts.txt`, Decisions `canada_australia`, `ionian_islands`, `hawaii_decisions`
  - 6 leere Achievement-Dateien mit alten Namen, 6 `.info`-Doku-Kopien, `history/trade_routes` und `history/interests` (gibt es in Vanilla nicht mehr)
  - Liste aller gelöschten Dateien: `git status` bzw. `git diff --stat`
- 2026-10-29: 37 weitere alte Kopien gelöscht (noch nicht committet): `interest_groups`, `ideologies`, `laws`, `government_types` (ohne `01_monarchies`), `portrait_modifiers`, `ai_strategies` – siehe VA-003.

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
