# VA-065: Machtblöcke zerfallen (Horde, Allianz, …)

- **Status:** wartet (Spieltest)
- **Typ:** bug
- **Priorität:** hoch
- **Erstellt:** 2026-11-10

## Beschreibung

Silvermoon ist zum Spielstart in der Horde, verlässt sie aber im Spiel (Kono, 2026-11-10). Ursache aufschlüsseln (Machtblock-Grundsätze, Beziehungen, KI-Gewichte, Ideologie?) und Events bzw. Modifier anknüpfen, damit Silvermoon in der Horde bleibt oder ein Austritt bewusst und erzählt passiert.

Danach: Event „Bote der Horde“ der Amani-Reihe (`amani_events.30`, siehe [../ablauf/amani.md](../ablauf/amani.md)), das an Silvermoons Horde-Zugehörigkeit hängt.

## Notizen

- 2026-11-10: Aus VA-022 ausgelagert, hinten angestellt.
- Lore für den Amani-Teil: Zul'jin kämpfte mit der alten Horde (Doomhammer) gegen Quel'Thalas; der Rückzug der Horde und später die Aufnahme der Blutelfen in Thralls Horde gelten ihm als Verrat. Darkspear (Vol'jin) stehen loyal zur Horde, keine Bindung an die Amani.
- 2026-11-12: Kono: auch Orgrimmar selbst hat die Horde verlassen, andere Blöcke zerfallen ebenfalls (vgl. VA-036: Ironforge/Gnomeregan raus aus der Allianz). Ticket auf alle Machtblöcke erweitert. Analyse (Vanilla 1.15, `common/history/power_blocs/00_power_blocs.txt`, keine Fehler im error.log):
  1. **Machtkampf (wahrscheinlichste Ursache Horde):** Hat ein Mitglied ≥ 1,2× Prestige des Anführers, startet nach `NPowerBlocs` ein Machtkampf, nach 12 Monaten wechselt die Führung. Orgrimmar/Thunder Bluff/Darkspear starten mit `effect_starting_technology_tier_4_tech` + Peasant Levies, Silvermoon und Undercity mit Tier 2 + Professional Army; Silvermoon bekommt aus seinen JEs bis zu +135 Prestige (`va_silvermoon_modifiers.txt`, `va_quel_thalas_modifiers.txt`). Wird Silvermoon Anführer, darf Orgrimmar als normales Mitglied austreten (`can_leave`: Leverage-Vorteil ≤ 30).
  2. **Anführer nicht mehr führungsfähig:** Anführer muss Great/Major Power sein (Rang über Prestige relativ zum Durchschnitt und zum stärksten Land). Fällt er ab, wird der Block aufgelöst („no longer being fit to lead“). Bei Tier-4-Anführern (Orgrimmar, Illidari, Cenarion Circle) naheliegend.
  3. **Leverage zu niedrig:** Alle Identitäten erlauben Austritt bei Leverage-Vorteil ≤ 30. Leverage wird in der History nicht gesetzt; schwache Anführer erzeugen kaum welche → Mitglieder können jederzeit gehen.
  4. **Kohäsion:** Basis 30, −2 je Mitglied; Ideologische Union (Allianz) zusätzlich Strafe für größten Unterschied der Regierungsform (EK-Länder mit eigenen Gesetzen vs. Kalimdor-Default `politics_traditional`), Religiöse Identität (Cenarion) hängt am Devout-Clout.
  - Offen: Ingame bestätigen (Benachrichtigungstext, Rang von Orgrimmar, Kohäsions-Tooltip), dann Gegenmaßnahmen wählen.
- 2026-11-12 (Kono, Spieltest): Machtkampf ist es **nicht** – alle treten in den ersten 3 Monaten aus. Orgrimmar ist zum Start nur Minor Power (darf nicht führen), Leverage um −900. Allianz bleibt mit Stormwind als Anführer bestehen, aber alle Mitglieder sind raus; Ironforge/Gnomeregan haben Leverage 0. Ursachen also Rang (Horde) + Leverage (alle Blöcke).
- Lösungsvorschlag (Hebel aus Script-Doku 1.15 und Vanilla geprüft):
  1. **Start-Leverage:** in `00_power_blocs.txt` nach `create_power_bloc` je Mitglied `power_bloc = { add_leverage = { target = c:X value = N } }` (Scope power_bloc, Vorbild `05_austria_buttons.txt`). Wirkt sofort, driftet aber zum Zielwert zurück (2 %/Woche) → nur Überbrückung.
  2. **Dauerhafte Leverage über Start-Verträge:** `common/history/treaties/` (Vorbild Vanilla `00_historical_treaties.txt`, Holy Alliance) Anführer ↔ Mitglied mit `alliance` (+400 `country_treaty_leverage_generation_add`) oder `defensive_pact` (+300), `binding_period` z. B. 10–20 Jahre. Passt zur Lore (Horde/Allianz als Bündnis), zieht Mitglieder aber in Kriege.
  3. **Rang Orgrimmar:** Start-Modifier (z. B. `va_warchief_of_the_horde`) mit `country_prestige_add`, Höhe nach Ingame-Werten (Prestige Orgrimmar, Schwelle Major Power). Alternativ/zusätzlich `country_leverage_generation_add` für die Anführer.
  - Offen: Kono wählt Kombination; Prestige-Zahlen aus dem Spiel nötig.
- 2026-11-12 (Kono): alle drei umsetzen, nur Horde und Allianz; Pakte als Verteidigungspakte. Orgrimmar startet mit 40 Prestige, Major Power ab 55 → +30.
- 2026-11-12 umgesetzt (Test T-129):
  - `common/history/power_blocs/00_power_blocs.txt`: je Mitglied von Horde und Allianz `add_leverage` 500.
  - `common/history/treaties/00_historical_treaties.txt` (war leer): 8 Verteidigungspakte Anführer ↔ Mitglied, in Kraft 617.1.1, 20 Jahre bindend.
  - `common/static_modifiers/va_power_bloc_modifiers.txt` (neu): `va_warchief_of_the_horde` (+30 Prestige), gesetzt in `va_kalimdor_countries.txt` bei Orgrimmar.
  - Loc: `localization/replace/english/va_power_blocs_l_english.yml` (neu).
  - Ungeprüft: ob Pakte trotz fehlender Tech `international_relations` (Kalimdor Tier 4) aus der History entstehen; Bedingung „Beziehungen herzlich“ gilt nur fürs Abschließen. Andere Blöcke (Illidari, Scharlachroter Kreuzzug, Cenarion) unverändert.
