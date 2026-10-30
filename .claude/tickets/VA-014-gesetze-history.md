# VA-014: Unzulässige Start-Gesetze in der Länder-History

- **Status:** offen
- **Typ:** bug
- **Priorität:** mittel
- **Erstellt:** 2026-10-29

## Beschreibung

Beim Spielstart meldet `error.log` 141× `Country X is not permitted to retain law …, fix this or consider … instead` für 75 Länder. Das Spiel tauscht die Gesetze dann selbst aus. Häufig: Protectionism (17), Traditionalism, Serfdom, Interventionism (je 14), No Police, Homesteading, Censorship (je 12), Mercantilism (11), Outlawed Dissent (9).

Vermutlich fehlen den Ländern seit 1.12/1.13 die nötigen Technologien bzw. die Gesetze haben neue Bedingungen. In `common/history/countries/` je Land das vorgeschlagene Ersatzgesetz eintragen oder die Start-Technologien anpassen.

## Notizen

