# VA-014: Unzulässige Start-Gesetze in der Länder-History

- **Status:** wartet (Spieltest)
- **Typ:** bug
- **Priorität:** mittel
- **Erstellt:** 2026-10-29

## Beschreibung

Beim Spielstart meldet `error.log` 141× `Country X is not permitted to retain law …, fix this or consider … instead` für 75 Länder. Das Spiel tauscht die Gesetze dann selbst aus. Häufig: Protectionism (17), Traditionalism, Serfdom, Interventionism (je 14), No Police, Homesteading, Censorship (je 12), Mercantilism (11), Outlawed Dissent (9).

Vermutlich fehlen den Ländern seit 1.12/1.13 die nötigen Technologien bzw. die Gesetze haben neue Bedingungen. In `common/history/countries/` je Land das vorgeschlagene Ersatzgesetz eintragen oder die Start-Technologien anpassen.

## Notizen
- 2026-11-03: Alle 137 Meldungen „not permitted to retain law“ (Log 03.11.) behoben: Fallback-Gesetz des Spiels in die History geschrieben, widersprechende `activate_law` entfernt, `va_decentralized_countries.txt` für die sieben Kontinent-Tags. Inhaltlich gewollte Gesetze (z. B. Zensur bei den Wretched) brauchen dafür die passende Technologie. Test T-079.
