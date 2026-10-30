# VA-036: Allianz – gemeinsamer Markt für Ironforge, Gnomeregan und Stormwind

- **Status:** offen
- **Typ:** technik
- **Priorität:** hoch
- **Erstellt:** 2026-10-30

## Beschreibung

Spieltest Kono: Gnomeregan und Ironforge sollten über die Allianz einen Markt haben, sind aber aus dem Machtblock ausgetreten. Ironforge soll über Loch Modan versorgt werden und an Stormwind angebunden sein. Gnomeregan braucht einen fertigen Hafen zum Handeln.

## Analyse 2026-10-30

- Machtblock `ALLIANCE_OF_STORMWIND` in `common/history/power_blocs/` mit `identity_ideological_union` und `principle_ideological_truth_2`: **kein gemeinsamer Markt**.
- Vanilla 1.13: Gemeinsamer Markt über `principle_market_unification_2` (`power_bloc_customs_union_bool`) oder die Identität `identity_trade_league` (hat die Zollunion fest eingebaut). Beides braucht die DLC-Funktion `power_bloc_features` (Sphere of Influence).
- Weltmarkt-Zugang läuft in 1.13 über Handelsknoten; Hafenstufen zählen stark. Seit 2026-10-30 haben alle Küstenländer Azeroths mit Tech-Stufe 1–5 einen Start-Hafen (`va_add_ports.py`, VA-029): u. a. Stormwind 3, Ironforge 3 (Coldridge Valley), Gnomeregan 1, Defias 1 (Deadmines).

## Vorschläge (Entscheidung Kono)

1. Allianz-Prinzip `principle_market_unification_2` von Beginn an (Zollunion, nur mit DLC).
2. Ohne DLC: Ironforge und Gnomeregan als Untertanen mit gemeinsamem Markt (Vanilla-Untertanentyp mit Zollunion prüfen) – passt lore-seitig schlecht.
3. Austritt verhindern: Kohäsion bzw. Gründe für den Austritt prüfen (Spielstand, Machtblock-Fenster).
- Loch Modan: Thelsamar gehört schon zu Ironforge, Versorgung läuft über den eigenen Markt, sobald Infrastruktur reicht.
