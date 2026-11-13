# VA-072: Upload Version 3 – Phase 1 Quel'Thalas (Silvermoon, Wretched, Zul'Jarra)

- **Status:** in Arbeit
- **Typ:** technik
- **Priorität:** hoch
- **Erstellt:** 2026-11-12

## Beschreibung

Kono 2026-11-12: Phase 1 abschließen, Silvermoon, Zul'Jarra und die ganze Region Quel'Thalas für den Release fertig machen. Blocker sind nur nicht feuernde Events, error.log-Zeilen aus der Region und nicht abgenommene AI-WRITTEN-Texte. Balance- und Buff-Tests blockieren nicht.

## Release-Blocker (Spieltest Kono)

| Test | Inhalt | Stand 2026-11-12 |
|---|---|---|
| T-073 | Eingliedern nach Heilung (Stufe 1) | Fix drin, erneut testen |
| T-074 | Felendren-Kopfgeld | Fix (Exil-Suche) drin, erneut testen |
| T-075 | Wretched zerfallen nach drittem Anführer | offen, braucht T-074 |
| T-076 | Mana-Aufstand | offen |
| T-111 | Amani-JEs zum Start | OK 2026-11-12 |
| T-112 | Stämme sammeln | OK, Balance geändert → T-131 |
| T-113 | Loa-Rituale | 2 von 4 Loa getestet; drittes und viertes Loa (Events .5/.6) offen |
| T-114 | Belagerung, Reich, Rache, Schatzjäger | OK; Formable-Wunsch → VA-017 |
| T-127 | Loa-Ritual- und Korridor-Kosten | OK 2026-11-12 |
| T-132 | Formable Amani-Reich (VA-017) | OK 2026-11-13, danach erweitert |
| T-133 | Eigenes Event-Bild „The Wretched Healed“ | OK 2026-11-13 |
| T-134 | Mana-Nerf (Ley Line Tap, Bedarf nach Lebensstandard) | OK 2026-11-13 |
| T-131 | Nachtest Shadowpine-Tribut, Schatzjäger +75, Korridor-Abbruch | offen |
| T-115 | error.log Amani | OK 2026-11-12 (nur Observe-Zeilen) |
| T-077, T-118 | error.log Wretched/Bevölkerung | OK 2026-11-13 (Log 22:39 sauber) |

Nicht blockierend: T-071/T-072 Restfälle (Entzug, Rückfall), T-108, T-120, T-129.

## Checkliste Upload (Skill `va-patch-upload`)

- [x] Letzte Testrunde: Kono 2026-11-13 (Freitag): offene Blocker-Tests (T-073–076, T-113 Rest, T-131, T-132, T-077/T-118) werden nach dem Release nachgeholt; Spieler testen übers Wochenende mit. Kampagne lädt, Kernpfade sind getestet.
- [x] `va_lint.py --regions 21–35`: 903 Befunde, 0 neue Fehler (2026-11-12)
- [x] Tickets: VA-019, VA-021, VA-022, VA-047, VA-065, VA-066, VA-068, VA-017 warten auf Spieltest. Bewusst offen (Kono 2026-11-13): VA-016 übrige Nord-EK-Herrscher (Release betrifft nur Quel'Thalas, Ghostlands, Zul'Aman), VA-067 Sylvanas (Priorität mit Undercity).
- [x] TODO-Durchgang (2026-11-12): 277 TODOs. Quel'Thalas: 191 Grafik-Platzhalter (VA-027), 3 „eigene arkane Technologie“ und 1 Mana-Werte (später, Kono 2026-11-06), Kael'thas (VA-056), Aldaron-Modifier (VA-021, Ausbau), Formable Amani-Reich (VA-017). Rest außerhalb der Region (Outland 52, Gilneas VA-007). Kein TODO blockiert.
- [ ] AI-WRITTEN-Abnahme durch Kono: **571** Texte, davon 554 abgenommen (Amani 177, Wretched 230, Mana 81, Silvermoon 51, Todesschneise 9, Figuren 6; 2026-11-13), **17** offen (16 Ländernamen Quel'Thalas abgenommen 2026-11-13; Gebäude 6, Machtblöcke 4, Gilneas 2, Regierung 2, Terrain 2, Quel'Thalas 1), Liste `.claude/abnahme/ai_written_version_3.md` (Amani 175, Wretched 123, Wretched-Story 107, Mana 81, Silvermoon 51, Todesschneise 9, Rest 23)
- [x] `.metadata/metadata.json`: `version` 2 → 3 (2026-11-13); `supported_game_version` 1.15.* passt zu Spiel 1.15.1
- [ ] `mod\warcraft` neu befüllen (Kono)
- [ ] Kurztest aus dem Mod-Ordner: Kampagne lädt
- [x] Workshop-Text: `.claude/releases/version_3_workshop.md` (Stand 2026-11-13 mit Formable, Texten, Wappen, Event-Bild)
- [x] Inhaltszahlen (`va_release_stats.py --compare 2025-12`, Arbeitsstand 2026-11-12): JEs +6 (12), Events +37 (52), Scripted Buttons +33, Progress Bars +10, Modifier +80, Scripted Effects +85, Scripted Triggers +61, Script Values +4, Güter +1, Charaktervorlagen +12, Texte +807 (+6.935 Wörter), Grafiken +3. 2026-11-13 abschließend (Zählung korrigiert: alte Vanilla-Reste und Erde-Hüllen ausgeschlossen, Basis 2025-12 neu = 2 JEs, 1 Event): JEs +10, Events +49, Effekte +65, Trigger +52, +1 Land (AMANI_EMPIRE), Texte +827 (+7.177 Wörter), Grafiken +4, AI WRITTEN noch 17 (außerhalb Quel'Thalas); gesichert als `releases/version_3.json`.

## Notizen

- 2026-11-12, Claude: error.log 17:16 zeigte noch 80× `va_wretched_last_level` nicht gesetzt (`va_silvermoon_wretched_effects.txt:135`, aus dem Tooltip des JE-Outcomes „Wretched anders untergegangen“). Der Fix vom Mittag setzt die Variable zwar vorher, aber Tooltips führen `set_variable` nicht aus. Jetzt alle vier Vergleiche mit `has_variable` abgesichert, ohne Variable gilt Stufe 3. Die 1.592 `va_wretched_heal_stage`-Zeilen stammen aus dem Start um 17:00, vor dem Fix um 17:17.
- 2026-11-12, Zul'Jarra-Sitzung: Ergebnisse oben. Kono: Formable Amani-Reich gehört in Version 3, gescriptet (VA-017, T-132).
- 2026-11-13, Kono: „Raze Zul'Aman“ bleibt in Version 3; Eindämmung später (VA-022).
- 2026-11-13, Claude: Abschluss-Log 22:39 (error.log + error.1.log, 69 Mod-Einträge): nur bekannte Altlasten (Vanilla-Reste, NewFlags-Embleme, city_types, Gilneas-Loc, Achievements), keine Zeile aus Version-3-Content. Freigabe für den Upload.
