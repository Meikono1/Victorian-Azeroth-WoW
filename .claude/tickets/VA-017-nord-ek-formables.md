# VA-017: Nord-EK – Formables

- **Status:** offen
- **Typ:** content
- **Priorität:** hoch
- **Erstellt:** 2026-10-29

## Beschreibung

Der Mod hat keine eigenen Formables. `common/country_formation/00_major_formables.txt` ist eine alte Vanilla-Kopie (GER, ITA, SCA, FND mit Erde-Kulturen), `00_formable_countries.txt` ist leer (schaltet Vanilla ab). `common/country_creation/00_releasable_countries.txt` ist ebenfalls eine Erde-Kopie.

Vorschlag Nord-EK (neue Tags inkl. `country_definitions`, Loc, Wappen):
- `LORDAERON` – Kultur `lordorean`, aus Scarlet/Argent/Andorhal
- `QUEL_THALAS` – `sin_dorei`/`quel_dorei`, aus Silvermoon/Tranquillien/Wretched/Highvale
- `ALTERAC` – `alteraci`, aus Syndicate
- `AMANI_EMPIRE` – `forest_troll`, aus Amani (Zul'jin), Shadowpine, Mossflayer (ggf. Major Formation)
- `STROMGARDE`/`ARATHOR` – menschliche Kultur der Arathi (Kultur fehlt bisher)

Vorlage: Vanilla 1.13 `common/country_formation/00_formable_countries.txt` (`states = {…}` oder `use_culture_states = yes`, `required_states_fraction`). Für Major Formations zusätzlich eigene Diplomatic Plays nötig.

## Notizen

- Die alte Kopie `00_major_formables.txt` sollte durch eine leere Datei ersetzt werden (VA-003), sobald eigene Formables existieren.
- 2026-10-30: `AMANI_EMPIRE` nur aus Amani (Zul'jin), Shadowpine und Mossflayer (siehe VA-022).
- 2026-10-30: `AMANI_TRIBE` heißt „Zul'Jarra“ (Loc in `va_countries_l_english.yml`), bis es `AMANI_EMPIRE` bildet.
