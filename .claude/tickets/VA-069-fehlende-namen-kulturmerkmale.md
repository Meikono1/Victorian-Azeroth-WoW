# VA-069: Fehlende Namen für Sprachen, Traditionen und Erbe-Merkmale

- **Status:** offen
- **Typ:** lokalisierung
- **Priorität:** mittel
- **Erstellt:** 2026-11-12

## Beschreibung

Kono-Test T-116 (2026-11-12): Sprache „Elven“ und Tradition „Magical Lowlands“ zeigten den rohen Key. Prüfung aller Merkmale in `common/discrimination_traits/va_*.txt` gegen die englische Loc: es fehlen rund 300 Namen.

- `va_languages.txt`: 37 Sprachen (alle außer jetzt `language_elfen`), Schlüssel `language_<name>`.
- `va_traditions.txt`: rund 225 Traditionen, Schlüssel `tradition_<name>` (Tippfehler im Objekt `tradition_cetradition_ntaur` prüfen).
- `va_cultural_heritages.txt`: 22 Erbe-Merkmale (`<volk>_heritage`).
- `va_religious_heritages.txt`: 14 (`heritage_<name>`).

## Notizen

- 2026-11-12, Claude: Behoben `language_elfen` („Elven (AI WRITTEN)“), Keys `magical_lowlands` → `tradition_magical_lowlands`, `marshland` → `tradition_marshland` (`va_culture_traits_l_english.yml`). `magical_highlands` hat kein passendes Objekt mehr, prüfen.
- Vorschlag: Namen per Skript aus den Objektnamen vorschlagen (Titel-Schreibweise, WoW-Eigennamen von Hand), Kono nimmt die Liste ab. Prüfskript: Objektnamen gegen alle `localization/**/*english*.yml` abgleichen (in VA-023-Lint aufnehmen).
