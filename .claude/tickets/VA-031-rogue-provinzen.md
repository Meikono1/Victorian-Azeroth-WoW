# VA-031: Rogue-Provinzen im Süden entfernen oder wiederverwenden

- **Status:** offen
- **Typ:** technik
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Beim Kartenumbau überzählige Provinzen hat Kono in einen Haufen im südlichen Meer geschoben und dann einzeln im Ingame-Editor gelöscht (~20 s pro Provinz). Frage Kono: Kann Claude sie per Skript entfernen? Idee: Mit den Provinzen Zandalar, Kul Tiras und die Verlorenen Inseln füllen (→ VA-032).

## Analyse 2026-10-30

- Haufen bei x 4635–4862, y 3096–3164 (provinces.png 8192 × 3616), mitten im Meer (umgebende Farbe `x48FDFD`).
- **649 Provinzen liegen vollständig im Haufen**, im Schnitt ~20 Pixel groß (normal: Median 180):
  - 312 in `STATE_TEST` (alle Provinzen dieses States, → VA-018)
  - **337 in echten States von Nord-Kalimdor:** Shadowglen 82, Dolanaar 55, Gnarlpine Hold 30, Ammen Vale 25, Oracle Glade 24, Nestlewood Hills 21, Exodar 17, Darnassus 15, Azure Watch 14, Bristlelimb Village 14, Silvermyst Isle 12, Stillpine Hold 10, Odesyus' Landing 9, Kessel's Crossing 5, Nazzivian 4. Diese States haben damit einen abgetrennten Splitter im Meer.
  - 4 Provinzen von Nestlewood Hills liegen nur teilweise im Haufen (Rest an Land) → nur die Splitter-Pixel entfernen.
- Leere States, deren Hubs in den Haufen zeigen: z. B. `STATE_LARGO_OVERLOOK`, `STATE_BARADIN_HOLD` (0 Provinzen; Tol Barad, Schattenhochland).
- Außerdem 23 Farben in provinces.png ohne State (zusammen 1,37 Mio. Pixel, vermutlich Seen/Ödland); separat prüfen.

## Wichtig (Hinweis Kono 2026-10-30)

- Provinz aus provinces.png entfernt, aber irgendwo noch referenziert → **Absturz beim Spielstart**.
- Alle Referenzen gelöscht, Farbe liegt aber noch auf provinces.png → **weißer Fleck** auf der Karte, jedes Frame Fehler beim Drüberfahren mit der Maus.
- Also immer beides vollständig: Pixel **und** jede Referenz. Nach dem Skript erneut alle Dateien nach den IDs durchsuchen (Ergebnis muss 0 sein) und provinces.png auf die Farben prüfen (muss 0 sein).

Fundstellen der 649 Haufen-IDs im Repo (Suche 2026-10-30, `x`+Hex in .txt/.csv/.map/.yml/.json):

| Datei | Treffer |
|---|---|
| `map_data/province_terrains.txt` | 649 |
| `map_data/state_regions/23_va_north_kalimdor.txt` | 356 |
| `common/history/states/VA_kalimdor_states.txt` | 337 |
| `map_data/state_regions/26_va_north_eastern_kingdoms.txt` | 312 |
| `map_data/state_regions/27_va_center_eastern_kingdoms.txt` | 34 (vermutlich Hubs der leeren Tol-Barad-/Schattenhochland-States) |
| `common/history/states/VA_pandaria.txt` | 31 |
| `map_data/state_regions/31_va_east_pandaria.txt` | 6 |
| `common/strategic_regions/kalimdor_strategic_regions.txt` | 1 |

Pandaria verweist also auch auf Haufen-Provinzen (History 31, State Regions 6); vor dem Löschen klären, ob dort Hubs oder `owned_provinces` betroffen sind und was stattdessen hingehört.

## Lösung (Skript, Entwurf)

Mit numpy/Pillow, Laufzeit Sekunden:
1. Alle Haufen-Pixel in provinces.png mit der Meeresfarbe `x48FDFD` übermalen.
2. Die 649 Provinz-IDs aus allen `provinces = { … }`, `impassable`, `prime_land` in `map_data/state_regions/*.txt` entfernen; `STATE_TEST` ganz löschen (samt leerem Block in `common/history/buildings/26_north_eastern_kingdoms.txt`).
3. Einträge aus `map_data/province_terrains.txt`, `default.map` (`sea_starts`, `lakes`) und `adjacencies.csv` entfernen, falls vorhanden.
4. Hubs (`city`, `farm`, `mine`, `wood`, `port`), die auf gelöschte Provinzen zeigen, auf eine Provinz des eigenen States umsetzen bzw. leere States melden.
5. Prüfen: `va_check_states.py` für 23, 26, 27, dann Spielstart und `error.log`.

Offen: `nodes.dat` (11 MB, vom Editor erzeugt) ändert sich bei Kono-Bearbeitung mit. Ob das Spiel es nach einer Änderung an provinces.png neu baut, beim ersten Test prüfen; Sicherung vorher.

**Freigabe nötig:** provinces.png ist eine große Binärdatei (Projektregel: nur auf ausdrücklichen Wunsch). Kono entscheidet, ob Claude das Skript ausführt.

## Notizen
