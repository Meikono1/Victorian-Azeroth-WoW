# VA-040: Weltmarkt – kein Land handelt

- **Status:** offen
- **Typ:** bug
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Kono 2026-10-30: Der Weltmarkt funktioniert nicht, weil kein Land handelt. Das verschärft die Hungersnot (VA-029): Engpässe auf einem Markt werden nicht über Importe ausgeglichen.

## Zu prüfen

- Weltmarkt-Standort: `NEconomy.WORLD_MARKET_LOCATION` in `common/defines/va_OVERWRITE_defines.txt`. Zeigt er auf eine gültige Meeresprovinz mit Verbindung zu den Seewegen?
- Handel in 1.13 läuft über Handelsrouten bzw. -knoten und braucht Häfen und Konvoikapazität. Seit VA-029 haben die Küstenländer in 21–28 Start-Häfen. Erreichen Seewege und `naval_exit_id` den Weltmarkt?
- Haben die Länder die Techs und Gesetze, die der Handel braucht (Handelspolitik `law_…_trade`, Merkantilismus/Protektionismus)? Vergleich Vanilla `common/history/countries`.
- Fehlen Vanilla-Defines oder -Objekte, die Erde-Provinzen voraussetzen (Strait-Definitions VA-012, Seegebiete)?
- In einem Spielstand prüfen: Handels-Lens, Marktübersicht eines Küstenlandes (Stormwind, Theramore).
- Verwandt: VA-036 (Allianz-Markt).

## Notizen
