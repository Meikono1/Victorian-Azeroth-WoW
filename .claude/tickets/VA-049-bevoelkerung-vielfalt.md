# VA-049: Bevölkerung weltweit zu eintönig

- **Status:** in Arbeit
- **Typ:** content
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Kono (2026-10-30): Die Pops auf der Welt sind zu monoton (je State meist eine Kultur). Für VA-048 (Untote eingliedern, Banshees nach Undercity) und allgemein braucht es gemischte Bevölkerungen: Minderheiten, Untote in Lebenden-States, Flüchtlinge usw. Region für Region, Anfang Quel'Thalas und Nord-EK.

## Notizen
- 2026-11-10: **Quel'Thalas gemischt** (`common/history/pops/va_north_eastern_kingdoms.txt`, Block mit Kopfkommentar): 39 → 68 Pops, Summen je State unverändert (außer Quel'Danas, VA-024). Silvermoon City: Quel'dorei, Goblins, Dalaraner, Verlassene, Orgrimmari, Darkspear (jungle_troll). Häfen West Sanctum/Sunsail: Goblins. Ghostlands: Banshees + Zombies; Tranquillien: Verlassene. Amani/Shadowpine: Dire Trolls. Lint 0 neue Fehler. Test T-116. Weitere Regionen offen.
- 2026-11-12, Kono-Test: Zahlen zu glatt, Goblins im Elfen-Startgebiet unklar, Banshees in den Ghostlands sollen stärker sein (Zombies = tote Menschen, in Deathholme am stärksten), Elfen als Sklaven der Trolle, Nachtelfen-Außenposten zu groß. Umgesetzt: alle Quel'Thalas-Zahlen krumm; Goblins nur noch 16.420 in Silvermoon City (Händler), West Sanctum/Sunsail ohne; Ghostlands rund 75–80 % Banshees; Sklaven-Elfen in Tor'Watha, Suncrown, Dawnstar, Sanctum und Zul'Aman (dort auch Quel'dorei, weniger Troll-Sklaven); Außenposten 130.000 → 34.860; Tranquillien 460.000 → 355.380. Neues Skript im Pop-Block-Stil (Scratchpad). Vergleich Vanilla/Mod: `.claude/regionen/bevoelkerung_vanilla_vs_mod.md`. Test T-121.
- 2026-11-12, Kono: Troll-Sklaven in Zul'Aman komplett raus (912.380), dafür Opium 3, Baumwolle 2 → 4, Holz 2 → 5 (500.000 Arbeitslose, viele Sklaven). Test T-122.
