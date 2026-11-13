---
name: va-testrunde
description: Änderungen am Victorian-Azeroth-Mod prüfen und abschließen – Lint laufen lassen, Testfälle T-NNN in TESTPROTOKOLL.md anlegen, error.log nach einem Spielstart auswerten, Testergebnisse von Kono übernehmen, Ticket-Status und Übersicht nachziehen. Nutzen nach jeder Mod-Änderung, wenn Kono getestet hat ("hab getestet", "error.log", "T-0xx OK") oder ein Ticket fertig werden soll.
---

# Testrunde (Victorian Azeroth)

Es gibt keinen Build. Verlässlich sind nur Lint (statisch) und `error.log` (Spielstart). Nie Korrektheit behaupten, sondern um einen Spielstart bitten.

## A. Nach einer Änderung (Runde vorbereiten)

1. **Lint**: `python -I .claude/tools/va_lint.py --regions <NN …>` (Regionen nur, wenn States/Pops/Gebäude betroffen; Präfixe in `.claude/KARTE.md`). Letzte Zeile muss `… davon 0 neue Fehler` lauten (Exit-Code 0). Laufzeit wenige Sekunden.
   - Neue Fehler beheben, nicht verstecken. `--update-baseline` nur nach Abbau von Altlasten oder mit Konos Zustimmung.
   - `--full` nur, wenn eine Gruppe abgeschnitten ist und sie gebraucht wird.
2. **Testfälle** in `.claude/TESTPROTOKOLL.md` eintragen. Die Datei nicht ganz lesen:
   - Nächste freie ID (beide Dateien!): `grep -ho "^### T-[0-9]*" .claude/TESTPROTOKOLL.md .claude/TESTPROTOKOLL_ARCHIV.md | sort -t- -k2 -n | tail -1`
   - Nächste Rundennummer ebenso: `grep -ho "^## Runde [0-9]*" .claude/TESTPROTOKOLL*.md | sort -k3 -n | tail -1`
   - Neue Runde unten anhängen (Format unten), oder an die offene Runde desselben Tickets anhängen.
   - Jede Runde endet mit einem Log-Testfall „error.log: … (Claude)“, der die betroffenen Dateien und Objektnamen aufzählt.
3. **Ticket**: Status `wartet (Spieltest)`, Notiz mit Datum, Dateien, offenen Punkten und den Test-IDs. Tabelle in `.claude/tickets/README.md` gleich ziehen.
4. **ABLAUFPLAN.md**: Zeile „Nächster Spieltest“ um die neue Runde ergänzen; bei größeren Schritten Eintrag unter „Erledigt“ (Datum, Ticket, ein Satz, „wartet auf Spieltest“).
5. Kono sagen: welche Runde, was zu tun ist, Lint-Ergebnis.

Format einer Runde:

```
## Runde N – <Thema> (Stand JJJJ-MM-TT)

Ticket: VA-NNN. Lint vor Freigabe: 0 neue Fehler (JJJJ-MM-TT).

### T-NNN <Kurztitel> (VA-NNN)
- **Schritte:** <was Kono im Spiel tut, mit Land, Menü, Konsole>
- **Erwartet:** <sichtbares Ergebnis, genaue Texte inkl. "(AI WRITTEN)", Zahlen>
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:

### T-NNN error.log: <Thema> (Claude)
- **Schritte:** Nach T-… Claude Bescheid geben.
- **Erwartet:** Keine Zeilen zu `<datei>`, `<objekt>`, …
- **Ergebnis:** [ ] OK  [ ] Fehler – Notiz:
```

## B. Nach Konos Spieltest (auswerten)

1. **Log zusammenfassen**, immer mit dem Mod-Filter zuerst:
   `python -I .claude/tools/va_errlog.py --mod --top 40`
   - Gezielt: `--filter va_silvermoon` (Dateiname oder Objekt), `--by-file` für den Überblick je Datei.
   - Ohne `--mod` nur, wenn ein Absturz oder Fehler ohne Dateibezug gesucht wird.
   - Rohes `error.log` nie ganz lesen (bis 6 × 512 KB). Wenn nötig: `grep -n "<datei>" "$USERPROFILE/Documents/Paradox Interactive/Victoria 3/logs/error.log" | head`.
2. **Bewerten**: Relevant sind Zeilen mit Dateien dieser Runde. Bekannte Altlasten nicht neu melden: alte Vollkopien (`00_*`, `01_*`: VA-003), Erde-Bezüge (`je_acw_*`, `country_is_in_europe`: VA-002/VA-025/VA-026), `fleet_dioramas`, Fortification-Locator (Karte). Neue Fehlergruppen außerhalb der Runde → Ticket anlegen bzw. VA-043 ergänzen.
3. **Ergebnis eintragen**: Beim Log-Testfall `[x] OK` oder `[x] Fehler – Notiz: <Datum>, <Befund>`. Konos Ergebnisse übernimmt Claude nur, wenn Kono sie nennt; Konos eigene Häkchen nicht ändern.
4. **Fehler beheben** → neue Teilrunde oder Testfall erneut („T-054 danach erneut testen“), Ticket-Notiz mit Ursache.
5. **Ticket schließen**: erst `erledigt`, wenn **alle** Testfälle des Tickets von Kono mit OK bestätigt sind. Dann Status im Ticket und in `tickets/README.md`, Testfälle in ABLAUFPLAN „Nächster Spieltest“ austragen.
6. **Archivieren** (ohne Nachfrage):
   - Jeden Testfall mit OK (oder entfallen/per Folgetest erledigt) einzeln nach `.claude/TESTPROTOKOLL_ARCHIV.md` unter seine Runde verschieben (Kono 2026-11-12: im Protokoll nur Offenes). Runde ohne offene Fälle ganz verschieben, Archiv nach Rundennummer sortiert.
   - Ticket `erledigt` oder `verworfen` → Datei nach `.claude/tickets/archiv/`, relative Links darin `../` → `../../`, Link in `tickets/README.md` auf `archiv/…`. Die Tabelle behält alle Tickets.
   - Wird ein archiviertes Ticket wieder aufgemacht, zurück nach `tickets/`.

## C. Nebenbei

- Fallen beim Auswerten wiederkehrende Fehlerursachen auf, in den Stolperfallen des passenden Skills eintragen (`va-content`, `va-karte`).
- Neue Dateien/Objekte aus dem Fix in `.claude/KARTE.md` nachtragen.
