# VA-066: Silvermoon – eigene Charaktere

- **Status:** wartet (Spieltest)
- **Typ:** content
- **Priorität:** mittel
- **Erstellt:** 2026-11-10

## Beschreibung

Silvermoon hat kaum eigene Charaktere (Kono, 2026-11-10). Bekannte Figuren als Charakter-Vorlagen anlegen, damit Events sie per `has_template` ansprechen und in Texten nennen können. Vorbild im Mod: `common/character_templates/va_wretched_characters.txt` (Erzeugung in `common/history/characters/va_eastern_kingdom.txt`).

Kandidaten (Vorschlag Claude, Kono wählt aus): Lor'themar Theron (Regent), Grand Magister Rommath, Halduron Brightwing (Waldläufer-General), Lady Liadrin (Blutritter), Aethas Sunreaver, Magister Astalor Bloodsworn.

Danach in vorhandene Silvermoon-Events einziehen (Korridor, Wretched, Todesschneise) und für die Gegenseite der Amani-Reihe nutzen (VA-022).

## Notizen

- 2026-11-10: Angelegt auf Konos Hinweis während VA-022.
- Gilt sinngemäß auch für Zul'Jarra: Zul'jin und Hexlord Malacrass fehlen als Charaktere (VA-016, VA-022).
- 2026-11-10: Erste Figuren angelegt: Lor'themar Theron (Herrscher), Rommath (IG-Anführer Intelligenzija), Halduron Brightwing (General), Liadrin (IG-Anführerin Fromme); dazu Dar'Khan, Zul'jin, Malacrass. Malacrass stirbt bei `amani_loa_events.6` Option a. Offen: Figuren in bestehende Silvermoon-Events einziehen (Korridor, Wretched, Todesschneise), Astalor, Aethas. Test T-117.
- 2026-11-10, Kono: Boni abgenommen und umgesetzt. Trigger `va_has_halduron/rommath/liadrin_trigger` (`va_quel_thalas_character_triggers.txt`). Halduron: Korridor-Balken +0,2/Monat (15 statt 18 Monate), Kopfgeld +10 Prozentpunkte. Rommath: Rückfall bei der Wretched-Heilung erst nach 5 statt 3 Monaten Entzug. Liadrin: Modifier `va_silvermoon_blood_knight_wardens` (Bürokratie +10) solange eine Ritual Site steht (`va_liadrin_ritual_wardens_effect`, aus `je_va_dead_scar`). Deathholme-Abschluss `silvermoon_events.2.d` nennt Dar'Khan, Auriferous, Mavren. Schalter-Texte nennen die Boni. Test T-120.
