# VA-052: Script-Doku (docs/*.log) älter als das Spiel

- **Status:** erledigt
- **Typ:** technik
- **Priorität:** mittel
- **Erstellt:** 2026-11-01

## Beschreibung

Beim Aufbau der Skills (2026-11-01) gefunden: `%USERPROFILE%\Documents\Paradox Interactive\Victoria 3\docs\*.log` ist vom 2025-11-30, `binaries\victoria3.exe` vom 2026-08-19 (1.13.11). Die Doku stammt also von vor 1.13. Beispiel: `set_owner_of_provinces` fehlt in `effects.log`, Vanilla benutzt es aber (`common/decisions/canal_decisions.txt:144`), der Mod ebenso (Korridor, VA-047).

Folge: Prüfungen gegen die Doku können falsch negativ sein (Effekt fehlt) oder alte Syntax zeigen.

## Erledigen

1. Kono: Spiel starten, Konsole öffnen, `script_docs` ausführen.
2. Claude: Datum von `effects.log` prüfen, Stichprobe `set_owner_of_provinces`.
3. Hinweise auf die alte Doku entfernen: `.claude/KARTE.md` (Abschnitt „Vanilla und Script-Doku“), `.claude/CLAUDE.md` (Pfade), Skill `va-content` (Schritt 1.4).

Bis dahin gilt: Verwendung in Vanilla-Dateien schlägt Doku.

## Notizen

- 2026-11-01: Kono hat `script_docs` ausgeführt. Neue Doku vom 2026-11-01 13:48: `effects.log` 920 KB (3.152 Effekte, vorher 140 KB), `triggers.log` 420 KB (1.816), `modifiers.log` 900 KB. `set_owner_of_provinces` ist jetzt dokumentiert (Scope `state_region`). Format von `modifiers.log` geändert (`<name>:` mit `Mask`/`Name`/`Description` statt `Tag:`), Grep-Befehle in KARTE und Skill angepasst. Hinweise auf die alte Doku entfernt.
