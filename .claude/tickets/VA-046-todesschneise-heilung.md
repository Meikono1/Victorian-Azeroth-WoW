# VA-046: Todesschneise – Heilung je Region mit laufenden Kosten

- **Status:** wartet (Spieltest)
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Ersetzt die einfache Heilung aus VA-020 (`je_silvermoon_dead_scar`, Knopf mit Einmalkosten). Vorgaben Kono (2026-10-30):

- Für **jedes Land**, das einen State auf der Schneise besitzt, auch Untote (Deathholme, Undercity …), nicht nur Silvermoon.
- **Ein Balken je Region**, die noch verdorben ist. Jede Region einzeln jederzeit **an- und abschaltbar**.
- Solange aktiv: **laufende monatliche Kosten** an Gold, Mana und Bürokratie. Nach **20 Monaten** aktiver Heilung ist die Region (der Abschnitt) geheilt.
- Insgesamt schwerer als bisher.

Konzept: [../konzepte/quel_thalas.md](../konzepte/quel_thalas.md), Abschnitt „Überarbeitung nach Kono-Feedback“.

## Notizen

- 2026-10-30, Machbarkeit (Claude): Vanilla erlaubt mehrere `scripted_progress_bar` in einem JE (`00_antarctica.txt`, Definitionen in `common/scripted_progress_bars/`, Doku `scripted_progress_bars.md`); `monthly_progress` kann an Bedingungen hängen. Bars haben kein Sichtbarkeitsfeld → alle sechs Balken immer sichtbar, oder je Region ein eigenes JE.
- Kostenideen: Gold `country_expenses_add`, Bürokratie `country_bureaucracy_add` (beide in `modifiers.log`), Mana ungeklärt. Vorschlag: je aktiver Region ein staatliches Gebäude „Ritual Site“ im State (`create_building`), dessen PM Mana verbraucht und Akademiker beschäftigt → Mana und Löhne laufen von selbst über Markt und Haushalt. Zu prüfen.
- Offen: Fortschritt an die Region hängen (State-Region-Variable), damit er bei Besitzwechsel erhalten bleibt?
- 2026-10-30: Kono: ein JE mit sechs Balken. **Umgesetzt**, nicht getestet:
  - `common/journal_entries/va_dead_scar.txt`: `je_va_dead_scar` (Innere Angelegenheiten) für jedes Land mit Schneisen-State, auch Untote. Start per `va_global_quel_thalas.txt`, neue Besitzer per `va_on_state_dead_scar_check` (On-Action). Ungültig ohne Schneisen-State. Erfüllt, wenn weltweit keine Region mehr verdorben ist → `va_dead_scar_land_restored` (Prestige +50, 20 J.).
  - Sechs Balken `va_dead_scar_bar_<region>` (`common/scripted_progress_bars/va_dead_scar_progress_bars.txt`, 0–20): +1 je Monat, wenn das Land in der Region eine Ritual Site hat und nicht im Mana-Entzug ist. Fortschritt bleibt beim Abschalten erhalten, gehört aber dem Land (bei Besitzwechsel fängt der neue Besitzer bei 0 an).
  - Schalter je Region (`common/scripted_buttons/va_dead_scar_buttons.txt`): „Begin Healing“ kostet einmalig 100.000 (`START_COST` im Skript) und baut `building_va_scar_ward` (Ritual Site) im eigenen State, „Halt Healing“ reißt sie ab.
  - Kosten über das Gebäude (`common/buildings/va_dead_scar_buildings.txt`, Gruppe `bg_va_dead_scar_healing` unter `bg_government`, PM `pm_ritual_circles_building_va_scar_ward`): Löhne für 1.000 Clerks + 500 Academics aus dem Staatshaushalt, 15 Mana + 10 Papier Input, Bürokratie −25 (bis 2026-10-31: 10 Mana, kein Papier). Nicht baubar, nicht erweiterbar.
  - `va_dead_scar_heal_pulse_effect` (`common/scripted_effects/va_dead_scar_effects.txt`): voller Balken → Ritual Site weg, Region heilen, `dead_scar_events.1` (Text für Untote eigener). Ganze Schneise → `dead_scar_events.2`.
  - Regionsteile erzeugt `.claude/tools/va_gen_dead_scar.py` (Regionen, Dauer, Startkosten oben im Skript; neu laufen lassen, dann `va_dead_scar.txt` nachziehen). Seit 2026-10-31 behält das Skript in der Loc-Datei alles ab der ersten Leerzeile (handgeschriebene Einträge); vorher hätte ein Neulauf sie gelöscht.
  - Altes Silvermoon-Ritual entfernt (`je_silvermoon_dead_scar`, Knopf, Script-Wert, `silvermoon_events.1`/`.4`, Loc).
  - Ungeprüft: `scope:journal_entry` im `on_monthly_pulse` des JE; ob `create_building` Regierungseigentum setzt; ob Löhne spürbar genug sind (sonst zusätzlich `country_expenses_add`).
  - Tests T-053 bis T-055.
- 2026-10-31: Kono testet T-053 OK (Teilbesitz, Schalter nach Eroberung). Kosten erhöht auf Konos Wunsch (Einmalkosten + höhere laufende Kosten); Werte Vorschlag Claude: 10.000 Start, 15 Mana, 10 Papier; Start auf Konos Wunsch auf 100.000 erhöht. T-054 danach erneut testen.
- 2026-11-01: Bug: Balken füllten sich nicht. Ursache: `owner = { … }` in `monthly_progress`, der Scope dort ist aber schon das Land (Vorbild `00_greece_progress_bars.txt`). Im Skript behoben, neu erzeugt; ebenso im Korridor-Balken (VA-047).
- 2026-11-01: JE erst ab Technologie `quinine` (Kono). Hinzufügen in `va_global_quel_thalas.txt` und im Monatspuls/Besitzwechsel (`va_on_actions_quel_thalas.txt`). Doppel-Hinzufügen beim Start (error.log `already has a journal entry`) per `NOT has_journal_entry` behoben.
- 2026-11-01: Kono-Test: Balken läuft (East Sanctum), aber Stillstand war nicht erkennbar. Ergänzt: Balken-Tooltip „Stalled: Mana Withdrawal“, deutlicherer Status-Text, kurze Balken-Beschriftung (Regionsname statt abgeschnittenem Satz). Quinine-Sperre zusätzlich im `possible` des JE (Vic3 aktiviert JEs selbst, sobald `possible` erfüllt ist; vorher erschien es trotzdem). „Halt Healing“-Tooltip zeigte Vanilla-Fehler `BUG: remove_building missing perspective` → eigener `custom_tooltip` + `hidden_effect`.
- 2026-11-01: Stillstand hängt jetzt an der Versorgung der Ritual Site (`building_has_goods_shortage`, Mana oder Papier fehlt) statt am Modifier Mana Withdrawal. Grund (Kono): Untote haben keinen Entzug und heilten mit 0 Mana. Invalid-Tooltip zeigte rohen Trigger („All SILVERMOON_ADJ States …“) → `custom_tooltip`. Fehlendes `SILVERMOON_ADJ` gehört zu VA-006.
- 2026-11-01: Texte mit Kono finalisiert (JE-Titel „Curing the Path of Destruction“, Beschreibung, Schalter „Start/Stop Ritual“, Status, Gebäude, Modifier, Events). Balken-Texte ebenfalls bestätigt; Todesschneise ohne AI WRITTEN.
