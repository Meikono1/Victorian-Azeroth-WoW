# VA-043: error.log 30.10. – Restbefunde aus Mod-Dateien

- **Status:** wartet (Spieltest)
- **Typ:** bug
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Restbefunde aus dem Log vom 30.10. und der Großputz vom 03.11. (acht Läufe, Start-Einträge 9.598 → 2.021, Laufzeit-Spam beseitigt). Vollständiger Verlauf mit allen Maßnahmen: [verlauf/VA-043-errorlog-befunde-3010.md](verlauf/VA-043-errorlog-befunde-3010.md). Werkzeuge und Hüllen dazu: `karte/erde_abschalten.md`.

## Stand (2026-11-14)

Erledigt: Loc-Keys mit `’`/`Ö`, `STATE_SKORN`, Holzfäller-PMs Nord-Kalimdor, Gebäude-Kopien gelöscht und 861 Stellen auf 1.13-Namen, Erde-Hüllen (Events, JEs, Vorlagen, Geo-Regionen), erzeugte Overrides (Monumente, Kanäle, Machtblock-Namen, Pan-Bewegungen, Regierungsformen, Errungenschaften), `va_earth_effects.txt`, doppelte `je_mana_hunger`.

Weitergereicht (dort bearbeiten, nicht hier):

| Befund | Ticket |
|---|---|
| 312 Provinzen ohne State Region (ehem. `STATE_TEST`), Pandaria-Provinzen | VA-031, VA-032 |
| Provinzen in mehreren State Regions | VA-011 |
| `region_state` ungültig `va_center_eastern_kingdoms.txt:336` | VA-024 |
| `size = zombie` Outland | VA-055 |
| Doppelte Ressourcen Outland | VA-029 (Region 29) |
| Festungs-/Port-Locators | VA-060, Kono beim Neuzeichnen |
| Fehlende Wappen-Texturen | VA-027 |

## Offen

- Test **T-081** (error.log nach dem Großputz). Danach `erledigt`; neue Log-Befunde gehören in das Ticket ihres Systems oder ein neues Ticket.
- Hier selbst noch: Länderfarbe außerhalb 0–255 `common/country_definitions/VA_outlands.txt:2, 13` (`color = { 64 487 140 }`).
- Bewusst liegen gelassen (allgemeine Mechanik mit Erde-Zweigen, harmlos): `ai_strategy_default`, Firmen-Charter, KI-Diplomatie, `Variable … is never set` (~390), Erde-Tags `Failed to find country` (~150), `AFS` in Namen/Flaggen, Great-Game-Unterziele.

## Notizen

- 2026-11-14 (VA-074): Ticket auf Stand gekürzt, alter Verlauf unter `verlauf/`.
