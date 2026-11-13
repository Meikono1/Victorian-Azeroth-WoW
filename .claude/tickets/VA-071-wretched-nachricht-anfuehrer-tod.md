# VA-071: Wretched erfahren vom Tod ihres Anführers

- **Status:** offen
- **Typ:** content
- **Priorität:** niedrig
- **Erstellt:** 2026-11-12

## Beschreibung

Kono-Test T-074 (2026-11-12): Stirbt ein Anführer durch das Kopfgeld, bekommt nur Silvermoon ein Popup, zum Beispiel „The Ringleader Falls“. Die Wretched erfahren nichts. Spielt man die Wretched, wäre eine eigene Nachricht schön, zum Beispiel ein Toast oder ein kleines Event aus ihrer Sicht.

## Notizen

- Ansatz: In `va_silvermoon_wretched_hunt_success_effect` (`va_silvermoon_wretched_bounty_effects.txt`) für `c:WRETCHED_BLOODELFES` ein Event ohne Popup auslösen; Vorbild für die Nachricht ist Vanilla `post_notification`.
- Neue Texte bekommen „(AI WRITTEN)“. Deshalb erst nach dem Quel'Thalas-Release, damit die Abnahmeliste nicht wächst.
