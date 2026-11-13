# VA-027: Platzhalter-Grafiken durch eigene ersetzen

- **Status:** offen
- **Typ:** grafik
- **Priorität:** niedrig
- **Erstellt:** 2026-10-30

## Beschreibung

Sammelticket: Bilder, die Kono generieren soll. Im Script ist jeder Platzhalter mit `# TODO: eigenes …` markiert. Die Liste unten wird beim TODO-Durchgang (Ablaufplan, Checkliste Upload) aus dem Code nachgezogen. Fertige Bilder legt Kono als PNG ins Repo oder nennt den Pfad; Claude wandelt sie in DDS um, legt sie unter `gfx/…` ab, trägt die Pfade ein und entfernt das TODO.

**Format der Vanilla-Vorbilder** (gemessen 2026-10-30): RGBA mit transparentem Hintergrund, DDS unkomprimiert mit Mipmaps. Umwandlung: `python -I .claude/tools/va_icon.py <quelle.png> <ziel.dds> [--size N]`; Quell-PNGs nach `.claude/grafik_quellen/` (nicht in den Mod-Root, sonst landen sie im Upload). Stil wie Vanilla: gemalt, leichte Schrägansicht, kräftige Kontur, kein Text.

## Eigene Grafiken (eingebaut)

| Was | Quelle | Datei | Rechte |
|---|---|---|---|
| Event-Bild „The Wretched Healed“ (`wretched_events.5`, `events/va_wretched_events.txt`) | `.claude/grafik_quellen/photo_2020-04-29_23-17-00.jpg` (1280×914) | `gfx/event_pictures/va_eversong_road_home.dds` (2026-11-13) | Zeichnung eines Freundes von Kono, Nutzung im Mod erlaubt (Kono 2026-11-13). Fremde Bilder (z. B. JJcanvas) nur mit Erlaubnis des Künstlers. |

## Offene Grafiken

| Was | Wo im Script | Platzhalter | Größe | Ziel-Datei (Vorschlag) | Ticket |
|---|---|---|---|---|---|
| Produktionsmethode „Focus Crystals“ | `common/production_methods/va_mana_production_methods.txt:5` | Spitzhacke/Schaufel | 104×104 | `gfx/interface/icons/production_method_icons/va_focus_crystals.dds` | VA-019 |
| Produktionsmethoden „Arcane Conduits“, „Runic Resonators“, „No Attunement“, „Arcane Sigils“ | `common/production_methods/va_mana_production_methods.txt` | Pumpe, Kondensationspumpe, keine Sprengstoffe, Nitroglyzerin | 104×104 | `gfx/interface/icons/production_method_icons/va_arcane_conduits.dds`, `va_runic_resonators.dds`, `va_no_attunement.dds`, `va_arcane_sigils.dds` | VA-019 |
| Modifier-Icon „The Dead Scar“ | `common/static_modifiers/va_quel_thalas_modifiers.txt:4` | Feuer (negativ) | wie Vanilla `modifier_fire_negative.dds` | `gfx/interface/icons/timed_modifier_icons/va_dead_scar.dds` | VA-019 |
| Modifier-Icons „Arcane Abundance“, „Mana Scarcity“, „Mana Withdrawal“ | `common/static_modifiers/va_mana_modifiers.txt` | Glühbirne (pos./neg.), Feuer (neg.) | wie Vanilla `timed_modifier_icons` | `gfx/interface/icons/timed_modifier_icons/va_mana_*.dds` | VA-019 |
| Modifier-Icon „Shadow of the Dead Scar“ | `common/static_modifiers/va_quel_thalas_modifiers.txt` | Feuer (negativ) | wie Vanilla `timed_modifier_icons` | `gfx/interface/icons/timed_modifier_icons/va_dead_scar_living.dds` | VA-019 |
| JE-Icon „The Mana Hunger“ | `common/journal_entries/va_mana.txt:5` | Waage (`event_scales`) | wie Vanilla `event_icons` | `gfx/interface/icons/event_icons/va_mana_hunger.dds` | VA-019 |
| JE-/Event-Icons Silvermoon (Deathholme, Zul'Aman, Todesschneise) | `common/journal_entries/VA_silvermoon.txt`, `events/va_silvermoon_events.txt` | Totenkopf, Militär, Karte | wie Vanilla `event_icons` | `gfx/interface/icons/event_icons/va_deathholme.dds`, `va_zul_aman.dds`, `va_dead_scar.dds` | VA-020 |
| Modifier-Icons Silvermoon-Ziele (3×) | `common/static_modifiers/va_silvermoon_modifiers.txt` | Fahne pos./neg. | wie Vanilla `timed_modifier_icons` | `gfx/interface/icons/timed_modifier_icons/va_silvermoon_*.dds` | VA-020 |
| Todesschneise heilen: JE-Icon, Gebäude „Ritual Site“, PM „Ritual Circles“, Modifier „The Land Restored“, Event-Bilder `dead_scar_events.1`/`.2` | `common/journal_entries/va_dead_scar.txt`, `common/buildings/va_dead_scar_buildings.txt`, `common/production_methods/va_dead_scar_production_methods.txt`, `common/static_modifiers/va_quel_thalas_modifiers.txt`, `events/va_dead_scar_events.txt` | Karte, Verwaltung, Aktenschränke, Fahne, Vanilla-Videos | wie Vanilla | `gfx/…/va_dead_scar_*.dds`, `va_scar_ward.dds` | VA-046 |
| Korridor nach Tranquillien: JE-/Event-Icons (Karte), Modifier „Logistics Operation“ (Münzen neg.), „The Road to Tranquillien“ (Fahne), Event-Bilder `silvermoon_events.4`/`.5` (Vanilla-Videos Bau-Kolonie, Züge) | `common/journal_entries/VA_silvermoon.txt`, `common/static_modifiers/va_silvermoon_modifiers.txt`, `events/va_silvermoon_events.txt` | Karte, Münzen, Fahne, Vanilla-Videos | wie Vanilla | `gfx/…/va_silvermoon_corridor*.dds` | VA-047 |
| Wretched (Schritt 2–4 ergänzt 2026-11-03: Sucht-Stufen, Etappen-, Kopfgeld-, Aufstand-Modifier und Events `wretched_heal_events`, `wretched_bounty_events`, `mana_uprising_events`; dazu Porträts für Thaelis, Aldaron, Felendren): JE-Icon (Porträt), Modifier „Wretched Addiction“/„Wretched Addicts“ (Feuer neg.), „Healing the Wretched“ (Münzen neg.), „The Wretched Absorbed“ (Faust neg.), „The Wretched Restored“ (Fahne), Event-Bilder/-Icons `wretched_events.1–5` und `.10–.16` (Vanilla-Videos Herrscherrede, Extremismus, Parade, Laden, Polizei, Schule, Seeschlacht, Krankenhaus, vor der Schlacht), Balken „Wretched Threat“, Modifier „Unsafe Road“, „Harbor Overrun“, „Breach in the Wall“, „Apprentices Disciplined“, „War against Our Own“, „Scars of the Kinslaying“ | `common/journal_entries/VA_silvermoon.txt`, `common/static_modifiers/va_wretched_modifiers.txt`, `va_silvermoon_modifiers.txt`, `events/va_wretched_events.txt` | Porträt, Feuer, Münzen, Faust, Fahne, Vanilla-Videos | wie Vanilla | `gfx/…/va_wretched_*.dds` | VA-021 |
| Event-Bilder `silvermoon_events.2`/`.3` | `events/va_silvermoon_events.txt` | Vanilla-Videos (Leibeigene, vor der Schlacht, Parade, Herrscherrede) | wie Vanilla `event_image` (Bild statt Video möglich) | `gfx/event_pictures/va_silvermoon_*.dds` | VA-020 |
| State-Bild Terrain „Underwater“ (Vashj'ir) | `common/terrain/va_terrain.txt` | Vanilla `wetland.dds` + `vfx_entity_ui_state_wetland` | wie Vanilla `gfx/state_pictures/*.dds` | `gfx/state_pictures/va_underwater.dds` | VA-051 |

Bildideen (Vorschlag): Ley Line Tap = Kristallturm über leuchtender blauvioletter Leylinie, elfische Goldverzierung. Mana = schwebender, leuchtender Kristall bzw. Phiole mit arkaner Flüssigkeit. Focus Crystals = einzelner geschliffener Fokuskristall in Goldfassung.

## Notizen

- 2026-11-05: Gut „Mana“ eingebaut: Konos `.claude/grafik_quellen/mana.png` (56×56) mit `.claude/tools/va_icon.py` → `gfx/interface/icons/goods_icons/va_mana.dds` (256×256, BGRA mit Mipmaps wie Vanilla). Quelle ist klein, hochskaliert etwas weich; bei Bedarf größere Fassung nachliefern. Test T-090.

- Später (eigene Aufgabe, wenn gewünscht): Stadtgrafiken je Volk (Zwerge, Elfen, Orcs) über die Trigger in `common/scripted_triggers/00_gfx_buildings_graphics_triggers.txt` (TODO dort). Braucht 3D-Assets, nicht nur Bilder.

- Ohne TODO-Markierung, aber mit Erde-Platzhaltern: Gilneas-Events (`events/gilneas_events/infection_events.txt`, 9× `event_image` mit Erde-Videos wie Amerikanischer Bürgerkrieg) und JE-Icons in `VA_gilneas_infection.txt`. Erst angehen, wenn der Inhalt mit VA-007 überarbeitet ist (`VA_silvermoon.txt` mit VA-020 erledigt); dann TODOs setzen und hier eintragen.
- 2026-11-06 (VA-062): Icon für `va_deathholme_scourge_tide` (vorerst `modifier_fist_positive.dds`) und eigenes Schneisen-Material statt `DYNAMIC-Devastation_Mud_01` (`common/terrain/va_terrain.txt`).
- 2026-11-06: Gebäude-Icon „Ley Line Tap“ eingebaut: Konos Bild (256×256, transparent; lag als `Mana Produktion.png` im Mod-Root, verschoben nach `.claude/grafik_quellen/va_ley_line_tap.png`) mit `va_icon.py` → `gfx/interface/icons/building_icons/va_ley_line_tap.dds`. Zeile aus der Tabelle entfernt. PM-Icon „Focus Crystals“ bleibt vorerst Platzhalter (Kono). Test T-107.
