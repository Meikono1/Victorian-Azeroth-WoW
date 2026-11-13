# VA-022: Amani und Deathholme – Journal Entries

- **Status:** wartet (Spieltest)
- **Typ:** content
- **Priorität:** mittel
- **Erstellt:** 2026-10-30

## Beschreibung

Amani: JE Amani-Reich wiederherstellen (Troll-States besitzen/unterwerfen) → Formable `AMANI_EMPIRE` (VA-017). Deathholme: JE Ausharren mit `timeout` ≈ 36.500 Tage, Ausbreitung von `va_dead_scar`, `on_timeout` Unterwerfung unter den Lichkönig, sofern ein Geißel-Land in Northrend existiert (derzeit nicht, Fallback nötig).

Konzept: [../konzepte/quel_thalas.md](../konzepte/quel_thalas.md)

## Notizen

- 2026-10-30: **Deathholme zurückgestellt**, bis Northrend ein Geißel-Land hat. Bis dahin nur der Amani-Teil.
- 2026-10-30: Amani-Reich: Träger Zul'jin (`AMANI_TRIBE`, Lore: Zul'Jarra-Klan). Dazu gehören `SHADOWPINE_TRIBE` und `MOSSFLAYER_TROLLS`, nicht Revantusk/Vilebranch/Witherbark.
- 2026-10-30: `AMANI_TRIBE` heißt „Zul'Jarra“, bis das Amani-Reich gegründet ist. Das JE sollte im Text auch von Zul'Jarra sprechen.
- 2026-10-30, Kono: Silvermoons Zul'Aman-Ziel ändert sich: zuerst **die Trolle nach Zul'Aman zurücktreiben und dort einsperren** (Eindämmung statt Zerstörung). Zul'Aman bekommt eine eigene Eventreihe mit Zul'jin. Kono liest dafür erst die Quests; Script wartet darauf.
- 2026-11-10: Erstentwurf Ablaufdiagramm [../ablauf/amani.md](../ablauf/amani.md): fünf geplante JEs (`je_amani_tribes`, `_loa`, `_siege`, `_empire`, `_vengeance`). Loa-Reihe, Schatzjäger und Horde-Bote sind Vorschläge von Claude, noch nicht von Kono bestätigt. Offene Fragen stehen dort unter „Offen“. Silvermoons `je_silvermoon_zul_aman` muss zusammen mit `je_amani_siege` auf „Eindämmung“ umgebaut werden.
- 2026-11-10, Kono: Plan als V1 abgenommen, Schatzjäger ausdrücklich gewollt. Horde-Teil zurückgestellt → VA-065. Silvermoon-Charaktere → VA-066.
- 2026-11-10: **V1 gescriptet.** JEs `je_amani_tribes/loa/siege/empire/vengeance` (`common/journal_entries/va_amani.txt`), Start in `va_global_quel_thalas.txt`. Schalter `va_amani_buttons.txt`, Balken `va_amani_bars.txt`, Effekte `va_amani_effects.txt`, Trigger `va_amani_triggers.txt`, Modifier `va_amani_modifiers.txt`, Schatzjäger über `on_monthly_pulse_country` (`va_on_actions_amani.txt`). Events `amani_events.1–5, 10–12`, `amani_loa_events.1–6`, `amani_treasure_events.1–3`. Loc `va_amani_l_english.yml`. Lint: 0 neue Fehler. Testfälle T-111 bis T-114.
- V1-Grenzen: `va_amani_besieged` gilt pauschal, solange `je_amani_siege` läuft (keine Abfrage von Silvermoons Eindämmung). Formable `AMANI_EMPIRE` fehlt noch (VA-017), `je_amani_empire` gibt nur Modifier und das Rache-JE. Zul'jin und Malacrass gibt es nicht als Charaktere.
- 2026-11-10, Kono: Ausbruch aus der Belagerung erst mit vollem Besitz von Sanctum of Sun (Anteile Shadowpine, Tranquillien, Nachtelfen-Außenposten), dazu Zul'Aman und Tor'Watha. Anspruch auf Sanctum kommt mit `je_amani_siege`. Die Shadowpine-Bedingung gilt nur noch für `je_amani_tribes`. Test T-114.
- 2026-11-12, Kono-Test T-113: Loa-Rituale funktionieren, Autorität −25 zu billig (Zul'Jarra ~1500) → −100 in `va_amani_loa_ritual`. Nachtest T-127.
- 2026-11-12, Kono-Test Sitzung 3: T-111, T-112, T-114, T-127 OK, T-115 (error.log) sauber bis auf harmlose Observe-Zeilen. T-113 nur bis zum zweiten Loa gespielt. Balance: Shadowpine-Eingliederung jetzt Tribut 50.000, Autorität −50, 36 Monate; Schatzjäger „Trespassers Executed“ Autorität 10 → 75. Nachtest T-131. Schatzjäger feuern wiederholt: 3 % je Monat unter Isolationismus mit Zul'Aman im Besitz, danach 3 Jahre Pause. Kono: Rache-Belohnung (nur Prestige) zu schwach, Formable fehlt → VA-017.
- 2026-11-13, Kono: `je_silvermoon_zul_aman` („Raze Zul'Aman“) bleibt für Version 3 so. Umbau auf Eindämmung zusammen mit `je_amani_siege` nach dem Release.
