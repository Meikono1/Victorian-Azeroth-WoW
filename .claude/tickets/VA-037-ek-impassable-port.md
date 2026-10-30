# VA-037: Eastern Kingdoms – falsche impassable- und port-Einträge entfernen

- **Status:** offen
- **Typ:** bug
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Kono 2026-10-30: Die impassable- und Port-Einträge in den EK-Regionen müssen noch weg. Betroffen sind `map_data/state_regions/26_…`, `27_…` und `28_…`. Zusammen stehen dort 253 Zeilen mit `impassable` oder `port =` (26: 112, 27: 80, 28: 61).

## Notizen

- Noch zu klären: Fliegen **alle** Einträge raus, oder nur die, deren Provinz nicht (mehr) im State liegt bzw. nicht an der Küste? Die Hubs `port = "x…"` hängen an den Start-Häfen aus VA-029 (`va_add_ports.py`). Ein State mit Hafengebäude braucht einen gültigen `port`.
- Kono 2026-10-30: Einige States haben noch Meereszugang, der weg muss. Das macht Kono selbst im Editor (Kleinigkeiten).
- Vorschlag: per Skript prüfen (Provinz im State? Küste?) und nur die ungültigen entfernen.
- 2026-10-30 (T-003): Nicht alle Bergprovinzen sind impassable, dadurch grafische Fehler bei Stadt-/Hafenmarkern. Kono sieht es sich später an; Prüfung zusammen mit diesem Ticket.
