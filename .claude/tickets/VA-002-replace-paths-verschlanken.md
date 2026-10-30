# VA-002: replace_paths verschlanken

- **Status:** in Arbeit
- **Typ:** technik
- **Priorität:** hoch
- **Erstellt:** 2026-10-29

## Beschreibung

`events`, `events/india_events`, `events/soi_events`, `common/journal_entries`, `common/scripted_buttons`, `common/company_types`, `common/character_templates` aus `replace_paths` nehmen. Danach nur historisch-spezifische Vanilla-Dateien leer überschreiben, allgemeine Mechaniken (Wahlen, Gesetze, Streiks …) kommen wieder aktuell aus Vanilla und die eigenen Kopien in diesen Ordnern können weg.

Hinweis: `replace_paths` gilt nur für genau den Ordner, nicht für Unterordner.

## Notizen

### 2026-10-30 – Teil 1: events

- Entscheidung Christian: `events` streichen. `events`, `events/india_events`, `events/soi_events` aus `.metadata/metadata.json` entfernt.
- Neues Prüfskript `.claude/tools/va_events.py` klassifiziert jede Eventdatei, die das Spiel jetzt lädt:
  - **Erde:** `s:`/`sr:` auf States/Regionen, die der Mod nicht hat, oder Vanilla-JEs/Erde-Länder/-Kulturen/-Religionen.
  - **Allgemein:** keine solchen Verweise, oder von Hand in `GENERIC` aufgenommen (Wahlen, Gesetze, Petitionen, Attentate, Unterdrückung, Lobbys …; 32 Dateien, die Erde-Länder/-Religionen oder Vanilla-JEs nur nebenbei nennen).
- 122 neue leere Dateien schalten Vanilla-Eventdateien mit Erde-Inhalt ab (`--stubs`). 32 leere Dateien gab es schon.
- Alte Mod-Kopien bereinigt (Liste: `VA-002-events-liste.txt`): 119 Kopien allgemeiner Events gelöscht (Vanilla 1.13 lädt), 27 Kopien von Erde-Events geleert. Befehl: `python -I .claude/tools/va_events.py --apply-copies`, Kontrolle ohne Option: `kopie-allgemein (0)`, `kopie-erde (0)`. Lint danach: 0 neue Fehler.
- Bewusst behalten: `events/agitators_events/coup_events.txt` (passt zur Mod-JE-Kopie `01_coup.txt`, siehe ABLAUFPLAN „Bewusste Vanilla-Overrides“).
- Event-Verweise: Nach dem Aufräumen zeigen 211 Verweise auf Events, die nicht mehr geladen werden (vorher 133; 101 neu, 23 behoben). Fast alle stehen in den alten Mod-Kopien der On-Actions (`common/on_actions/00_*.txt`) und Mod-JE-Kopien und zeigen auf abgeschaltete Erde-Events. Das gibt einmalige Ladefehler, keinen Spam. Die On-Action-Kopien bleiben vorerst (mit Vanilla-On-Actions wären es 297), Abbau mit VA-003.
- Gilneas: `common/journal_entries/VA_gilneas_infection.txt` ruft 18 Events aus `french_pretenders` auf (Vorlage war offenbar das Vanilla-JE der französischen Thronprätendenten). Diese Events gab es im Mod schon vorher nicht → VA-007 prüfen.

### Teil 2 (offen): journal_entries, scripted_buttons, company_types, character_templates

- Gleiches Vorgehen. `journal_entries` zuerst, weil die allgemeinen Events in `GENERIC` Vanilla-JEs brauchen (Attentate, Petitionen, Putsche, Unterdrückung, Lobbys).

### 2026-10-30 – Nachprüfung der abgeschalteten Events (Hinweis Christian: nihilism.txt)

- `va_events.py` wertet jeden `c:`/`cu:`/`rel:`-Verweis auf Erde-Objekte als Erde, auch reine Namensverzweigungen wie `c:RUS ?= THIS` mit Fallback. Dadurch wurden allgemeine Mechaniken abgeschaltet. Von den 181 Stubs haben 69 keinen `s:`/`sr:`-Verweis; das sind die Kandidaten.
- Umgesetzt (Christian: „alle 9“): alle neun stehen in `GENERIC`. Die zwei ohne JE sind wieder aktiv (Stub gelöscht per `--apply-copies`). Die sieben mit JE stehen in der neuen Skriptgruppe `stub-wartet-je` und kommen nach Teil 2 per `--apply-copies` automatisch frei. Lint: 0 neue Fehler. Test: T-018.
- Neue Skriptgruppen: `stub-pruefen` (60 Stubs ohne `s:`/`sr:`, bei Patches durchsehen), `stub-allgemein`, `stub-wartet-je`.
- Thematisch allgemein:
  - braucht Vanilla-JE, also erst mit Teil 2 zurück: `nihilism.txt` (`je_nihilist_movement`, Auslöser nur Technik/Gesetze), `agitators_events/silkworm_diseases.txt`, `balkans_events/hungry_forties.txt`, `balkans_events/grunderzeit.txt`, `iberia_events/ip4_coup_events.txt`, `iberia_events/negotiation_events.txt`, `iberia_events/ip4_election_rigging.txt` (nennt `je_coffee_with_milk` nur im `NOT`)
  - ohne JE, sofort möglich: `agitators_events/slave_revolt_events.txt`, `iberia_events/ip4_anarchism_events.txt`
- Klar Erde trotz fehlender State-Verweise: z. B. `scotland_yard.txt` (nur `c:GBR`), `titanic_events.txt`, Indien-, Japan-, Iberien-Länderreihen, Expeditionen.
- Markierung: Rücknahme über `GENERIC` in `va_events.py` (Stub löschen, Vanilla lädt). Zusätzlich soll das Skript Stubs ohne `s:`/`sr:` als eigene Gruppe „stub-pruefen“ ausgeben, damit solche Fälle bei Patches nicht still verschwinden.
