# VA-074: Projekt-Doku schlank halten (Token-Verbrauch)

- **Status:** erledigt
- **Typ:** aufraeumen
- **Priorität:** hoch
- **Erstellt:** 2026-11-14

## Beschreibung

Kono, 2026-11-14: Das Modpack wird noch 2–3 Jahre weiterentwickelt. Die Doku in `.claude/` soll so bleiben, dass pro Aufgabe nicht unnötig viel geladen wird.

Messung 2026-11-14 (Zeichen, grob 4 Zeichen ≈ 1 Token):

| Datei | Zeichen | Wann geladen |
|---|---|---|
| `CLAUDE.md` | 7.200 | immer |
| `KARTE.md` | 26.000 | vor fast jeder Aufgabe |
| `ABLAUFPLAN.md` | 15.100 | vor größerer Arbeit |
| `tickets/README.md` | 9.900 (alle 73 Tickets, auch erledigte) | bei Ticket-Arbeit |
| `TESTPROTOKOLL.md` | 42.900 (nur offene Fälle) | per grep, gezielt |
| `ablauf/gilneas.md` | 30.600 | bei Gilneas-Content |

Die Ticketnummern selbst kosten nichts; vierstellige Nummern sind kein Problem.

## Vorschläge (nach Nutzen)

1. **KARTE aufteilen:** `KARTE.md` nur als Index (Werkzeuge, Ordner, je Region/System eine Zeile mit Verweis), Details in `karte/<region>.md`. Größter Hebel, weil sie fast immer gelesen wird.
2. **Ticket-Übersicht nur offen:** erledigte und verworfene Zeilen nach `tickets/archiv/README.md`; erledigte Ticket-Dateien konsequent nach `tickets/archiv/`.
3. **Ablauf und Lore trennen:** In `ablauf/<land>.md` nur Entscheidungen, Mechanik und Diagramm; Lore-Recherche (Wiki, Videos) nach `ablauf/lore/<land>.md`, nur bei Bedarf lesen.
4. **Testfälle kurz halten:** je Fall höchstens 3–5 Zeilen (Schritte, erwartetes Ergebnis); Hintergründe gehören ins Ticket.
5. **Größengrenzen als Regel:** z. B. Index-Dateien unter 15.000 Zeichen, sonst aufteilen. Prüfen bei jeder Testrunde oder in einer festen Aufräumrunde, und in `CLAUDE.md` bzw. im Skill festhalten.

6. **Übergabefest bleiben:** Jede neue Session muss allein aus `CLAUDE.md` → `KARTE.md` → Ticket bzw. Ablauf arbeitsfähig sein. Keine Entscheidung nur im Chat; Doku nicht an ein bestimmtes Modell oder Werkzeug binden.

## Notizen
- 2026-11-14, Kono: Weiterentwicklung über 2–3 Jahre ist ohne Claude für eine Person nicht machbar. Deshalb Priorität hoch: Die Doku ist das Projektgedächtnis.
- 2026-11-14, Claude: umgesetzt (reine Doku, kein Spieltest nötig; wartet nur auf Konos Durchsicht).
  1. `KARTE.md` ist jetzt Index (26.000 → 7.400 Zeichen); Details in `karte/content_systeme.md`, `karte/laender_wirtschaft.md`, `karte/erde_abschalten.md`, `karte/werkzeuge.md`. Inhalt unverändert verschoben, `va_pop_report.py` in der Werkzeugliste ergänzt.
  2. `tickets/README.md` zeigt nur Offenes; 12 erledigte/verworfene Zeilen in `tickets/archiv/README.md`.
  3. Gilneas: Lore-Recherche nach `ablauf/lore/gilneas.md`, Entscheidungen bleiben im Ablauf (30.600 → 25.000). Wretched (24.700) enthält keine reine Lore, bleibt. Gilneas liegt an der Grenze: beim Anlegen der JE-Tickets Mechanik-Details in die Tickets verschieben.
  4. Erledigt-Log aus `ABLAUFPLAN.md` nach `ERLEDIGT.md` (15.100 → 8.000), veralteten Kopf (1.13) korrigiert.
  5. Grenzen in `CLAUDE.md` („Doku schlank halten“), Prüfskript `tools/va_doku_check.py` (Exit 1 bei Überschreitung), Prüfung und Testfall-Länge (3–5 Zeilen) im Skill `va-testrunde`, Lore-Regel im Skill `va-content`, Workshop-Quelle `ERLEDIGT.md` im Skill `va-patch-upload`.
  6. Einstiegsreihenfolge `CLAUDE.md` → `KARTE.md` → Ticket/Ablauf in `CLAUDE.md`.
  Bestehende Testfälle nicht umgeschrieben (Konos Häkchen bleiben); die Regel gilt für neue Fälle.
- 2026-11-14, Kono: keine Abnahme nötig, Doku-Struktur liegt in Claudes Verantwortung. Erledigt.
