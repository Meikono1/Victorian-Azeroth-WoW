# VA-055: Ungültige Pop-Größe „zombie“ in Outland

- **Status:** offen
- **Typ:** bug
- **Priorität:** niedrig
- **Erstellt:** 2026-11-03

## Beschreibung

`common/history/pops/va_outlands.txt` (ca. Z. 1618): `s:STATE_EXPEDITION_ARMORY` → `region_state:UNYIELDING_DEFENDER` → `create_pop = { culture = stormwindian size = zombie }`. `size` muss eine Zahl sein; vermutlich ist beim Bearbeiten Kultur und Größe vertauscht oder eine Zombie-Pop gemeint.

Gefunden von `va_country_overview.py` (Warnung „Ungültige Pop-Größe“).

## Notizen
- Kono entscheidet: Größe für die Sturmwind-Pop und ob zusätzlich eine Zombie-Pop gedacht war.
- 2026-11-03: Platzhalter `size = 12800` mit TODO gesetzt, damit die Pop entsteht (VA-043). Entscheidung von Kono bleibt offen.
