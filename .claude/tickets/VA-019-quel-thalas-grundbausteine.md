# VA-019: Quel'Thalas – Mana und Todesschneise (Grundbausteine)

- **Status:** in Arbeit
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Gemeinsame Bausteine für Silvermoon, Wretched und Deathholme: Länder-Variable `va_mana` mit Scripted Progress Bar, Mangel-/Überschuss-Modifier, State-Modifier `va_dead_scar` auf den Ghostlands-States. Muss vor VA-020 bis VA-022 stehen. Ersetzt das leere Gerüst `je_silvermoon_wretched_elfes` (VA-008).

Konzept: [../konzepte/quel_thalas.md](../konzepte/quel_thalas.md)

## Notizen

- 2026-10-30: **Entscheidung Kono: Mana wird ein echtes Handelsgut**, keine Variable. Umfang:
  - Gut `mana` in neuer Datei `common/goods/va_goods.txt` (Vorbild Vanilla `00_goods.txt`, z. B. `opium` mit `obsession_chance`), Icon vorerst aus Vanilla (`# TODO:` eigene Grafik), Loc.
  - Nachfrage: in ein Pop-Bedürfnis aufnehmen (Vanilla `common/pop_needs/00_pop_needs.txt`, per `INJECT:` prüfen) und als Obsession bei `sin_dorei`/`quel_dorei`.
  - Angebot: Produktionsgebäude bzw. PM noch offen (Mana-Kristalle als Ressource? Sonnenbrunnen als Monument auf `STATE_SUNWELL_PLATEAU`?) → Kono fragen, bevor Gebäude gebaut werden.
  - Achtung VA-003: `buildings`/`production_methods` im Mod sind alte Vanilla-Kopien. Neue Mana-Gebäude in eigene `va_`-Dateien, nicht in die Kopien.
- Die Todesschneise (`va_dead_scar`) bleibt ein State-Modifier.
- 2026-10-30: **Angebot geklärt (Kono): Mana stammt aus Leylinien** und ist eine abbaubare Ressource.
  - Abbaugebäude (Arbeitsname `building_leyline_tap`) mit eigener Building Group und PMs, Vorbild Vanilla `building_coal_mine` (`common/buildings/03_mines.txt`, PMGs in `common/production_method_groups/03_mines.txt`).
  - Verteilung als `capped_resources` (1.13-Format: `building_leyline_tap = N`) in den State Regions, Schwerpunkt Quel'Thalas. Verteilung vor dem Eintragen mit Kono abstimmen.
  - Später (eigenes Ticket): Mana als Vorprodukt für magische Gegenstände und als Antrieb von Produktionen (PMs analog Kohle/Strom).
- 2026-10-30: **Mana-Grundgerüst angelegt** (nicht getestet):
  - `common/goods/va_goods.txt` – Gut `mana` (industrial, Preis 40, Icon vorerst Strom)
  - `common/building_groups/va_building_groups.txt` – `bg_leyline_tapping` (Eltern: `bg_mining`)
  - `common/buildings/va_mana_buildings.txt` – `building_leyline_tap`, ab Spielstart baubar, Icon vorerst Kohlemine
  - `common/production_method_groups/va_mana_production_method_groups.txt`, `common/production_methods/va_mana_production_methods.txt` – eine PM `pm_focus_crystals_building_leyline_tap` (5 Werkzeug → 20 Mana, 4.000 Arbeiter + 500 Akademiker)
  - `common/modifier_type_definitions/va_mana_modifier_types.txt` – `goods_output_mana_add`, `goods_input_mana_add`, `building_leyline_tap_throughput_add` (Vanilla definiert diese je Gut/Gebäude)
  - `localization/replace/english/va_mana_l_english.yml`
- **Leylinien-Verteilung (Vorschlag, in `26_va_north_eastern_kingdoms.txt` eingetragen):** Sunwell Plateau 40, Magisters' Terrace 25, Silvermoon City 20, Duskwither Spire 20, West/East Sanctum je 15, Dalaran Crater 15, Sun's Reach/Sunstrider Isle/Sanctum of the Sun/Dawnstar Spire je 10, Farstrider Retreat/Sunsail Anchorage/Ruins of Silvermoon/Tranquillien/Suncrown Village/Windrunner Village je 5. Ohne Leylinien: Deathholme, Tor Watha, Zul'Aman (Todesschneise bzw. Troll-Land). Kono bestätigt oder korrigiert.
- **Offen (präzisiert unten, 2026-10-30):** Nachfrage fehlt noch. Ohne Abnehmer fällt der Mana-Preis auf das Minimum → als Nächstes Pop-Bedürfnis/Obsession (Sin'dorei) oder erste Mana-verbrauchende PMs. Leylinien außerhalb Nord-EK (Karazhan, Kalimdor, Northrend …) später.
- 2026-10-30: **Kono: Verteilung passt fürs Erste.** Verbrauch kommt später über (a) Produktionsmethoden, die Mana verbrauchen, und (b) die Bevölkerung der Blutelfen (`sin_dorei`) und Hochelfen (`quel_dorei`), also Pop-Bedürfnis/Obsession. Beides ist noch nicht gebaut. Nächster Schritt in diesem Ticket: Todesschneise (`va_dead_scar`).
- 2026-10-30: Testfälle im [Testprotokoll](../TESTPROTOKOLL.md), Runde 1: T-010 bis T-012.
- 2026-10-30: T-010 bis T-012 OK. Ley Line Tap baubar, Mana am Markt. Gebäude-Icon (Kohlemine) und Mana-Icon (Strom) noch Platzhalter, in VA-027 gelistet.
- 2026-10-30: **Nachfrage präzisiert (Kono):** Mana ist für Blutelfen (`sin_dorei`) und Hochelfen (`quel_dorei`) eine **Obsession** (wie Opium/Tee in Vanilla). Zusätzlich eine **Abhängigkeit**: Je nach Mana-Zugang gibt es Mali oder Boni.
  - Baustein 1, Obsession: In den beiden Kulturen `obsessions = { mana }` eintragen, beim Gut `obsession_chance` setzen und Mana in ein Pop-Bedürfnis aufnehmen. Vorbilder: Vanilla `opium` in `00_goods.txt`, Kultur-`obsessions` in `common/cultures/`, `common/pop_needs/00_pop_needs.txt`. Syntax vor dem Schreiben in Vanilla 1.13 und der Script-Doku prüfen.
  - Baustein 2, Abhängigkeit: Mana-Versorgung der Elfen-Pops bzw. des Markts monatlich auswerten und gestufte Modifier vergeben, z. B. Mangel → Malus (Zustimmung, Arbeitsleistung, Radikale; Richtung „Wretched“, VA-021), gute Versorgung → Bonus. Vorbild für die Mechanik suchen: Marktknappheit-Trigger plus Modifier über On-Action oder JE-Pulse. Stufen und Werte mit Kono abstimmen.
  - Reihenfolge: zuerst Baustein 1 (damit der Mana-Preis nicht mehr am Minimum liegt), dann Baustein 2. Die Todesschneise bleibt in diesem Ticket offen.
- 2026-10-30: **Baustein 1 (Obsession) angelegt**, nicht getestet:
  - `common/cultures/va_elfen_cultures.txt`: `obsessions = { mana }` bei `quel_dorei` und `sin_dorei`.
  - `common/goods/va_goods.txt`: `obsession_chance = 0.5` (niedrigste Vanilla-Stufe, damit andere Kulturen Mana kaum als dynamische Obsession bekommen).
  - Neu `common/pop_needs/va_pop_needs.txt`: `INJECT:popneed_intoxicants` mit Eintrag Mana (Gewicht 0.25, max. Anteil 0.5). Offen: ob `INJECT` den wiederholten Schlüssel `entry` anhängt oder alle Vanilla-Einträge ersetzt. Prüft T-040; ersetzt er, bleibt nur eine bewusste Vollkopie von `popneed_intoxicants` (dann unter „Bewusste Vanilla-Overrides“).
  - Nebenbefund: `quel_dorei` hat `tradition_magical_lowlands` doppelt in `traditions`.
  - Tests T-040, T-041. Danach Baustein 2 (Abhängigkeit, gestufte Modifier).
