# VA-027: Platzhalter-Grafiken durch eigene ersetzen

- **Status:** offen
- **Typ:** grafik
- **Priorität:** niedrig
- **Erstellt:** 2026-10-30

## Beschreibung

Sammelticket: Bilder, die Kono generieren soll. Im Script ist jeder Platzhalter mit `# TODO: eigenes …` markiert. Die Liste unten wird beim TODO-Durchgang (Ablaufplan, Checkliste Upload) aus dem Code nachgezogen. Fertige Bilder legt Kono als PNG ins Repo oder nennt den Pfad; Claude wandelt sie in DDS um, legt sie unter `gfx/…` ab, trägt die Pfade ein und entfernt das TODO.

**Format der Vanilla-Vorbilder** (gemessen 2026-10-30): RGBA mit transparentem Hintergrund, DDS unkomprimiert mit Mipmaps. Stil wie Vanilla: gemalt, leichte Schrägansicht, kräftige Kontur, kein Text.

## Offene Grafiken

| Was | Wo im Script | Platzhalter | Größe | Ziel-Datei (Vorschlag) | Ticket |
|---|---|---|---|---|---|
| Gebäude-Icon „Ley Line Tap“ | `common/buildings/va_mana_buildings.txt:5` | Kohlemine | 256×256 | `gfx/interface/icons/building_icons/va_ley_line_tap.dds` | VA-019 |
| Gut „Mana“ | `common/goods/va_goods.txt:3` | Strom | 256×256 | `gfx/interface/icons/goods_icons/va_mana.dds` | VA-019 |
| Produktionsmethode „Focus Crystals“ | `common/production_methods/va_mana_production_methods.txt:3` | Spitzhacke/Schaufel | 104×104 | `gfx/interface/icons/production_method_icons/va_focus_crystals.dds` | VA-019 |
| Modifier-Icon „The Dead Scar“ | `common/static_modifiers/va_quel_thalas_modifiers.txt:4` | Feuer (negativ) | wie Vanilla `modifier_fire_negative.dds` | `gfx/interface/icons/timed_modifier_icons/va_dead_scar.dds` | VA-019 |
| Modifier-Icons „Arcane Abundance“, „Mana Scarcity“, „Mana Withdrawal“ | `common/static_modifiers/va_mana_modifiers.txt` | Glühbirne (pos./neg.), Feuer (neg.) | wie Vanilla `timed_modifier_icons` | `gfx/interface/icons/timed_modifier_icons/va_mana_*.dds` | VA-019 |
| Modifier-Icon „Shadow of the Dead Scar“ | `common/static_modifiers/va_quel_thalas_modifiers.txt` | Feuer (negativ) | wie Vanilla `timed_modifier_icons` | `gfx/interface/icons/timed_modifier_icons/va_dead_scar_living.dds` | VA-019 |
| JE-Icon „The Mana Hunger“ | `common/journal_entries/va_mana.txt:5` | Waage (`event_scales`) | wie Vanilla `event_icons` | `gfx/interface/icons/event_icons/va_mana_hunger.dds` | VA-019 |

Bildideen (Vorschlag): Ley Line Tap = Kristallturm über leuchtender blauvioletter Leylinie, elfische Goldverzierung. Mana = schwebender, leuchtender Kristall bzw. Phiole mit arkaner Flüssigkeit. Focus Crystals = einzelner geschliffener Fokuskristall in Goldfassung.

## Notizen

- Später (eigene Aufgabe, wenn gewünscht): Stadtgrafiken je Volk (Zwerge, Elfen, Orcs) über die Trigger in `common/scripted_triggers/00_gfx_buildings_graphics_triggers.txt` (TODO dort). Braucht 3D-Assets, nicht nur Bilder.

- Ohne TODO-Markierung, aber mit Erde-Platzhaltern: Gilneas-Events (`events/gilneas_events/infection_events.txt`, 9× `event_image` mit Erde-Videos wie Amerikanischer Bürgerkrieg) und JE-Icons in `VA_gilneas_infection.txt`/`VA_silvermoon.txt`. Erst angehen, wenn der Inhalt mit VA-007 bzw. VA-020 überarbeitet ist; dann TODOs setzen und hier eintragen.
