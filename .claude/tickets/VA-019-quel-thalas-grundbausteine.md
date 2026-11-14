# VA-019: Quel'Thalas – Mana und Todesschneise (Grundbausteine)

- **Status:** wartet (Spieltest)
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Gemeinsame Bausteine für Silvermoon, Wretched und Deathholme: Mana als Handelsgut mit Abhängigkeit der Elfen, Todesschneise auf den Ghostlands-States. Konzept: [../konzepte/quel_thalas.md](../konzepte/quel_thalas.md). Objekte und Dateien: `karte/content_systeme.md` („Quel'Thalas: Mana“, „Todesschneise“). Vollständiger Verlauf bis 2026-11-13: [verlauf/VA-019-quel-thalas-grundbausteine.md](verlauf/VA-019-quel-thalas-grundbausteine.md).

## Stand (2026-11-14)

Entscheidungen von Kono, alle umgesetzt:
- **Mana ist ein Handelsgut** (`mana`), Quelle sind Leylinien (`building_leyline_tap`, `capped_resources` in Region 26, 13 States). Stufen Focus Crystals → Arcane Conduits → Runic Resonators, Zusatz Arcane Sigils. Nach Nerf 2026-11-13: Ausstoß 12/24/36, Sigils +6, 7.000 Arbeiter je Stufe.
- **Mana ist Stimulans, kein Rauschmittel:** `popneed_stimulants` per `INJECT:` (Gewicht 0.65, `min_supply_share` 0.1), Obsession bei `sin_dorei`/`quel_dorei`.
- **Abhängigkeit als Dauer-JE** `je_mana_hunger`: Stufen nach Marktpreis (Fülle ≤ Grundpreis, Knappheit ab +25 %, Entzug ab +70 %).
- **Grundbedarf** je State `va_mana_upkeep`: 3,0 je 100.000 Elfen, steigt mit dem Lebensstandard (×1,1–1,75), kein Tech-Faktor. Start-Tap Sunwell 2 Stufen = 48 Mana → Entzug ab Start, erste 10 Jahre bewusst unangenehm.
- **Maßnahmen** im JE: Disenchantment-Werkstatt (10 Mana, 1 Jahr), Rationierung, Fauna aussaugen je Eversong-Region (stapelnde Malusse).
- **Todesschneise** hängt an der State-Region (`va_dead_scar_region`), Untote leiden kaum (Lebenden-Malus nur ohne untote Mehrheit), Prüfung monatlich und bei Besitzwechsel. Heilung: VA-046 (erledigt), Optik: VA-062 (erledigt).

## Offen

- Spieltests **T-108** (Ausbaustufen) und **T-134** (Mana-Nerf). Danach `erledigt`.
- Werte und Vanilla-Techs der Tap-Stufen sind Platzhalter (TODO in den PM-Dateien); Icons in VA-027.
- Später, eigenes Ticket: Mana als Vorprodukt für Gebäude/PMs (Bedarf wächst dann mit der Wirtschaft), Leylinien außerhalb Nord-EK.

## Notizen

- 2026-11-14 (VA-074): Ticket auf Stand gekürzt, alter Verlauf unter `verlauf/`.
