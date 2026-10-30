# VA-043: error.log 30.10. – Restbefunde aus Mod-Dateien

- **Status:** offen
- **Typ:** bug
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Lauf 30.10. 17:50–17:52 (vier Logdateien, rund 19.800 Zeilen, Repo gleich Mod-Ordner). Behoben ist schon, was in T-033 steht. Offen sind die folgenden Punkte, sortiert nach Gewicht:

| Befund | Ort | Zuständig |
|---|---|---|
| 312 Landprovinzen ohne State Region („missing state region“) | ehemalige `STATE_TEST`-Splitter | VA-031 (Kono: bleiben vorerst liegen) |
| 31 Provinzen in der History ohne State Region | `common/history/states/VA_pandaria.txt:1047–1110` | VA-031/VA-032 |
| Provinzen in mehreren State Regions | `VA_eastern_kingdoms_states.txt:1145, 2286` (`x55EC94`, `x5F8C33`), `VA_northrend_state.txt:121, 248, 285` | VA-011 |
| Holzfäller-PMs auf Farmen/Plantagen | `common/history/buildings/23_north_kalimdor.txt:693, 773, 885` (Exodar, Azure Watch, Wildwind Peak, Stillpine Hold) | VA-038 |
| `region_state` ungültig (Land ohne State) | `common/history/pops/va_center_eastern_kingdoms.txt:336` | VA-024 |
| `size = zombie` | `common/history/pops/va_outlands.txt:1618` | VA-029 (Region 29) |
| Gilneas-JE ruft Frankreich-Inhalte (`je_divided_monarchists`, `fra_clear_divided_monarchist_variables`) | `common/journal_entries/VA_gilneas_infection.txt:40, 243, 259, 450` | VA-007 |
| Unzulässige Start-Gesetze (Zandalar, Wretched u. a.) | `common/history/countries` | VA-014 |
| Ungültige Zeichen in Loc-Keys (`’`, `Ö`): Namenslisten, `HUB_NAME_STATE_SKÖRN_*` | `localization/replace/english/va_*_names_l_english.yml`, `va_hub_names_l_english.yml:532–535` | hier |
| Doppelte Ressourcen-Einträge | State Regions Manaforge B'naar, `STATE_AREA_*`, Broken Wilds | VA-029 (Region 29) |
| 367 Festungs-Locators in Nicht-Land-Provinzen, Port-Locators mit `building_shipyard` | `gfx/map/…` (Map-Editor) | Kono, beim Neuzeichnen |
| Fehlende Wappen-Texturen (`ce_dragon`, `ce_nethergarde_tower`, `ce_block_*` …) | `gfx/coat_of_arms` | VA-027 |

Kein Problem aus Mod-Sicht: rund 300 Kleidungs-/Hut-Fehler zu Erde-Charaktervorlagen (`has_template … BRZ_virgulino_ferreira` usw.). Das sind Vanilla-Porträtdateien, deren Vorlagen seit VA-002 Teil 3 abgeschaltet sind. Sie stören nicht, solange wir `01_clothes.txt` nicht kopieren.

## Notizen
