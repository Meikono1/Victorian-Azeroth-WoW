# VA-018: STATE_TEST auflösen

- **Status:** offen
- **Typ:** bug
- **Priorität:** mittel
- **Erstellt:** 2026-10-29

## Beschreibung

`STATE_TEST` (id 2699, Ende von `26_va_north_eastern_kingdoms.txt`) sammelt 312 Provinzen aus der ganzen Karte (Schwerpunkt bei x≈4800/y≈3100, also nicht Nord-EK). Keine Hubs, keine Strategic Region, kein Besitzer. Die Hubs von u. a. `STATE_LARGO_OVERLOOK`, `STATE_DARKWOOD`, `STATE_FARSON_HOLD`, `STATE_FORGOTTEN_HILL`, `STATE_IRONCLAD_GARRISON`, `STATE_BARADIN_HOLD`, `STATE_WARDENS_VIGIL` zeigen auf Provinzen in `STATE_TEST` – vermutlich wurden dort beim Karten-Umbau ganze States hineingeschoben.

Lösung: Provinzen per Nachbarschaft/Hub-Verweis zurück in ihre States verteilen (`va_check_states.py 26 --assign-test` als Startpunkt; 191 Provinzen grenzen nur an andere TEST-Provinzen, 102 an Meer), danach `STATE_TEST` und den leeren Block in `common/history/buildings/26_north_eastern_kingdoms.txt` entfernen.

## Notizen
