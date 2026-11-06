# VA-064: Kupfer-Vorkommen in Azeroth (neues Gut seit Patch)

- **Status:** wartet (Spieltest)
- **Typ:** content
- **Priorität:** mittel
- **Erstellt:** 2026-11-06

## Beschreibung

Vanilla 1.15 hat das Gut `copper` (`common/goods/00_goods.txt`) und das Gebäude `building_copper_mine` (`common/buildings/03_mines.txt`, Gruppe `bg_mining`, freigeschaltet mit `shaft_mining`). In Vanilla haben 84 State Regions `building_copper_mine = N` in `capped_resources`. Im Mod gibt es bisher kein einziges Vorkommen.

Kupfer verbrauchen unter anderem `pm_bronze_cannons` und `pm_bronze_smoothbores` (Waffen, früh), `pm_early_power_plant`, `pm_telephones`, `pm_electric_engines` und Fließband- bzw. Kühl-PMs. Ohne Vorkommen gibt es in Azeroth Dauermangel.

## Offen

- Kono: Wo liegt Kupfer in Azeroth? Lore-Orte (z. B. Kupfer-Adern in Dun Morogh, Loch Modan, Westfall, Durotar, Steinkrallengebirge) und Mengen. Vanilla-Maßstab: meist 6–30 je State.
- Eintragen in `map_data/state_regions/NN_va_*.txt` als `building_copper_mine = N` in `capped_resources` (Skill `va-karte`), danach Lint.
- Prüfen, ob Mod-Gebäude Kupfer brauchen sollten.

## Vanilla-Maßstab (1.15, erhoben 2026-11-06)

- 84 von 676 Land-States haben Kupfer (12,4 %), nach Provinzen 16,6 % der Landfläche. Nur sichtbare Vorkommen, kein unentdecktes Kupfer.
- Menge je State: min 4, Median 6, max 36, Summe 609. Zum Vergleich: Eisen 295 States/7.917, Blei 124/2.874, Schwefel 108/3.319, Gold 31/91. Kupfer ist also selten und meist klein, mit wenigen großen Lagern (Michigan 36, Katanga 30, Antofagasta 30, Sambia/Arizona/Tarapacá 18).
- Verteilung: in jedem Großraum etwas, Schwerpunkte Nordamerika (14 States, 130), Westeuropa (12, 74), Südamerika (6, 73), Ostasien (10, 62), Afrika südlich der Sahara (3, aber 54).
- Länder: nur etwa jedes vierte Land mit States hat zum Start Kupfer (110 von 449). Große Länder ohne Kupfer: Frankreich, Ägypten, Österreich, Brasilien, Dänemark, Argentinien, Niederlande; mit Kupfer u. a. Russland, China, USA, Osmanen, Großbritannien, Mexiko, Japan.
- Übertragen auf den Mod (711 Land-States): etwa 85–90 States, Summe ~600–650, meist 4–8, drei bis sechs große Lager 18–36.

## Vorschlag (Claude, 2026-11-06, von Kono freigegeben)

Leitidee Lore: Kupfer ist in WoW das Anfangserz, es liegt in den Start- und frühen Gebieten der alten Welt. Deshalb ballt es sich in EK und Kalimdor, und fast jede große Startnation (Stormwind, Ironforge/Gnomeregan, Undercity, Gilneas, Silvermoon, Orgrimmar, Thunder Bluff, Exodar, Darnassus über Dunkelküste) kommt an etwas heran. Northrend, Pandaria und Outland bekommen wenig, das passt zu später dazukommenden Gebieten (Platzhalter-Ressourcen `iron36,lead18` werden dort ohnehin neu gesetzt).

Budget gesamt ~86 States, ~660 (Vanilla-Anteil 12 %):

| Bereich | States | Summe |
|---|---|---|
| EK + Kalimdor (jetzt) | 62 | ~475 |
| Northrend (später, Heulender Fjord, Boreanische Tundra, Grizzlyhügel) | ~8 | ~50 |
| Pandaria (später, eher klein) | ~10 | ~70 |
| Uldum/Silithus (später, 2–3 große Wüstenlager wie Atacama) | ~3 | ~40 |
| Inseln (Kezan, Kul Tiras, Zandalar) | ~3–4 | ~25 |
| Outland | 0 | Fel-Eisen/Eternium statt Kupfer |

EK + Kalimdor im Einzelnen (Zonen per `strategic_regions` geprüft):

- **Groß (18–24):** GOL_BOLAR_QUARRY 24 (Dun Morogh), THELSAMAR 20 (Loch Modan), DEADMINES 20 (Westfall), RUINS_OF_SOUTHSHORE 18 (Hillsbrad, Azurelode), WINDSHEAR_HOLD 18 (Steinkrallen), DRYGULCH_RAVINE 18 (Durotar)
- **Mittel (8–12):** REDRIDGE_CANYONS 12; EMBERSTONE, SEPULCHER, WITHERBARK_VILLAGE, ANGOR_FORTRESS, BLOODHOOF_VILLAGE, RAZOR_HILL, SUN_ROCK_RETREAT je 10; ULDAMAN, WAILING_CAVERNS, KHARANOS, AGAMAND_MILLS, TOWER_OF_AZORA, JANSEN_STEAD, BLOOD_WATCH, RUINS_OF_AUBERDINE, AMETH_ARAN, STRAHNBRAD, BOULDER_GOR je 8
- **Klein (je 5):** SUNSTRIDER_ISLE, SUNCROWN_VILLAGE, DAWNSTAR_SPIRE, DEATHKNELL, BRILL, PYREWOOD_VILLAGE, TARRENS_MILL, HAMMERFALL, AERIE_PEAK, COLDRIDGE_VALLEY, GNOMEREGAN, SHIMMER_RIDGE, NORTH_GATE_OUTPOST, STONEWROUGHT_DAM, MENETHIL_KEEP, DUN_MODR, WHELGARS_RETREAT, DUSTWIND_DIG, NORTHSHIRE, GOLDSHIRE, SENTINEN_HILL, DAGGER_HILLS, RAGING_CHASM, LAKESHIRE, STONEWATCH, RAVEN_HILL, KURZENS_COMPOUND, AMMEN_VALE, AZURE_WATCH, ASTRANAAR, ORGRIMMAR, BILGEWATER_HARBOR, VALLEY_OF_TRIALS, CAMP_NARACHE, RATCHET, THORN_HILL, UNEARTHED_GROUNDS

Bewusst ohne Kupfer: Teldrassil, Östliche Pestländer, Brennende Steppe/Sengende Schlucht, Schattenhochland, Tanaris/Feralas/Desolace, Silithus/Uldum bis zur Überarbeitung.

## Notizen

- 2026-11-06: EK + Kalimdor eingetragen (62 States, Summe 473) als `building_copper_mine = N` am Ende von `capped_resources` in `23_`, `24_`, `26_`, `27_`, `28_va_*.txt`. Lint: 0 neue Fehler. Test T-094. Offen bleiben Northrend, Pandaria, Uldum/Silithus und Inseln (Budget oben), jeweils bei deren Überarbeitung.
- 2026-11-06: Aufgefallen beim Patch 1.15 (VA-063). Ob es außer Kupfer weitere neue Güter gibt, lässt sich ohne eine 1.13-Kopie nicht sicher sagen; die Güterliste hat jetzt 51 Einträge.
