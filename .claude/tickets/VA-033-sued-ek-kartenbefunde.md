# VA-033: Süd-EK – Hubs und State-History-Provinz bereinigen

- **Status:** offen
- **Typ:** bug
- **Priorität:** niedrig
- **Erstellt:** 2026-10-30

## Beschreibung

Aufgefallen bei VA-029 (`python -I .claude/tools/va_check_states.py 28`):

- `STATE_JANSEN_STEAD`: port-Hub `x3C1493` liegt in `STATE_SENTINEN_HILL`
- `STATE_KURZENS_COMPOUND`: city-Hub `x81E032` und farm-Hub `x071B9C` liegen in `STATE_DEADMINES`
- `STATE_BOOTY_BAY` / `STEAMWHEEDLE_CARTEL`: Provinz `xF81480` in der State-History gehört nicht zur State Region (verwandt: VA-011)

## Notizen

- Hubs auf eine Provinz des eigenen States setzen. Bei der History-Provinz klären, zu welchem State sie gehört.
- Danach `va_check_states.py 28` erneut laufen lassen.
