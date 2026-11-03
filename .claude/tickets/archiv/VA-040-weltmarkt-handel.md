# VA-040: Weltmarkt – kein Land handelt

- **Status:** erledigt
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

- 2026-10-30: Ursache gefunden. 1.13 handelt nur über `building_trade_center` (Vanilla `11_private_infrastructure.txt`: `state_weekly_trades_add`, `state_trade_capacity_add`). Vanilla setzt sie in der Gebäude-History (FRA 1836: 27 Stufen, PRU 15, GBR 60), der Mod hatte **keine einzige**. Weltmarkt-Standort `x74FAFA` ist gültig (Ozean, in `sea_starts`, 52.000 Pixel). Gesetze: 241 Länder ohne Handelsgesetz bekommen über `effect_starting_politics_traditional` Merkantilismus (decentralized: Isolationismus), 46 Protektionismus, 32 explizit Isolationismus. error.log ohne Handelsfehler.
- 2026-10-30: Werkzeug `.claude/tools/va_add_trade_centers.py` (Probelauf ohne `--apply`). Regeln: Land hat Hafen (Merchant Marine ist Input), kein Isolationismus, mind. 100.000 Pops; Zentrale in der Hauptstadt, 1 Stufe je Mio. Pops, 1–10. Angewandt auf 26–28: **43 Zentralen, 125 Stufen** (Stand vor dem Goblin-Fix) (Stormwind, Undercity, Vashj'ir, Ironforge je 10, Gilneas 8, Silvermoon 5). Testfälle T-037, T-038.
- Offen: Kalimdor (23–25) bewusst ausgelassen wegen Neuzeichnen (VA-038); Probelauf ergibt dort 65 Zentralen. Danach `va_add_trade_centers.py 23 24 25 --apply`.
- 2026-10-30: Goblins geprüft. `va_add_ports.py` zählte Häfen je State statt je Land: Steamwheedle (6,8 Mio. Pops) galt als versorgt, weil Nachbarn in geteilten States (Jaguero, Stagelbog …) einen Hafen haben. Behoben. Neu in 26–28: Häfen für Steamwheedle (Booty Bay, 2), Hammerfall (1), Dabyrie (1) und Handelszentralen dort (Booty Bay 7, je 1). Summe EK jetzt **46 Zentralen, 134 Stufen**. In Kalimdor ergibt der Probelauf noch Häfen für Wrathscale und Bristlelimb, das kommt nach VA-038.
- Offen: `VENTURE_CO` hat nur Binnen-States (Nozzlepot's Outpost, Golden Plains, Great Gate, Bambala), also weder Hafen noch Zentrale. Lore-mäßig okay (Bergbau-Firma). Bei Bedarf später eine Zentrale ohne Hafen setzen, die Merchant Marine kommt dann über den Markt.
- Offen: Merchant Marine reicht in großen Zentralen evtl. nicht (Hafen 1–3 Stufen à 10, Zentrale braucht 4 je Stufe). Im Spieltest beobachten, sonst Häfen der Hauptstädte anheben.
- 2026-10-30: T-037 und T-038 OK, Ticket erledigt. Kalimdor-Zentralen und -Häfen folgen mit VA-038 (Notiz dort).
