# VA-068: Lor'themar Theron ist Regent, nicht König

- **Status:** wartet (Spieltest)
- **Typ:** content
- **Priorität:** niedrig
- **Erstellt:** 2026-11-12

## Beschreibung

Kono (2026-11-12): Lor'themar Theron (`va_qt_lorthemar_theron`, VA-066) führt Silvermoon als Herrscher und trägt im Spiel den Titel König. Lore: Er ist Regent Lord von Quel'Thalas und hat die Krone ausdrücklich abgelehnt, obwohl Quel'Thalas eine Monarchie ist. Titel bzw. Regierungsform so anpassen, dass er als Regent erscheint. Kommt irgendwann dazu.

## Notizen

- Ansatz zum Prüfen (Claude, ungeprüft): Vanilla hat Regentschafts-Regierungsformen (`common/government_types/01_regencies.txt`, im Mod als Hülle abgeschaltet, VA-063) bzw. eigene Herrschertitel je Regierungsform (`ruler_male`/`ruler_female` in `government_types`). Möglich: eigene Regierungsform `va_gov_regency_quel_thalas` mit Titel „Regent Lord“ für Silvermoon, solange kein Sunstrider herrscht (Kael'thas, VA-056).
- 2026-11-12, Claude (Kono-Test T-117 erneut gemeldet): Regierungsform `gov_va_regency_quel_thalas` in `common/government_types/00_va_monarchies.txt` (Monarchie, nur SILVERMOON), Titel `RULER_TITLE_VA_REGENT_LORD/LADY` „Regent Lord/Lady“ in `va_goverment_l_english.yml`. Vorbild Vanilla `gov_regency_ethiopia_ras`. TODO: Sunstrider-Bedingung mit VA-056. Test T-130.
