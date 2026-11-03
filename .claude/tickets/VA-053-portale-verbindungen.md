# VA-053: Portale und Verbindungen – Dunkles Portal, Dalaran-Portale, Tiefenbahn

- **Status:** offen
- **Typ:** content
- **Priorität:** mittel
- **Erstellt:** 2026-11-02

## Beschreibung

Kono (2026-11-02): Verbindung Azeroth–Outland/Draenor (Dunkles Portal), Dalaran-Portale zu den Hauptstädten, Tiefenbahn Stormwind–Ironforge. Inspiration: Mod „Realms of Exether“ (Workshop 3279217222).

## Notizen

### 2026-11-02 – Sichtung Realms of Exether

- Kein WoW-Mod, hat **keine Portale**. Brauchbar nur als Muster, keine Lizenzdatei gefunden → nichts kopieren, Vorbilder aus Vanilla nehmen.
  - Kanal-System (Survey-Decision → JE → Gebäude mit `strait = canal_…`, `strait_definitions` mit `type = artificial`) = Vanilla Suez/Panama (`common/decisions/`, `common/strait_definitions/strait_definitions.txt`).
  - `building_dwarf_tunnels` (Monument, `buildable = no`, `state_infrastructure_add`) → Muster für Tiefenbahn.
  - `je_electric_underground_railway` (Metro-JE: urban_center ≥ 20 + Bahn mit Elektro-PM) → Muster für Tiefenbahn-Bau-JE.
  - Ihre Land-„connection“-Gebäude (`canal = …`) sind auskommentiert, also aufgegeben.
- **Ist-Stand bei uns:** `map_data/adjacencies.csv` hat schon `x967141;x3406CB;special;…;DarkPortal` (Region 28 ↔ 29), also **dauerhaft offen**. Dazu 14 `sea`-Adjazenzen in Outland.
- **Befund:** Zeile `x31968A;x74BF34;special;…;Jan Mayen` ist ein Vanilla-Rest, verbindet aber zufällig zwei echte Provinzen in Nordend (`21_va_west_northrend.txt`, Z. 521 und 1304). Prüfen, ob gewollt, sonst löschen.

### 2026-11-02 – Was die Engine hergibt (Vanilla 1.13 geprüft)

- **Reisenetz:** `map_data/nodes.dat` ist binär und vom Spiel erzeugt (2,8 MB, Floats), nicht von Hand erweiterbar. Verbindungstypen darin sind fest eingebaut.
- **Einzige Stellschraube für neue Kanten:** Zeilen in `adjacencies.csv`. Typ `sea` = Land↔Land über Wasser (Vanilla 227×, z. B. Ireland-Scotland), Typ `special` = beliebige Entfernung (Vanilla nur Jan Mayen, bei uns DarkPortal). Eine Kante überspringt alles dazwischen, also auch fremde Länder. Statisch: zur Laufzeit nicht ein- oder ausschaltbar.
- **Geschwindigkeit:** keine Einstellung je Kante. Nur global `NMilitary.FORMATION_TRAVEL_NETWORK_SPEED = 15` und Modifier `military_formation_army_movement_speed_add/_mult` je Formation bzw. Land.
- **Meerengen/Kanäle** (`strait_definitions`, `strait = …` am Gebäude) sind laut `strait_definitions.md` rein See: zwei Land-Endpunkte (wer kontrolliert) und zwei See-Endpunkte (was verbunden wird). Variante B fürs Portal fällt damit weg, Landtruppen laufen dort nicht durch.
- **Markt:** Ob eine `special`/`sea`-Kante als Landverbindung für Marktzugang und Eingliederung zählt, ist nicht dokumentiert → Spieltest.
- **Ungeklärt:** ob nach einer neuen Adjazenz `nodes.dat` neu erzeugt werden muss (Ingame-Map-Editor) oder ob das Spiel die CSV beim Laden einrechnet.

### Vorschlag

- **Tiefenbahn:** neue Zeile `x0559B3;x083D75;special;-1;5815;792;6072;1210;;Tiefenbahn` (Stadtprovinzen STATE_STORMWIND ↔ STATE_IRONFORGE; Koordinaten aus `provinces.png`, y gespiegelt wie bei DarkPortal). Dazu optional ein Gebäude „Tiefenbahn“ in beiden States (Muster Zwergentunnel) für Infrastruktur und Marktzugang-Modifier.
- **Dunkles Portal:** bestehende `special`-Kante bleibt. Bis zur Öffnung (~15 Jahre, VA-034) politisch gesperrt: keine Kriegsziele/Plays zwischen Azeroth und Outland, Handel per Modifier gebremst.
- **Dalaran-Portale:** keine Kanten (wären statisch für alle). Stattdessen Scripted Button mit `teleport_to_front` und Portal-Gebäude mit Modifiern.
- **Erster Test** (klärt Tiefenbahn und Portal zugleich): Laufen Armeen über DarkPortal bzw. Tiefenbahn? Hat Ironforge Marktzugang zu Stormwind ohne Hafen? Meldet `error.log` etwas zu `adjacencies`?

### Offene Entscheidungen (Kono)

- Tiefenbahn-Zeile so eintragen?
- Dalaran: Wer bekommt Portale (Kirin-Tor-Partner, alle Hauptstädte, per Vertrag)?
- Tiefenbahn: ab Start vorhanden (Lore: vor Cataclysm gebaut) oder per JE?
