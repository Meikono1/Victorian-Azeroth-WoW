# Konzept: Quel'Thalas (Nord-Nord-EK)

Stand: 2026-10-30, Idee von Kono. Umsetzung in VA-019 bis VA-022.

## Akteure

| Land | Tag | Rolle |
|---|---|---|
| Silvermoon | `SILVERMOON` | Hauptspieler. Vertreibt Deathholme, zerstört Zul'Aman, heilt die Wretched und die Todesschneise, löst das Mana-Problem |
| Wretched | `WRETCHED_BLOODELFES` | Mana-süchtig und krank. Arbeitet mit Silvermoon und geht per Eventreihe in Silvermoon auf |
| Zul'Jarra (Amani) | `AMANI_TRIBE` | Zul'jins Klan, will das Amani-Reich wieder aufbauen. Heißt Zul'Jarra, bis er als `AMANI_EMPIRE` zum Königreich wird |
| Deathholme | `DEATHHOLME` | Hält aus, verdirbt das Land und unterwirft sich nach ~100 Jahren dem Lichkönig (nur wenn Northrend steht) |
| Murlocs, Nachtelfen | `GRIMSCALE_MURLOCS`, `DARNASSUS_OUTPOST_EK` … | vorerst irrelevant |

Randfiguren, die in die Ziele hineinspielen: `TRANQUILLIEN` (Silvermoons Außenposten), Troll-Stämme `SHADOWPINE_TRIBE`, `MOSSFLAYER_TROLLS` (Amani-Ziel).

## Gemeinsame Bausteine

- **Mana** als Handelsgut `mana` (Entscheidung siehe unten). Nachfrage über die Pop-Bedürfnisse und eine Obsession der Kulturen `sin_dorei`/`quel_dorei` (Vanilla: `obsessions = {…}` in Kulturen, `obsession_chance` im Gut). Mangel zeigt sich über Preis und Versorgung. JEs fragen Versorgung bzw. Produktion ab.
- **Todesschneise** (Dead Scar) als State-Modifier `va_dead_scar` auf festen States (z. B. `STATE_RUINS_OF_SILVERMOON`, `STATE_DEATHHOLME`, Ghostlands-States). Vorbild für sich ausbreitende/heilende State-Modifier: `01_silkworm_diseases.txt`, `00_plague.txt`.
- **Wretched-Sucht** als Pop-/Länder-Modifier. Vorbild: `00_opium.txt`.

## Ziele und Mechanik

### Silvermoon
1. **Deathholme vertreiben**: JE, erfüllt, wenn `c:DEATHHOLME` nicht mehr existiert oder Silvermoon alle Ghostlands-States besitzt. Vorbild: `01_natural_borders_of_france.txt` (Besitz bestimmter States).
2. **Zul'Aman zerstören**: JE, Ziel `STATE_ZUL_AMAN` und `STATE_TOR_WATHA` in Silvermoons Besitz, Abschluss zerschlägt Amani-Ansprüche (verhindert deren Formable).
3. **Die Wretched heilen**: Eventkette zusammen mit dem Wretched-JE (siehe dort).
4. **Die Todesschneise heilen**: JE mit Fortschrittsbalken; Fortschritt durch Investition (Geld/Mana), entfernt `va_dead_scar` State für State. Vorbild: `00_land_reclamation.txt`.
5. **Mana-Problem**: Dauer-JE. Mana sinkt monatlich, steigt durch Entscheidungen/Gebäude; Lösung erst durch ein großes Ziel (z. B. Sunwell-Projekt auf Quel'Danas, falls Silvermoon es besitzt).

### Wretched
- JE „Mana-Hunger“: Sucht-Modifier, Mana-Verfall schneller als bei Silvermoon.
- Zusammenarbeit: Events bieten Kooperation mit Silvermoon an (Mana-Lieferungen, Pakt). Annahme senkt Sucht schrittweise.
- **Vereinigung**: Eventreihe, an deren Ende Silvermoon die Wretched annektiert (`annex_with_incorporation`). Vorbild: `00_romania.txt` (Union zweier Länder).

### Amani
- JE „Das Amani-Reich wiederherstellen“ (Zul'jin): States von Shadowpine und Mossflayer besitzen bzw. unterwerfen. Abschluss → Formable `AMANI_EMPIRE` (VA-017). Vorbilder: `00_italian_unification.txt`, `05_serbia.txt`.
- Gegenspieler zu Silvermoons Ziel 2.

### Deathholme (zurückgestellt, bis Northrend steht)
- JE „Ausharren“ mit `timeout` ≈ 100 Jahre (36.500 Tage). Vorbild: `00_sick_man.txt` (`timeout`/`on_timeout`).
- Während der Laufzeit breitet sich `va_dead_scar` in Nachbar-States aus (gegen Silvermoons Heilung).
- `on_timeout`: Land endgültig verdorben. Unterwerfung unter den Lichkönig nur, wenn ein Geißel-Land in Northrend existiert. **Northrend hat derzeit kein einziges Land** → Abhängigkeit, bis dahin Fallback (z. B. nur Verderbnis, keine Unterwerfung).

## Entscheidungen (Kono, 2026-10-30)

- **Quel'Danas** gehört zum Start Silvermoon (umgesetzt). Später eine Eventreihe: Kael'thas flieht dorthin und versucht, Kil'jaeden zu beschwören. Daraus entstehen die Shadowsword (Schattenschwerter) und eine kleine Gruppe der Zerschmetterten Sonne (Shattered Sun). Kommt später, siehe Content-Ideen im Ablaufplan.
- **Mana ist ein echtes Handelsgut** (`common/goods/va_goods.txt`), nicht nur eine Variable. Der Abschnitt „Gemeinsame Bausteine“ oben gilt für Mana entsprechend (Mangel = Marktpreis/Versorgung statt Variable). Details in VA-019.
- **Deathholme ist zurückgestellt**, bis Northrend ein Geißel-Land hat.
- **Amani:** Träger des Wiederaufbaus ist Zul'jin (`AMANI_TRIBE`, Lore: Zul'Jarra-Klan). Zum Reich gehören zusätzlich `SHADOWPINE_TRIBE` und `MOSSFLAYER_TROLLS`. Revantusk, Vilebranch und Witherbark gehören **nicht** dazu.
- **Zul'Jarra:** `AMANI_TRIBE` heißt im Spiel „Zul'Jarra“, solange es kein Königreich ist. Erst das Formable `AMANI_EMPIRE` trägt den Namen Amani-Reich.
- **Mana stammt aus Leylinien:** eine abbaubare Ressource wie Kohle oder Eisen. Leylinien werden als `capped_resources` in den States verteilt (Schwerpunkt Quel'Thalas). Ein Abbaugebäude (Arbeitsname `building_leyline_tap`) fördert das Gut `mana`. Später dient Mana als Vorprodukt für magische Gegenstände und als Antrieb für Produktionen (wie Kohle bzw. Strom in Vanilla-PMs).
- **Mana-Verbrauch** (2026-10-30): später über Produktionsmethoden und über die Bevölkerung von Blut- und Hochelfen (`sin_dorei`, `quel_dorei`). Leylinien-Verteilung in Quel'Thalas ist bestätigt (Werte in VA-019).
