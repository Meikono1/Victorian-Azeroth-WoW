# VA-019: Quel'Thalas – Mana und Todesschneise (Grundbausteine)

- **Status:** wartet (Spieltest)
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
- 2026-10-30, T-040 (Kono): `INJECT` hängt an, Vanilla-Rauschmittel bleiben. Effekt zu schwach. KI baut Ley Line Taps von selbst. Daraufhin `va_pop_needs.txt`: Intoxicants Gewicht 0.25 → 1, max. Anteil 0.5 → 0.75; neu Mana in `popneed_stimulants` (Gewicht 0.8 wie Tabak, Anteil 0.75). Folge: Auch andere Kulturen kaufen mehr Mana. Test T-042.
- 2026-10-30: **Kono: Mana ist kein Rauschmittel**, nur Stimulans. Eintrag in `popneed_intoxicants` entfernt; bleibt `popneed_stimulants` (Gewicht 0.8, Anteil 0.75, min. 0). Hebel, falls weiter zu schwach: `min_supply_share` > 0 (Nachfrage auch ohne Angebot im Markt) oder Gewicht erhöhen.
- 2026-10-30: Kono: `weight` 0.8 → 0.65, `min_supply_share` 0 → 0.1 (Mindestnachfrage auch ohne Angebot). Test T-042.
- 2026-10-30, Kono: Bedarf Stormwind 11 (15 Mio. Einwohner), Silvermoon 11 (5,1 Mio.), beide ohne Angebot. Daher 1 Stufe `building_leyline_tap` (20 Mana) als Start-Gebäude auf `STATE_SUNWELL_PLATEAU` für `SILVERMOON` in `common/history/buildings/26_north_eastern_kingdoms.txt`. Test T-043.
- 2026-10-30: **Todesschneise angelegt**, nicht getestet:
  - `common/static_modifiers/va_quel_thalas_modifiers.txt`: `va_dead_scar` (Ackerbau-Durchsatz −0,3, Infrastruktur −15 %, Bau −15 %, Sterblichkeit +0,1, Migrationssog −50 %). Icon vorerst `modifier_fire_negative` (TODO, VA-027).
  - `common/history/global/va_global_quel_thalas.txt`: setzt den Modifier zum Start dauerhaft auf `STATE_DEATHHOLME`, `STATE_SANCTUM_OF_SUN`, `STATE_TRANQUILLIEN`, `STATE_RUINS_OF_SILVERMOON` (Arthas' Weg zum Sonnenbrunnen). Kono bestätigt Auswahl/Stärke. Offen: ob ein zweiter `GLOBAL`-Block neben `00_global.txt` geladen wird (T-044).
  - Loc `localization/replace/english/va_quel_thalas_l_english.yml`. Heilung (Entfernen per JE) kommt mit VA-020, Ausbreitung durch Deathholme mit VA-022.
  - Tests T-044, T-045. Offen in diesem Ticket nur noch Baustein 2 (Abhängigkeit), Stufen/Werte warten auf Kono.
- 2026-10-30, Kono: Todesschneise auf **Sunwell Plateau, Ruins of Silvermoon, West Sanctum, East Sanctum, Tranquillien, Deathholme** (Sanctum of the Sun raus). Umgesetzt in `va_global_quel_thalas.txt`.
- 2026-10-30, Baustein 2 Vorschlag: Stufen nach Mana-Preis im eigenen Markt (Arkane Fülle ≤ Grundpreis, Knappheit ab +25 %, Mana-Entzug ab +70 %). Vanilla-Preis ist bei ±75 % gedeckelt, daher Entzug-Schwelle unter dem Maximum (Hinweis Kono). Werte noch nicht bestätigt.
- 2026-10-30, Kono: **Untote leiden kaum unter der Todesschneise.** Aufgeteilt: `va_dead_scar` (Land: Ackerbau, Infrastruktur, Bau) auf allen sechs States; `va_dead_scar_living` (Sterblichkeit +0,1, Migrationssog −50 %) nur, wenn keine untote Kultur ≥ 50 % stellt (`va_state_undead_majority_trigger` in `common/scripted_triggers/va_quel_thalas_triggers.txt`, Kulturen banshee, death_knight, forsaken, kvaldir, zombie). Anpassung per `va_update_dead_scar_living_effect` (`common/scripted_effects/va_quel_thalas_effects.txt`) zum Start und jährlich über `on_yearly_pulse_state` (`common/on_actions/va_on_actions_quel_thalas.txt`). Grenze: Vic3 hat keine Sterblichkeit je Kultur, der Malus gilt also für alle Pops eines States, entschieden wird nach Mehrheit. Offen: ob `on_actions` in der eigenen Datei an Vanillas `on_yearly_pulse_state` angehängt wird (T-044).
- 2026-10-30, Kono: **Feste Untoten-Liste.** `common/scripted_triggers/va_undead_triggers.txt`: `va_is_undead_culture_trigger` (Culture-Scope, Liste banshee, death_knight, forsaken, kvaldir, zombie) ist die einzige Stelle, an der untote Kulturen stehen. `va_state_undead_majority_trigger` fragt `va_state_undead_share` (neu `common/script_values/va_undead_values.txt`, summiert `total_size` aller untoten Pops / `state_population`) ≥ 0,5. Damit zählen gemischte Untote zusammen. `va_quel_thalas_triggers.txt` entfällt. Ungeprüft: `total_size` als Wert (Vanilla nutzt es so nicht, nur als Vergleich), T-044.
- 2026-10-30: T-044 OK (Kono). Mehrheitsprüfung über `va_state_undead_share` funktioniert, damit auch `total_size` als Wert und der zweite `GLOBAL`-Block. Noch nicht belegt: die jährliche Nachprüfung per `on_actions` aus eigener Datei (zeigt sich erst bei Besitz- oder Bevölkerungswechsel). Infrastruktur der Todesschneise −0,15 → −0,3 (Kono). Offen im Ticket: Baustein 2 (Abhängigkeit), Stufen vorgeschlagen (Entzug ab +70 %).
- 2026-10-30, Kono: Lebenden-Malus wechselte erst nach 11 Monaten (jährliche Prüfung zu langsam). Damit belegt: `on_actions` aus eigener Datei wird an Vanilla angehängt. Umbau:
  - Schneise hängt jetzt an der **State-Region** (Variable `va_dead_scar_region`, gesetzt in `va_global_quel_thalas.txt`), nicht am State. So bleibt sie bei Eroberung, Verschmelzung und neuen Teil-States erhalten.
  - `va_update_dead_scar_effect` (ersetzt `va_update_dead_scar_living_effect`) setzt/entfernt beide Modifier anhand der Variable und der Untoten-Mehrheit.
  - Prüfung monatlich (`on_monthly_pulse_state`) und sofort bei `on_state_owner_change` und `on_state_created`. Die jährliche Prüfung entfällt. Heilung (VA-020) = Variable entfernen.
  - Test T-046.
- 2026-10-30, Kono: **Alle von Claude geschriebenen Texte mit `[AI WRITTEN]` markieren** (Ausnahme: Übersetzungen, die Kono vorgibt). In Loc-Dateien als Zeilenkommentar `# [AI WRITTEN]`, weil eckige Klammern im Text als Script-Funktion gelesen würden. Nachgetragen in `va_mana_l_english.yml` und `va_quel_thalas_l_english.yml`.
- 2026-10-30, Kono: Markierung soll **im Spiel sichtbar** sein. Jetzt ` (AI WRITTEN)` am Ende jedes Claude-Textes statt Zeilenkommentar (Regel in `.claude/CLAUDE.md`).
- 2026-10-30: T-046 OK (Kono): Anpassung nach Übernahme nahezu sofort.
- 2026-10-30: **Baustein 2 (Abhängigkeit) angelegt**, nicht getestet. Stufen von Kono bestätigt:
  - `common/static_modifiers/va_mana_modifiers.txt`: `va_mana_abundance` (Preis ≤ Grundpreis: Forschung +10 %, Lebensstandard +1), `va_mana_scarcity` (ab +25 %: Lebensstandard −1, `state_radicals_and_loyalists_from_sol_change_mult` +0,1), `va_mana_withdrawal` (ab +70 %: Lebensstandard −2, Radikale/Loyale +0,25, Sterblichkeit +0,05, Durchsatz −0,1).
  - `common/scripted_triggers/va_mana_triggers.txt`: zentrale Liste `va_is_mana_dependent_culture_trigger` (sin_dorei, quel_dorei) und `va_country_mana_dependent_trigger` (Hauptkultur).
  - `common/scripted_effects/va_mana_effects.txt`: `va_update_mana_dependency_effect` prüft `market_capital.market` → `mg:mana` → `market_goods_pricier`, vergibt genau eine Stufe.
  - `common/on_actions/va_on_actions_mana.txt`: monatlich über `on_monthly_pulse_country`.
  - Loc in `va_mana_l_english.yml` (AI WRITTEN). Icons vorerst Glühbirne/Feuer (VA-027).
  - Einschränkung: Länder-Modifier wirken auf alle Pops des Landes, nicht nur auf Elfen (Vic3 kennt keine Kultur-Modifier). Für Silvermoon & Co. unkritisch, bei gemischten Ländern später prüfen.
  - Tests T-047, T-048. Danach in VA-019 offen: nichts mehr außer Testbestätigung.
- 2026-10-30, Kono: **Mana-Abhängigkeit muss ein Journal Entry sein**, ein reiner Modifier fällt erst nach vielen Stunden auf. Umgebaut:
  - Neu `common/journal_entries/va_mana.txt`: Dauer-JE `je_mana_hunger` (Innere Angelegenheiten, angeheftet), aktiv für Länder mit Mana-abhängiger Hauptkultur, ab Spielstart per `add_journal_entry` in `va_global_quel_thalas.txt`. Vergibt die Stufe beim Start und monatlich, Statuszeile zeigt die aktuelle Stufe, Beschreibung erklärt die Preisgrenzen. Ungültig, wenn keine Mana-abhängige Hauptkultur mehr → Modifier weg.
  - `common/on_actions/va_on_actions_mana.txt` gelöscht (JE übernimmt den Monatstakt).
  - Ablaufdiagramm angelegt: `.claude/ablauf/silvermoon.md`. Abschluss per Sunwell-Projekt kommt mit VA-020.
  - Loc in `va_mana_l_english.yml` (AI WRITTEN). JE-Icon vorerst `event_scales` (VA-027).
- 2026-10-30: JE läuft (Kono, Highvale in „Mana Withdrawal“). Tooltip „culture_this_equal has no localization“ behoben: `va_country_mana_dependent_trigger` und `va_state_undead_majority_trigger` in `custom_tooltip` gekapselt (Loc `_tt`, AI WRITTEN). Regel für künftige Listen-Trigger mit `this = cu:`: immer per `custom_tooltip` kapseln, wenn sie in JE/Entscheidung sichtbar sind.
- **Stand zum Session-Schnitt (2026-10-30):** VA-019 inhaltlich fertig (Mana-Gut, Leylinien, Obsession als Stimulans, Start-Tap, Todesschneise, Mana-JE). Offen: Spieltests T-041, T-043, T-045, T-047 (Tooltip), T-048; danach Ticket auf `erledigt`. Nächste Content-Schritte laut Fokus: VA-020 (übrige Silvermoon-Ziele, Ablauf in `.claude/ablauf/silvermoon.md`), optional Erklär-Event beim ersten „Mana Withdrawal“.
