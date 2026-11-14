# Tickets

Eine Datei pro Ticket: `VA-<nr>-<kurztitel>.md`. Nummern fortlaufend, nie wiederverwenden.
Die Tabelle unten listet nur **offene** Tickets (alles außer `erledigt`/`verworfen`). Erledigte und verworfene Tickets wandern samt Tabellenzeile nach `archiv/` bzw. [`archiv/README.md`](archiv/README.md) (Historie).
Nächste freie Nummer über beide Tabellen: `grep -ho "VA-[0-9]*" .claude/tickets/README.md .claude/tickets/archiv/README.md | sort -t- -k2 -n | tail -1`

## Felder

- **Status:** `offen` · `in Arbeit` · `wartet` (auf Kono/Spieltest) · `erledigt` · `verworfen`
- **Typ:** `content` · `technik` · `bug` · `aufraeumen` · `grafik`
- **Priorität:** `hoch` · `mittel` · `niedrig`

Aufbau: Beschreibung, **Stand** (was gilt), **Offen** (mit nächstem Schritt), kurze Notizen. Ein Ticket ist in einer Session erledigbar und bleibt unter 10.000 Zeichen (`va_doku_check.py`). Größeres wird ein Sammelticket mit Teiltickets; lange Verläufe wandern wortgleich nach `verlauf/VA-NNN-….md` (nur bei Bedarf lesen).
Neues Ticket: Kono sagt „Ticket: …“, oder Claude legt es an, wenn nebenbei etwas auffällt; Zeile unten eintragen und ggf. in „Als Nächstes“ einsortieren.

## Als Nächstes (Claude pflegt die Reihenfolge)

Kono sagt **„nimm das nächste Ticket“** → oberstes Ticket dieser Liste nehmen. Nennt Kono ein **Thema**, die Themenzeile unten nutzen: dort das Ticket mit der höchsten Priorität, das nicht wartet. Nach jedem Abschluss die Liste nachziehen (Erledigtes raus, 5–8 Einträge, Fokus aus `ABLAUFPLAN.md`).

| # | Ticket | Nächster Schritt |
|---|---|---|
| 1 | VA-075 | Gilneas-Startzustand: Mauer-Gesetz nach `law_sakoku`, Startgesetze, Crowley im Kerker |
| 2 | VA-076 | Fluch-JE mit Balken je State und Paranoia-Variable |
| 3 | VA-077 | Fraktions-JE nach `je_divided_monarchists` |
| 4 | VA-078 | Nachtelfen-JE, Ritual, Religionswechsel |
| 5 | VA-069 | Fehlende Namen für Sprachen, Traditionen, Erbe-Merkmale (Lint/error.log) |
| 6 | VA-043 | Länderfarbe außerhalb 0–255 in `VA_outlands.txt` (Kleinigkeit) |
| 7 | VA-023 | Lint-Altlasten abbauen (Lückenfüller) |

**Wartet auf Kono** (nicht von selbst nehmen): Spieltests im `TESTPROTOKOLL.md`; Karte neu zeichnen VA-038, VA-030, VA-037; `mod\warcraft` befüllen VA-072; Todesmeldung Sylvanas VA-067; Herrscher-Liste VA-016; Pop-Größe VA-055; Allianz-Markt VA-036.

## Themen

| Thema | Tickets |
|---|---|
| Gilneas | VA-007 (Sammel), VA-075 bis VA-082, VA-073 |
| Quel'Thalas | VA-019, VA-021, VA-022, VA-047, VA-050, VA-056, VA-066, VA-068, VA-071, VA-017 |
| Undercity, Scarlet, Untote | VA-041, VA-035, VA-067, VA-048 |
| Karte, Startwerte, Ressourcen | VA-011, VA-015, VA-018, VA-024, VA-029, VA-030, VA-031, VA-032, VA-033, VA-037, VA-038, VA-049, VA-051, VA-055, VA-061, VA-064, VA-070 |
| Welt, Diplomatie, KI | VA-013, VA-028, VA-034, VA-036, VA-053, VA-054, VA-065 |
| Loc, Grafik | VA-006, VA-027, VA-042, VA-045, VA-060, VA-069 |
| Technik, Altlasten, Release | VA-002, VA-003, VA-009, VA-010, VA-012, VA-014, VA-016, VA-023, VA-026, VA-043, VA-059, VA-063, VA-072 |

## Übersicht

| Ticket | Titel | Typ | Prio | Status |
|---|---|---|---|---|
| [VA-002](VA-002-replace-paths-verschlanken.md) | replace_paths verschlanken | technik | hoch | wartet (Spieltest) |
| [VA-003](VA-003-vanilla-kopien-pruefen.md) | Verbleibende Vanilla-Kopien abbauen | aufraeumen | hoch | in Arbeit |
| [VA-006](VA-006-laendernamen-loc.md) | Lokalisierung der Ländernamen | content | hoch | offen |
| [VA-007](VA-007-gilneas-loc.md) | Gilneas – Worgen-Reihe (Sammelticket) | content | hoch | in Arbeit |
| [VA-009](VA-009-content-vorlagen.md) | Vorlagen für Event, JE und Decision | technik | mittel | wartet (Kono) |
| [VA-010](VA-010-kopierskript.md) | Kopierskript Repo → Upload-Ordner | technik | niedrig | offen |
| [VA-011](VA-011-state-history-provinzen.md) | State-History: Provinzen in mehreren State Regions | bug | hoch | offen |
| [VA-012](VA-012-strait-definitions.md) | Vanilla-Meerengen/Kanäle abschalten | bug | hoch | wartet (Spieltest) |
| [VA-013](VA-013-ki-regionsgewichtung.md) | KI-Regionsgewichtung für Azeroth | content | niedrig | offen |
| [VA-014](VA-014-gesetze-history.md) | Unzulässige Start-Gesetze in der Länder-History | bug | mittel | wartet (Spieltest) |
| [VA-015](VA-015-nord-ek-mechanik.md) | Nord-EK – Karte, Besitz, Ressourcen bereinigen | bug | hoch | wartet (Spieltest) |
| [VA-016](VA-016-nord-ek-herrscher.md) | Nord-EK – historische Herrscher | content | hoch | offen |
| [VA-017](VA-017-nord-ek-formables.md) | Nord-EK – Formables | content | hoch | in Arbeit |
| [VA-018](VA-018-state-test-aufloesen.md) | STATE_TEST auflösen | bug | mittel | offen |
| [VA-019](VA-019-quel-thalas-grundbausteine.md) | Quel'Thalas – Mana und Todesschneise (Grundbausteine) | content | hoch | wartet (Spieltest) |
| [VA-021](VA-021-wretched-vereinigung.md) | Wretched – Mana-Hunger und Vereinigung mit Silvermoon | content | mittel | wartet (Spieltest) |
| [VA-022](VA-022-amani-deathholme-jes.md) | Amani und Deathholme – Journal Entries | content | mittel | wartet (Spieltest) |
| [VA-023](VA-023-lint-altlasten.md) | Lint-Altlasten abbauen | aufraeumen | mittel | offen |
| [VA-024](VA-024-nord-ek-startwerte.md) | Nord-EK – Pops, Start-Gebäude und Startwerte | content | hoch | offen |
| [VA-026](VA-026-geo-regionen-machtblock-namen.md) | Vanilla geographic_regions und power_bloc_names mit Erde-Bezug | bug | mittel | wartet (Spieltest) |
| [VA-027](VA-027-platzhalter-grafiken.md) | Platzhalter-Grafiken durch eigene ersetzen | grafik | niedrig | offen |
| [VA-028](VA-028-vulkan-states.md) | Vulkangebiete Azeroths für Naturkatastrophen | content | niedrig | offen |
| [VA-029](VA-029-start-gebaeude-hungersnot.md) | Ressourcen und Start-Gebäude außerhalb Nord-EK (Hungersnot) | content | hoch | in Arbeit |
| [VA-030](VA-030-vashjir-provinzen.md) | Vashj'ir – Provinzen neu zeichnen, Ressourcen | grafik | mittel | offen |
| [VA-031](VA-031-rogue-provinzen.md) | Rogue-Provinzen im Süden entfernen | technik | mittel | in Arbeit |
| [VA-032](VA-032-inseln-provinzen-unterteilen.md) | Zandalar, Kul Tiras, Verlorene Inseln, Draenor – Provinzen unterteilen | technik | mittel | offen |
| [VA-033](VA-033-sued-ek-kartenbefunde.md) | Süd-EK – Hubs und State-History-Provinz bereinigen | bug | niedrig | offen |
| [VA-034](VA-034-startevent-eventgruppen.md) | Startevent – Event-Übersicht und Zeitplan der Eventgruppen | content | mittel | offen |
| [VA-035](VA-035-ebon-blade-scarlet-start.md) | Ebon Blade gegen Scarlet Crusade zum Spielstart | content | mittel | offen |
| [VA-036](VA-036-allianz-markt.md) | Allianz – gemeinsamer Markt für Ironforge, Gnomeregan und Stormwind | technik | hoch | offen |
| [VA-037](VA-037-ek-impassable-port.md) | Eastern Kingdoms – falsche impassable- und port-Einträge entfernen | bug | hoch | offen |
| [VA-038](VA-038-kalimdor-sanierung.md) | Kalimdor von Grund auf sanieren (Provinzen und States) | technik | hoch | in Arbeit |
| [VA-041](VA-041-scarlet-empire.md) | Scarlet Crusade → Scarlet Empire | content | mittel | offen |
| [VA-042](VA-042-portraits-kleidung-kartenfarben.md) | Charakter-Kleidung (Lumpen) und Kartenfarben der Regionen | grafik | mittel | in Arbeit |
| [VA-043](VA-043-errorlog-befunde-3010.md) | error.log 30.10. – Restbefunde aus Mod-Dateien | bug | mittel | wartet (Spieltest) |
| [VA-045](VA-045-schiffsbau-test-icon.md) | Schiffsbau-Tab zeigt Test-Icon (Smiley) | grafik | niedrig | offen |
| [VA-047](VA-047-korridor-tranquillien.md) | Silvermoon – Korridor nach Tranquillien | content | hoch | wartet (Spieltest) |
| [VA-048](VA-048-untoten-system.md) | Untoten-System – Status, Ausrottung oder Inklusion | content | hoch | offen |
| [VA-049](VA-049-bevoelkerung-vielfalt.md) | Bevölkerung weltweit zu eintönig | content | mittel | in Arbeit |
| [VA-050](VA-050-blutelfen-koenigreich.md) | Blutelfen – Gründung eines eigenen Königreichs | content | mittel | offen |
| [VA-051](VA-051-provinz-terrain.md) | Provinz-Terrain zufällig (Berg, Feld) | bug | mittel | wartet (Spieltest) |
| [VA-053](VA-053-portale-verbindungen.md) | Portale und Verbindungen – Dunkles Portal, Dalaran, Tiefenbahn | content | mittel | offen |
| [VA-054](VA-054-heldengruppen.md) | Heldengruppen – Menü für Kopfgeld und Dungeons (Machbarkeit) | technik | niedrig | offen |
| [VA-055](VA-055-pop-groesse-zombie.md) | Ungültige Pop-Größe „zombie“ in Outland | bug | niedrig | offen |
| [VA-056](VA-056-kaelthas-legion.md) | Kael'thas und die Brennende Legion – Alternative für die Wretched | content | mittel | offen |
| [VA-059](VA-059-gfx-map-altkopien.md) | Alte Vanilla-Kopien unter `gfx/map` aufräumen | technik | mittel | offen |
| [VA-060](VA-060-festungs-locators.md) | Festungs-Locators für Azeroth (Vanilla-Erde-Positionen ersetzt) | grafik | niedrig | wartet (Spieltest) |
| [VA-061](VA-061-dynamische-masken-erde.md) | Dynamische Masken für übrige Kontinente (EK fertig, Rest leer) | grafik | mittel | offen |
| [VA-063](VA-063-patch-1-15.md) | Patch 1.15 (1.14 übersprungen) | technik | hoch | in Arbeit |
| [VA-064](VA-064-kupfer-vorkommen.md) | Kupfer-Vorkommen in Azeroth (neues Gut seit Patch) | content | mittel | wartet (Spieltest) |
| [VA-065](VA-065-silvermoon-horde.md) | Machtblöcke zerfallen (Horde, Allianz, …) | bug | hoch | wartet (Spieltest) |
| [VA-066](VA-066-silvermoon-charaktere.md) | Silvermoon – eigene Charaktere | content | mittel | wartet (Spieltest) |
| [VA-067](VA-067-lebensdauer-historische-figuren.md) | Sylvanas stirbt nach 3–4 Jahren | bug | hoch | offen |
| [VA-068](VA-068-lorthemar-regent.md) | Lor'themar Theron ist Regent, nicht König | content | niedrig | wartet (Spieltest) |
| [VA-069](VA-069-fehlende-namen-kulturmerkmale.md) | Fehlende Namen für Sprachen, Traditionen und Erbe-Merkmale | lokalisierung | mittel | offen |
| [VA-070](VA-070-regionale-ressourcen.md) | Regionale Ressourcen je Kontinent (Fel Iron, Eternium, …) | content | niedrig | offen |
| [VA-071](VA-071-wretched-nachricht-anfuehrer-tod.md) | Wretched erfahren vom Tod ihres Anführers | content | niedrig | offen |
| [VA-072](VA-072-upload-version-3.md) | Upload Version 3 – Phase 1 Quel'Thalas | technik | hoch | in Arbeit |
| [VA-073](VA-073-bloodfang-alpha-prime.md) | Bloodfang-Rudel spielbar machen (Alpha Prime) | content | niedrig | offen |
| [VA-075](VA-075-gilneas-startzustand.md) | Gilneas – Startzustand (Mauer, Gesetze, Crowley im Kerker) | content | hoch | offen |
| [VA-076](VA-076-gilneas-fluch-paranoia.md) | Gilneas – Fluch-JE und Paranoia | content | hoch | offen |
| [VA-077](VA-077-gilneas-fraktionen.md) | Gilneas – Fraktionen Greymane, Godfrey, Crowley | content | hoch | offen |
| [VA-078](VA-078-gilneas-nachtelfen-religion.md) | Gilneas – Nachtelfen, Ritual von Tal'doren, Religion | content | mittel | offen |
| [VA-079](VA-079-gilneas-biss-liam.md) | Gilneas – Greymanes Biss und Liam | content | mittel | offen |
| [VA-080](VA-080-gilneas-crowley-heilmittel.md) | Gilneas – Crowley frei, Heilmittel, Crowleys Ultimatum | content | mittel | offen |
| [VA-081](VA-081-gilneas-godfrey.md) | Gilneas – Godfreys Machtgriff, Aussprache und Verrat | content | mittel | offen |
| [VA-082](VA-082-gilneas-mauerfall-forsaken.md) | Gilneas – Mauerfall und Forsaken-Krieg | content | mittel | offen |
