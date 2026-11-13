# VA-067: Sylvanas stirbt nach 3–4 Jahren

- **Status:** offen
- **Typ:** bug
- **Priorität:** hoch
- **Erstellt:** 2026-11-10

## Beschreibung

Kono (2026-11-10): Im Test starb Sylvanas nach 3–4 Jahren Spielzeit, Varimathras (Erbe, `heir = yes`) übernahm Undercity. Untote und Dämonen sollen sehr langlebig sein.

## Notizen

- 2026-11-10, Kono: Die Lebensdauer-Eigenschaft (`trait_50000_lifespan`, vergeben in `trait_generation` von `00_default_template.txt`) kommt auch bei Anführern der Untoten an, schon getestet. Claudes erster Verdacht (Eigenschaft fehlt bei Vorlagen mit eigenen `traits`) ist damit vom Tisch; der Umbau dafür wurde zurückgenommen.
- Geprüft (Claude, 2026-11-10), scheidet aus:
  - Natürlicher Tod: Gesundheit ist per `MAX_CHARACTER_HEALTH = 5000` gedeckelt (`va_OVERWRITE_defines.txt`), die Vanilla-Formel (NCharacters in `00_defines.txt`) ergibt damit 37.000 bis 112.000 Jahre. Sylvanas ist 2.800.
  - `assassination_events.1`: in 1.15 per `always = no` abgeschaltet.
  - Duell `character_events.3`: schließt Herrscher und Unsterbliche aus.
- Noch offen als Ursache: übrige Vanilla-Events mit `kill_character`, die der Mod nicht abschaltet (`revolution_events_01/02`, `exiles_events`, `agitators_election_events`, `ig_suppression_events`, `secession_situations`, `law_events/*`, `train_events`), Bürgerkrieg/Revolution, Regierungswechsel.
- **Nächster Schritt:** Kono achtet beim nächsten Mal auf die Meldung (Todesursache bzw. Event-Titel) oder hebt einen Spielstand kurz davor auf. Dann gezielt das Event abfangen.
- Mögliche Absicherung, falls es ein Event ist: Vanilla schützt Figuren mit `set_character_immortal = yes` (Muster `history/characters/aus - austria.txt`), viele Vanilla-Events prüfen `is_immortal = no`. `kill_character` selbst tötet aber auch Unsterbliche.
