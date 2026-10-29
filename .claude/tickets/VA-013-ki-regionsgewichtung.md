# VA-013: KI-Regionsgewichtung für Azeroth

- **Status:** offen
- **Typ:** content
- **Priorität:** niedrig
- **Erstellt:** 2026-10-29

## Beschreibung

`common/ai_strategies/va_default_strategy.txt` ersetzt `strategic_region_scores` der Vanilla-Standardstrategie durch die neutralen Teile (Grundwert, Heimat, Kolonien). Die Erde-Sonderfälle (Ägypten-Krise, Scramble for Africa, Monroe-Doktrin …) sind raus. Azeroth-Gegenstücke ergänzen, z. B. Allianz/Horde an umstrittenen Regionen, Interesse an Northrend/Outland.

Andere `sr:`-Bezüge in der Vanilla-Strategie (`state_value`, `aggression`, `secret_goal_scores`, `wargoal_scores` …) erzeugen derzeit keine Fehler, prüfen falls sie im Log auftauchen.

## Notizen

