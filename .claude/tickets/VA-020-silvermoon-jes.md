# VA-020: Silvermoon – Journal Entries

- **Status:** offen
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Fünf Ziele: Deathholme vertreiben, Zul'Aman zerstören, Wretched heilen (zusammen mit VA-021), Todesschneise heilen, Mana-Problem (Dauer-JE). Datei `common/journal_entries/VA_silvermoon.txt`, Events `namespace = silvermoon_events`.

Konzept: [../konzepte/quel_thalas.md](../konzepte/quel_thalas.md)

## Notizen
- 2026-10-30 (Log Runde 4): Bestehende `common/journal_entries/VA_silvermoon.txt` hat kein BOM und nutzt `should_be_pinned_by_default` (Zeile 15), das 1.13 nicht mehr kennt. Beim Neuaufbau mitbeheben.
- 2026-10-30: Ziel 5 (Mana-Problem, Dauer-JE) ist als `je_mana_hunger` in `common/journal_entries/va_mana.txt` angelegt (VA-019). Hier bleibt nur der Abschluss per Sunwell-Projekt. Ablauf: `.claude/ablauf/silvermoon.md`.
