# Konzept: Quel'Thalas (Nord-Nord-EK)

Stand: 2026-10-30, Idee von Christian. Umsetzung in VA-019 bis VA-022.

## Akteure

| Land | Tag | Rolle |
|---|---|---|
| Silvermoon | `SILVERMOON` | Hauptspieler. Vertreibt Deathholme, zerstört Zul'Aman, heilt die Wretched und die Todesschneise, löst das Mana-Problem |
| Wretched | `WRETCHED_BLOODELFES` | Mana-süchtig und krank. Arbeitet mit Silvermoon und geht per Eventreihe in Silvermoon auf |
| Amani | `AMANI_TRIBE` | Will das Amani-Reich wieder aufbauen |
| Deathholme | `DEATHHOLME` | Hält aus, verdirbt das Land und unterwirft sich nach ~100 Jahren dem Lichkönig (nur wenn Northrend steht) |
| Murlocs, Nachtelfen | `GRIMSCALE_MURLOCS`, `DARNASSUS_OUTPOST_EK` … | vorerst irrelevant |

Randfiguren, die in die Ziele hineinspielen: `TRANQUILLIEN` (Silvermoons Außenposten), Troll-Stämme `REVANTUSK_TROLLS`, `VILEBRANCH_TROLLS`, `WHITERBARK_TROLLS`, `SHADOWPINE_TRIBE`, `MOSSFLAYER_TROLLS` (Amani-Ziel).

## Gemeinsame Bausteine

- **Mana** als Länder-Variable `va_mana` (0–100), angezeigt als Scripted Progress Bar. Vorbild: `common/scripted_progress_bars/00_je_progress_bars.txt`. Mangel → Malus-Modifier (Unruhe, weniger Durchsatz), Überschuss → Bonus.
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
- JE „Das Amani-Reich wiederherstellen“: Ziel-States der Troll-Stämme besitzen bzw. unterwerfen. Abschluss → Formable `AMANI_EMPIRE` (VA-017). Vorbilder: `00_italian_unification.txt`, `05_serbia.txt`.
- Gegenspieler zu Silvermoons Ziel 2.

### Deathholme
- JE „Ausharren“ mit `timeout` ≈ 100 Jahre (36.500 Tage). Vorbild: `00_sick_man.txt` (`timeout`/`on_timeout`).
- Während der Laufzeit breitet sich `va_dead_scar` in Nachbar-States aus (gegen Silvermoons Heilung).
- `on_timeout`: Land endgültig verdorben. Unterwerfung unter den Lichkönig nur, wenn ein Geißel-Land in Northrend existiert. **Northrend hat derzeit kein einziges Land** → Abhängigkeit, bis dahin Fallback (z. B. nur Verderbnis, keine Unterwerfung).

## Offene Fragen

- Quel'Danas: Besitzer (bisher Platzhalter `EASTERNKINGDOMS`). Für den Sunwell als Mana-Lösung wäre Silvermoon naheliegend.
- Mana abstrakt (Variable + Balken) oder als echtes Gut/Gebäude? Empfehlung: abstrakt, weil ein neues Gut Markt, PMs und Gebäude berührt.
- Geißel/Lichkönig in Northrend: eigenes Ticket, sobald Northrend dran ist.
