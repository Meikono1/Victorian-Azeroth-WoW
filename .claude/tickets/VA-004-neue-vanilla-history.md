# VA-004: Neue Vanilla-History-Ordner abfangen

- **Status:** offen
- **Typ:** technik
- **Priorität:** mittel
- **Erstellt:** 2026-10-29

## Beschreibung

Seit 1.11 hat Vanilla neue Ordner unter `common/history/`: `conscription`, `cultures`, `government_setup`, `governments`, `military_deployments`, `political_movements`. Die sind nicht in `replace_paths` und laden Erde-Inhalte (z. B. 21 Länder-Referenzen in political_movements). In replace_paths aufnehmen oder Dateien leer überschreiben.

## Notizen

