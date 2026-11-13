# VA-017: Nord-EK – Formables

- **Status:** in Arbeit
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
- 2026-11-12, Kono-Test T-114: Nach „Vengeance for Zul'Aman“ gibt es nur Prestige, eine Nation-Formation ist nicht möglich. Kono will das Amani-Reich richtig bilden können (Formable `AMANI_EMPIRE`, Namenswechsel Zul'Jarra → Amani-Reich, Platzhalter-TODO in `common/journal_entries/va_amani.txt`). Ob es in den Release Version 3 gehört, entscheidet Kono (VA-072).
- 2026-11-12, Kono: Amani-Reich gehört in Version 3. **Gescriptet:** Formable `AMANI_EMPIRE` (`common/country_formation/va_formable_countries.txt`, Vorbild Vanilla `BYZ`): States Zul'Aman, Tor'Watha, Dawnstar Spire, Sanctum of Sun, Suncrown Village, Zul'Mashar, 66 % nötig, nur mit `va_amani_empire_restored` aus `je_amani_empire`. Normales Formable, keine Major Formation. Länderdefinition (Imperium, forest_troll/dire_troll, Hauptstadt Zul'Aman), Wappen mit `ce_troll_mask_zuljin.dds`, Namen „Amani Empire“/„Amani“ ohne AI-WRITTEN-Marker (Kono-Vorgabe „Amani-Reich“). Hinweis im Event `amani_events.11`. Test T-132.
- 2026-11-13, Kono-Test T-132 OK. Erweitert um Northpass Tower, East Sanctum, Sunsail Anchorage, Duskwither Spire (10 States, 0,5). Wappen getauscht: Reich grün mit Adler-Loa (bisher Zul'Jarra), Zul'Jarra türkis mit Zul'jins Maske (NewFlags.txt). Dazu die ganzen Ghostlands (Windrunner Village, Tranquillien, Deathholme; 13 States; Kono 2026-11-13: 9 nötig, 0,69). Offen: eigene Kultur/Wappen für das Reich später.
