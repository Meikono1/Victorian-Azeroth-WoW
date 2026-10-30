# VA-045: Schiffsbau-Tab zeigt Test-Icon (Smiley)

- **Status:** offen
- **Typ:** grafik
- **Priorität:** niedrig
- **Erstellt:** 2026-10-30

## Beschreibung

Bauübersicht → Reiter „Ships“: Links steht ein graues Smiley-Icon (Platzhalter- bzw. Fehlgrafik der Engine), daneben das Feld „No“, Kapazität 0/0, £ 0.00. Gefunden von Kono im Spieltest Runde 9.

## Notizen

- 2026-10-30: Vermutung: Bild des Schiffstyps bzw. der Werft fehlt, oder eine Textur wird mit leerem Dateinamen geladen. `error.log` vom 30.10. (20:58–21:02) meldet wiederholt `Could not find texture due to 'VFSOpen Error: gfx/map/textures/ not found'` (leerer Name). Ob das dazu gehört, ist offen.
- Nächste Schritte: in Vanilla `gui/construction_panel.gui` nachsehen, welche Textur das Bild links zieht (Schiffstyp, Werft, Land), und gegen die Mod-Dateien (Schiffs-/Einheitentypen, `gfx/`) prüfen. Mod hat keinen eigenen `gui`-Ordner.
