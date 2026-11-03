# VA-004: Neue Vanilla-History-Ordner abfangen

- **Status:** erledigt
- **Typ:** technik
- **Priorität:** mittel
- **Erstellt:** 2026-10-29

## Beschreibung

Seit 1.11 hat Vanilla neue Ordner unter `common/history/`: `conscription`, `cultures`, `government_setup`, `governments`, `military_deployments`, `political_movements`. Die sind nicht in `replace_paths` und laden Erde-Inhalte (z. B. 21 Länder-Referenzen in political_movements). In replace_paths aufnehmen oder Dateien leer überschreiben.

## Notizen

- 2026-10-30: `replace_paths` wirkt nicht rekursiv, `common/history` allein deckt die Unterordner nicht ab. Bestand je Vanilla-Ordner geprüft:
  - **In `replace_paths` aufgenommen** (nur Erde-Inhalte, künftige Patch-Dateien fallen automatisch weg): `ai`, `diplomatic_plays` (neu: Carlistenkrieg, Fezzan, Ladakh), `government_setup`, `governments`, `lobbies`, `military_deployments` (warf `p:`-/`has_template`-Fehler im Log), `military_formations`, `trade`, `treaties`.
  - Mod-Kopien mit Erde-Inhalt in diesen Ordnern geleert: `ai/00_secret_goals.txt`, `ai/00_strategy.txt`, `military_formations/00_military_formations_europe.txt`. Allgemeiner Subject-Teil der KI-Strategie neu als `ai/va_ai_strategy.txt`.
  - **Per leerer Datei abgeschaltet, allgemeiner Teil als `va_`-Datei:** `cultures/00_cultures.txt` → `va_cultures.txt` (Grund-Fervor 5), `political_movements/00_movements.txt` → `va_movements.txt` (Royalisten, Liberale, Arbeiter, Sklaverei, religiöse/kulturelle Mehrheit; ohne Erde-Länder und ohne deutsche/italienische Nationalbewegung).
  - **Bleibt Vanilla:** `conscription` (allgemein). Seine Log-Fehler (`is_building_type` false) kommen daher, dass die alte Kopie `common/buildings/05_military.txt` noch `building_barracks` statt `building_barrack` definiert → VA-003.
  - Schon vorher abgedeckt: `buildings`, `global`, `power_blocs`, `production_methods` (Mod-Dateien gleichen Namens).
- Test: T-034 (2026-10-30): Bewegungen da, Log sauber bis auf `conscription` (VA-003). **Aber:** Fervor startet bei 0 statt 5 (Ziel 7), `va_cultures.txt` greift nicht.
- 2026-10-30: `va_cultures.txt` ohne die Vanilla-Bedingung (`NOT any_scope_culture … count = all`) neu geschrieben, plus Kontrollwert `cu:sin_dorei` = 10 (Direktaufruf wie Vanilla `cu:british`). T-035 zeigt, ob die Schleife oder die History an sich nicht greift. Kontrollwert danach entfernen. Hinweis: `culture_current_fervor` steht nicht in der Script-Doku (Stand Nov. 2025, vor 1.13) – `script_docs` neu erzeugen wäre gut.
- T-035 (2026-10-30): Blood Elf 10, Stormwindian 0, Bronzebeard 0 → `cu:<kultur> = { set_fervor = N }` wirkt, die Schleife über `every_country` nicht (zur History-Zeit haben Länder vermutlich noch keine Scope-Kulturen). `va_cultures.txt` jetzt mit 86 Einzeleinträgen (alle Kulturen aus `common/cultures/`, gruppiert nach Datei), Kontrollwert entfernt. **Neue Kulturen müssen dort ergänzt werden** (Hinweis im Dateikopf). Test: T-036 OK (2026-10-30), alle drei Kulturen bei 5, Log sauber.

