# VA-047: Silvermoon – Korridor nach Tranquillien

- **Status:** wartet (Spieltest)
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Umbau von `je_silvermoon_deathholme` (VA-020). Silvermoon soll recht schnell (ca. 5 Jahre) eine Verbindung nach Tranquillien schlagen, damit Tranquillien in Silvermoons Markt kommt. Zwei Wege:

1. **Triage und Logistik:** Provinzen entlang der Schneise schrittweise übernehmen (annektieren), ohne Krieg, mit Kosten.
2. **Militärische Macht:** Krieg gegen Deathholme.

Danach bleibt Deathholme vertreiben bzw. eingliedern das größere Ziel (VA-048). Vorbild für Provinz-Übernahme prüfen (Vanilla `transfer_province` o. Ä., Grenzkorrektur-Events).

## Notizen

- 2026-10-31 (Claude): Umgesetzt als **eigenes JE `je_silvermoon_corridor`** parallel zu `je_silvermoon_deathholme` (das bleibt das große Ziel, Umbau mit VA-048). So bleiben die offenen VA-020-Tests gültig.
- Geografie aus `provinces.png`: Tranquilliens Exklave (5 Provinzen in `STATE_TRANQUILLIEN`) ist nur **zwei** Deathholme-Provinzen von Silvermoons East Sanctum entfernt (`xFDDA71`, `xD536B6`). Etappen nach Konos Auswahl (2026-10-31), 5 Provinzen, alle in `STATE_TRANQUILLIEN`:
  1. Grenze: xFDDA71 x186841
  2. Berge (impassable): xCEF332 x2FC0FD
  3. Straße: xD536B6 (grenzt an die Exklave)
  - Für Straße/Infrastruktur nötig sind nur x186841 und xD536B6. xA4E8D0, xFB0892, x7511A0 gehören zur Todesschneisen-Grafik und bleiben bewusst draußen.
- **Weg 1 Logistik:** Schalter „Launch Logistics Operation“ (nur ohne Krieg, nicht bankrott, Deathholme hält noch Land der Etappe): einmalig −100.000, solange die Operation läuft Modifier `va_silvermoon_corridor_logistics` (Bürokratie −25, Autorität −25). Balken 18 Monate, ruht in jedem Krieg. Danach `set_owner_of_provinces` (nur Provinzen, die noch Deathholme gehören), `silvermoon_events.4`, nächste Etappe. 3 × 18 Monate = 4,5 Jahre.
- **Weg 2 Krieg:** Erfüllt ist das JE, sobald Silvermoon oder ein Subjekt `xD536B6` und eine Provinz zwischen ihr und Silvermoon besitzt (x186841, xFDDA71 oder im Krieg auch Deathholmes East-Sanctum-Provinz x7C385F), egal wie (Ansprüche auf `STATE_TRANQUILLIEN`/`STATE_EAST_SANCTUM` kommen schon aus `je_silvermoon_deathholme`). Etappen ohne Deathholme-Land werden übersprungen.
- Abschluss: `silvermoon_events.5`, Modifier „The Road to Tranquillien“ (Prestige +10, 10 J.). Ablauf nach 8 Jahren ohne Malus.
- Dateien: `common/journal_entries/VA_silvermoon.txt`, `common/scripted_buttons/va_silvermoon_corridor_buttons.txt`, `common/scripted_progress_bars/va_silvermoon_corridor_bars.txt`, `common/scripted_triggers/va_silvermoon_corridor_triggers.txt`, `common/scripted_effects/va_silvermoon_corridor_effects.txt`, `common/static_modifiers/va_silvermoon_modifiers.txt`, `events/va_silvermoon_events.txt`, `common/history/global/va_global_quel_thalas.txt`, Loc `va_silvermoon_l_english.yml`.
- Offen für Kono: Kosten (100.000, −25/−25), Etappendauer (18 Monate), Belohnung, Malus bei Ablauf? Reaktion Deathholmes auf die Operationen (Grenzzwischenfall-Event)? Ob ein Protektorat schon ohne Landweg in Silvermoons Markt hängt, entscheidet der Spieltest (Marktzugang Tranquillien vorher/nachher ansehen).
- Ungeprüft: Wie `set_owner_of_provinces` Pops und Gebäude der Teil-States aufteilt; Testfall T-057 achtet darauf.
- 2026-10-31: Einmalkosten je Etappe auf Konos Wunsch 100.000 (Startwerte Silvermoon: ca. +10.000/Monat, Kreditlimit ca. 700.000).
- 2026-11-12, Kono: T-056, T-057 OK; Bürokratie der Logistik-Operation zu billig → −50 in `va_silvermoon_corridor_logistics`. Nachtest T-127, danach erledigt.
- 2026-11-12, Kono-Test: Korridor-JE blieb offen, obwohl Tranquillien schon von Zul'Jarra erobert war. Neues verstecktes Abbruch-Outcome in `je_silvermoon_corridor`: Stadt x1437EA gehört weder Silvermoon noch einem Untertan → JE endet, Logistik-Modifier weg. Test T-131 (3).
