# VA-020: Silvermoon – Journal Entries

- **Status:** wartet (Spieltest)
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Fünf Ziele: Deathholme vertreiben, Zul'Aman zerstören, Wretched heilen (zusammen mit VA-021), Todesschneise heilen, Mana-Problem (Dauer-JE). Datei `common/journal_entries/VA_silvermoon.txt`, Events `namespace = silvermoon_events`.

Konzept: [../konzepte/quel_thalas.md](../konzepte/quel_thalas.md)

## Notizen
- 2026-10-30 (Log Runde 4): Bestehende `common/journal_entries/VA_silvermoon.txt` hat kein BOM und nutzt `should_be_pinned_by_default` (Zeile 15), das 1.13 nicht mehr kennt. Beim Neuaufbau mitbeheben.
- 2026-10-30: Ziel 5 (Mana-Problem, Dauer-JE) ist als `je_mana_hunger` in `common/journal_entries/va_mana.txt` angelegt (VA-019). Hier bleibt nur der Abschluss per Sunwell-Projekt. Ablauf: `.claude/ablauf/silvermoon.md`.
- 2026-10-30: **Drei Ziele angelegt**, nicht getestet. Wretched (Ziel 3) bleibt bei VA-021, Sunwell-Projekt (Abschluss Mana-JE) später.
  - `common/journal_entries/VA_silvermoon.txt` neu aufgebaut (BOM, altes Gerüst `je_silvermoon_wretched_elfes` und `should_be_pinned_by_default` entfernt):
    - `je_silvermoon_deathholme`: Ansprüche auf Deathholme, Windrunner Village, Tranquillien, East Sanctum, Suncrown Village. Erfüllt, wenn `c:DEATHHOLME` nicht mehr existiert. Belohnung `va_silvermoon_ghostlands_avenged` (Prestige +25, 10 J.). Ablauf 15 J. → `va_silvermoon_deathholme_endures` (Prestige −10 %, 10 J.).
    - `je_silvermoon_zul_aman`: Ansprüche auf Zul'Aman, Tor Watha; erfüllt bei vollem Besitz beider. Belohnung `va_silvermoon_amani_broken` (Prestige +25), setzt `global_var:va_amani_claims_shattered` (für VA-017/022: Amani-Formable sperren). Ablauf 20 J. ohne Malus.
    - `je_silvermoon_dead_scar`: Fortschrittsbalken 0/6 (Variable `va_dead_scar_regions_healed`). Knopf `va_silvermoon_dead_scar_ritual_button` (`common/scripted_buttons/va_silvermoon_buttons.txt`, 25.000 Gold) startet ein Ritual; `va_dead_scar_ritual_pulse_effect` zählt monatlich, ruht in „Mana Withdrawal“, bricht ohne eigenen Schneisen-State ab. Nach `va_dead_scar_ritual_duration` (24 Monate, `common/script_values/va_silvermoon_values.txt`) heilt `silvermoon_events.1` eine eigene Schneisen-Region (`va_heal_dead_scar_state_effect`). Erfüllt, wenn kein State mehr auf der Schneise liegt → `va_silvermoon_quel_thalas_healed` (Prestige +50, 20 J.). Ablauf 30 J.
  - Neu: `events/va_silvermoon_events.txt` (`silvermoon_events.1`–`.4`), `common/static_modifiers/va_silvermoon_modifiers.txt`, `common/scripted_triggers/va_quel_thalas_triggers.txt` (`va_state_on_dead_scar_trigger`), Loc `localization/replace/english/va_silvermoon_l_english.yml` (AI WRITTEN). Zuweisung zum Start in `va_global_quel_thalas.txt`.
  - Werte (Kosten, Dauer, Prestige, Abläufe) sind Vorschläge, Kono passt an. Icons/Bilder Platzhalter (VA-027).
  - Tests T-049 bis T-052 (Runde 10).
- 2026-10-30, Kono: guter Start, aber zu simpel. Umbau verteilt:
  - Todesschneise → VA-046 (Balken je Region, an/aus, laufende Kosten, 20 Monate, alle Besitzer).
  - Deathholme → VA-047 (Korridor nach Tranquillien) und VA-048 (Untote eingliedern).
  - Zul'Aman → Eindämmung statt Zerstörung, Eventreihe mit Zul'jin (VA-022), wartet auf Kono.
  - Fehlende JEs: Wretched (VA-021, Annexion oder Heilung) und eigenes Königreich (VA-050).
  Die gescripteten Stände bleiben bis zum Umbau als Testbasis.
