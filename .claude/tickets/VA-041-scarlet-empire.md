# VA-041: Scarlet Crusade → Scarlet Empire

- **Status:** offen
- **Typ:** content
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Kono 2026-10-30: Die Scarlet Crusade soll sich zu einem Scarlet Empire entwickeln können (JE, Events, Formable). Gehört zur ersten Content-Welle in EK, zusammen mit Silvermoon wiederherstellen (VA-020) und Zul'Aman/Amani-Reich gründen (VA-022).

## Offene Fragen an Kono

- Träger: `SCARLET_CRUSADERS_WHITEMANE` (6 States), `SCARLET_CRUSADERS_ONSLAUGHT` (3 States, Northrend?) oder beide?
- Weg: Formable (Bedingung States/Kultur `lordorean`) oder JE mit Eroberungszielen (Tyr's Hand, Hearthglen, Stratholme …)?
- Verhältnis zu `LORDAERON` (VA-017, „aus Scarlet/Argent/Andorhal“): Konkurrenz oder Vorstufe?
- Verhältnis zum Startkonflikt mit der Ebon Blade (VA-035).
- Gesetze, Ideologie, Staatsreligion (Heiliges Licht, Theokratie?).

## Notizen

### 2026-10-30 – Lore und Ablauf (Kono)

- Die Scarlet Crusade ist **zersplittert**. Whitemane und Renault Mograine führen `SCARLET_CRUSADERS_WHITEMANE` (Charaktere in `common/history/characters/va_eastern_kingdom.txt:23`). Daneben gibt es `SCARLET_CRUSADERS_ONSLAUGHT` (New Avalon, Tyr's Hand, Havenshire), bisher ohne Charaktere.
- **Kein einzelnes JE, sondern eine Reihe von Journal Entries.** Sie betreffen auch die Forsaken (`UNDERCITY`) und die Argent Crusade (`ARGENT_CRUSADERS`).
- Bausteine:
  1. **Unterstützung gegen die Ebon Blade:** Scarlet liefert Waffen und Mittel an die Gegner der Ebon Blade (verknüpft mit VA-035).
  2. **Brücke Nightmare Vale – Solliden schlagen** und damit Deathknell (Forsaken-Startgebiet) abschneiden. Lage: `STATE_SOLLIDEN` gehört Whitemane, `STATE_NIGHTMARE_VALE` teilen sich Undercity und Whitemane, `STATE_DEATHKNELL` gehört Undercity.
  3. **Sympathisanten in Hearthglen wieder einbinden:** `STATE_HEARTHGLEN` gehört der Argent Crusade, dort lebt eine Scarlet-treue Gruppe.
  4. **Dämonenlord, der die Crusade kontrolliert**, muss sich über JEs lösen lassen (aufdecken, vertreiben). Lore: vermutlich Balnazzar als Großkreuzzügler Dathrohan. Im Mod gibt es dafür noch keinen Charakter.
- Am Ende steht das **Scarlet Empire** (Formable oder Ergebnis-Event).

### 2026-10-30 – Antworten Kono

1. **Dämonenlord: Balnazzar im Scarlet Monastery** (`STATE_SCARLET_MONASTERY`, Whitemane). Braucht eine eigene Charaktervorlage.
2. **Waffenlieferungen = Startkonflikt** (VA-035). Whitemane und Onslaught sind schon im Machtblock `SCARLET_CRUSADE` (`common/history/power_blocs/00_power_blocs.txt:98`, Militärbündnis, `principle_aggressive_coordination_2`). Offen: Warum verlassen manche Länder ihre Machtblöcke? Gleiches Muster wie Ironforge/Gnomeregan in VA-036, also gemeinsam untersuchen.
3. **Brücke = Provinzen `xD31E1A` und `xCA3319`** und ein paar andere (welche, sagt Kono noch). Beide liegen in `STATE_NIGHTMARE_VALE` im Teil von `UNDERCITY`; Whitemane hält den Rest des States. Eroberung per JE oder Kampf, Optionen siehe unten.
4. **Hearthglen:** Die Argent Crusade kümmert sich um die östlichen Pestländer, Hearthglen um Andorhal. Schafft die Argent Crusade es nicht, oder gewinnt die Ebon Blade gegen die Crusaders, spaltet sich Hearthglen ab und kehrt zur Scarlet Crusade zurück. Alternativ durch einen Aufstand. Dafür braucht Hearthglen passende Bevölkerung. Bisher: 860 Tsd. `lordorean`/`brotherhood_light`, keine `scarlet_crusade`-Pops (die Religion gibt es, Whitemane-Pops haben sie).
5. **Der Weg zum Empire führt über den Krieg mit den Forsaken und die Eroberung Lordaerons**, nicht über die Wiedervereinigung mit Onslaught.
6. **Dämonenlord und Empire laufen parallel**, als getrennte Journal Entries.

### JE-Reihe (Entwurf)

| JE | Land | Inhalt | Ende |
|---|---|---|---|
| `je_scarlet_bridge` | Whitemane | Brücke Nightmare Vale – Solliden nehmen, Deathknell abschneiden | Provinzen in Scarlet-Hand |
| `je_scarlet_balnazzar` | Whitemane | Balnazzar im Monastery entlarven und vertreiben | Charakter entfernt, Modifikator weg |
| `je_scarlet_empire` | Whitemane | Krieg gegen die Forsaken, Lordaeron erobern (Brill, Undercity, Tirisfal …) | Formable/Event Scarlet Empire |
| `je_hearthglen_loyalty` | Argent Crusade (Hearthglen) | Andorhal halten; scheitert die Argent Crusade oder siegt die Ebon Blade → Abspaltung | Rückkehr zu Scarlet oder Ruhe |

### Optionen für die Brücke (Entscheidung Kono)

Vic3 erobert normalerweise ganze State-Teile, nicht einzelne Provinzen. Möglichkeiten:

- **A – JE mit Provinz-Übertragung:** Das JE setzt Ziele (Armee in Solliden, Kriegsunterstützung, Geld/Waffen). Beim Abschluss überträgt ein Event die Provinzen per `set_owner_of_provinces = { country = … provinces = { xD31E1A xCA3319 … } }` (Scope `state_region`). Vorbild: Vanilla `events/zanzibar_events.txt:438`. Kein Krieg nötig, Undercity kann per Event-Option reagieren (abtreten, Gegenangriff).
- **B – Krieg um den ganzen Undercity-Teil:** Kriegsziel `conquer_state` auf Undercitys Teil von Nightmare Vale. Einfach, aber Whitemane bekommt alle Undercity-Provinzen dort, nicht nur die Brücke.
- **C – Eigener Brücken-State:** Kono zeichnet die Brücke als eigenen kleinen State. Dann geht B genau für die Brücke, und die KI versteht das Ziel. Kostet Kartenarbeit.
- **D – Kombination A + Kampf:** Diplomatic Play mit eigenem Kriegsziel, bei Sieg überträgt ein Event nur die Brücken-Provinzen (`on_war_end`/Event nach Friedensschluss). Am flexibelsten, aber am meisten Script.

**Brücken-Provinzen vollständig (Kono 2026-10-30):** `xD31E1A xCA3319 x8906CC xF769EE xE4D8D8`. Alle fünf liegen in `STATE_NIGHTMARE_VALE` und gehören Undercity, das dort 18 Provinzen hält. Keine ist `impassable`.

~~Entscheidung Kono 2026-10-30: Das JE startet ein Diplomatic Play gegen Undercity.~~ **Überholt, siehe unten:** Ein Diplomatic Play führt direkt in den Krieg.

### 2026-10-30 – Überarbeitung (Kono)

**Brücke hängt an Gilneas, kein Diplomatic Play:**
- Auslöser: **Undercity erklärt `GILNEAS` den Krieg** bzw. ein Diplomatic Play Undercity gegen Gilneas beginnt. Dann sind die Forsaken gebunden, und Whitemane kann die fünf Brücken-Provinzen per JE einnehmen (`set_owner_of_provinces`, kein eigener Krieg).
- Danach entscheiden die Forsaken per Event: **(a)** Diplomatic Play gegen Whitemane, um den ganzen State Nightmare Vale zu holen, oder **(b)** Rückzug, die Provinzen bleiben Scarlet.
- Technik prüfen: Event, wenn ein Diplomatic Play/Krieg Undercity gegen Gilneas startet (`on_diplomatic_play_started`/`on_war_started` o. ä. in `docs\on_actions.log`, sonst JE-Bedingung `is_at_war_with`/`has_diplomatic_play`).

**Balnazzar und Stratholme über Kolonisierung:**
- Balnazzar ist als Saidan Dathrohan unterwegs, um Stratholme einzunehmen. `STATE_STRATHOLME` gehört `PLAGUELAND_UNDEAD` (`country_type = decentralized`), lässt sich also kolonisieren.
- Whitemane kolonisiert Stratholme. **Waffenlieferungen beschleunigen die Kolonisierung** (Modifier auf das Koloniewachstum, Namen in `docs\modifiers.log` prüfen).
- **Hält Balnazzar 80 % von Stratholme, entsteht die Crimson League** (neues Land, Tag z. B. `CRIMSON_LEAGUE`). Sie besiedelt selbstständig weiter.
- Während der Besiedelung schickt er dem Spieler immer wieder Ratschläge und Gegenstände, die die Scarlet Crusade verderben (Event-Kette mit verlockenden Optionen und versteckten Folgen). Der Spieler merkt das und muss entscheiden, ob er selbst besiedelt, ohne dass die Crimson League entsteht. **Wird noch ausgearbeitet.**
- Die 80 % sind als Anteil der Provinzen bzw. des Koloniefortschritts gedacht. Wie man das misst, an Vanilla prüfen (Koloniefortschritt, Provinzanzahl im State-Teil).

**Lordaeron (Ziel `je_scarlet_empire`):**
- Alle States der Strategic Region `region_tirisfal_glades`: Scarlet Monastery, Whispering Gardens, The Bulwark, Brill, Agamand Mills, Undercity, Nightmare Vale, Solliden, Deathknell
- dazu `STATE_ANDORHAL`, `STATE_HEARTHGLEN`, `STATE_SORROW_HILL`, `STATE_FORSAKEN_HIGH_COMMAND`, `STATE_FORSAKEN_REAR_GUARD`
- Die State-Namen werden noch angepasst und ändern sich zum Teil bei der Übernahme (z. B. Forsaken-Namen → Scarlet-Namen). Technik prüfen: State-Namen per Loc mit Bedingung, oder Umbenennung per Effekt.

Empfehlung Claude (überholt): **A** für den Start (schnell, patchsicher, kein Kartenumbau), später **D**, wenn der Krieg mit den Forsaken (Empire-JE) ohnehin läuft.

### Offene Fragen an Kono (Stand 2026-10-30, ältere Fragen)

- Welcher Dämonenlord, und wo sitzt er? Bei Whitemane, bei Onslaught oder in Stratholme (`PLAGUELAND_UNDEAD`)? Als Charakter mit eigener Vorlage?
- Waffenlieferungen an wen: an die Argent Crusade, an die Forsaken oder als reine Kriegsunterstützung in VA-035?
- „Brücke schlagen“: Eroberung von Nightmare Vale bzw. Brill als JE-Ziel oder eine Art Bauprojekt (Gebäude, Infrastruktur)?
- Hearthglen: Sympathisanten als Bewegung oder Pop-Gruppe, Einbindung über Annexion, Abspaltung oder Aufstand?
- Gehört Onslaught zur Reihe (Wiedervereinigung beider Teile als Schritt zum Empire)?
- Reihenfolge: zuerst der Dämonenlord, dann das Empire, oder umgekehrt?
