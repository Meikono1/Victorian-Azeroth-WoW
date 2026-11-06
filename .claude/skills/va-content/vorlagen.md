# Vorlagen im Hausstil

Destilliert aus getesteten eigenen Dateien (`events/va_silvermoon_events.txt`, `common/journal_entries/VA_silvermoon.txt`, `va_silvermoon_corridor_*.txt`, `va_silvermoon_modifiers.txt`). `<…>` ersetzen. Kommentare deutsch, Loc-Texte englisch.

## Event (`events/va_<thema>_events.txt`)

```
# Events zu <Thema> (VA-NNN). Vorbild: Vanilla land_reclamation.1 (events/land_reclamation.txt).
namespace = <thema>_events

# <Kurzbeschreibung>, ausgelöst von <JE/Effekt>
<thema>_events.1 = {
	type = country_event

	title = <thema>_events.1.t
	desc = <thema>_events.1.d
	flavor = <thema>_events.1.f

	event_image = {
		video = "<video>" # TODO: eigenes Bild (VA-027)
	}

	on_created_soundeffect = "event:/SFX/UI/Alerts/event_appear"

	icon = "gfx/interface/icons/event_icons/<icon>.dds" # TODO: eigenes Icon (VA-027)

	duration = 3

	trigger = {
		# ausgelöst von <…>
	}

	option = {
		name = <thema>_events.1.a
		default_option = yes
		# Effekte, die schon im Auslöser passieren, nur als show_as_tooltip = { … }
	}
}
```

Desc je Bedingung: `desc = { first_valid = { triggered_desc = { desc = <key>_undead trigger = { … } } triggered_desc = { desc = <key> trigger = { always = yes } } } }` (so in `dead_scar_events.1`).

## Journal Entry: Ziel mit Timeout (`common/journal_entries/VA_<thema>.txt`)

```
# <Zweck> (VA-NNN). Vorbild: Vanilla je_sick_man_syria (journal_entries/00_sick_man.txt).
# Ablauf: .claude/ablauf/<land>.md.

je_<thema>_<ziel> = {
	icon = "gfx/interface/icons/event_icons/<icon>.dds" # TODO: eigenes Icon (VA-027)

	group = je_group_historical_content   # oder je_group_internal_affairs

	immediate = {
		# Ansprüche, Variablen setzen
	}

	possible = { … }       # Sperren hier auch eintragen, Vic3 aktiviert JEs selbst

	# seit 1.15: outcome statt complete/fail/invalid/timeout (Vanilla journal_entries.md)
	outcome = {
		header = je_standard_completion_header
		effect_header = je_standard_on_completion_header
		color = "gold_positive"
		conclusion_desc = je_standard_completion_conclusion_desc
		trigger = { … }
		effect = {
			add_modifier = { name = va_<thema>_<belohnung> years = 10 }
			trigger_event = { id = <thema>_events.1 popup = yes }
		}
	}

	# Scheitern sichtbar: header/effect_header je_standard_failure_header/je_standard_on_failure_header,
	# color = "blue_negative", conclusion_desc = je_standard_failure_conclusion_desc
	# Still ungültig (früher invalid/on_invalid):
	outcome = {
		flags = { hidden invalid_outcome }
		conclusion_desc = je_standard_failure_conclusion_desc
		trigger = { … }
		effect = { … }
	}

	timeout = 5475 # 15 Jahre; braucht dann genau ein timeout-outcome
	outcome = {
		header = JOURNAL_ENTRY_TIMEOUT
		effect_header = JOURNAL_ENTRY_ON_TIMEOUT
		flags = { timeout }
		conclusion_desc = JOURNAL_ENTRY_TIMEOUT_CONCLUSION_DESC
		effect = { … }
	}

	transferable = no
	weight = 100

	should_be_pinned_by_default_uninvolved_or_context = yes
}
```

## Journal Entry mit Balken und Schalter

Zusätzlich zur Ziel-Vorlage:

```
	scripted_progress_bar = va_<thema>_bar
	scripted_button = va_<thema>_start_button

	on_monthly_pulse = {
		effect = { va_<thema>_pulse_effect = yes }   # Balken voll → Effekt prüft und löst aus
	}

	status_desc = {
		first_valid = {
			triggered_desc = { desc = je_<thema>_status_stalled trigger = { … } }
			triggered_desc = { desc = je_<thema>_status_running trigger = { … } }
			triggered_desc = { desc = je_<thema>_status_idle trigger = { always = yes } }
		}
	}
```

## Scripted Button (`common/scripted_buttons/va_<thema>_buttons.txt`)

```
# <Zweck> (VA-NNN).
# Vorbild: Vanilla je_haitian_debt_payment_button (scripted_buttons/00_hispaniola_buttons.txt).

va_<thema>_start_button = {
	name = "va_<thema>_start_button"
	desc = "va_<thema>_start_button_desc"

	visible = { … }

	possible = {
		custom_tooltip = { text = va_<thema>_not_at_war_tt is_at_war = no }
		custom_tooltip = { text = va_<thema>_not_bankrupt_tt NOT = { has_modifier = declared_bankruptcy } }
	}

	ai_chance = {
		value = 0
		if = { limit = { scaled_debt <= 0 } add = 50 }
	}

	effect = {
		add_treasury = -100000
		add_modifier = { name = va_<thema>_running }
	}
}
```

## Progress Bar (`common/scripted_progress_bars/va_<thema>_bars.txt`)

```
# <Zweck> (VA-NNN). Vorbild: Vanilla 00_greece_progress_bars.txt (Scope in monthly_progress = Land).

va_<thema>_bar = {
	name = "va_<thema>_bar"
	desc = "va_<thema>_bar_desc"

	default_green = yes

	monthly_progress = {
		if = {
			limit = { <läuft> }
			add = { desc = "va_<thema>_bar_progress_desc" value = 1 }
		}
		else_if = {
			limit = { <läuft, aber blockiert> }
			add = { desc = "va_<thema>_bar_stalled_desc" value = 0 }
		}
	}

	start_value = 0
	min_value = 0
	max_value = 18
}
```

## Decision (`common/decisions/va_<thema>_decisions.txt`)

Vanilla-Doku: `common/decisions/000_decisions_help.txt`. Scope immer das Land.

```
# <Zweck> (VA-NNN). Vorbild: Vanilla KOR_declare_korean_empire (decisions/korea_decisions.txt).

va_<thema>_decision = {
	is_shown = {
		c:<TAG> ?= THIS
		NOT = { has_variable = va_<thema>_taken }
	}

	possible = {
		# Bedingungen, bei Bedarf in custom_tooltip
	}

	when_taken = {
		set_variable = va_<thema>_taken
		trigger_event = { id = <thema>_events.1 popup = yes }
	}

	ai_chance = {
		value = 10
	}
}
```

## Static Modifier (`common/static_modifiers/va_<thema>_modifiers.txt`)

```
# <Zweck> (VA-NNN). Vorbild: Vanilla sick_man_of_europe (static_modifiers/content_3_modifiers.txt).

# <wann er gilt>
va_<thema>_<name> = {
	icon = gfx/interface/icons/timed_modifier_icons/modifier_flag_positive.dds # TODO: eigenes Icon (VA-027)
	country_prestige_add = 25
}
```

Modifier-Namen in `docs/modifiers.log` prüfen (`grep -n -A4 "^country_prestige_add:"`); State-Modifier beginnen mit `state_`, Gebäude-Modifier mit `building_`.

## Pflicht-Loc je Objekt

| Objekt | Keys |
|---|---|
| Event | `<id>.t`, `<id>.d`, `<id>.f`, `<id>.a` (`.b` …), ggf. eigene `desc`-Varianten |
| JE | `je_x`, `je_x_reason`, alle `status_desc`-Keys, alle `custom_tooltip`-Texte (`…_tt`) |
| Button | `name`- und `desc`-Key, alle `…_tt` aus `possible` |
| Balken | `name`, `desc`, alle `add = { desc = … }` |
| Static Modifier | `va_x`, `va_x_desc` |
| Decision | `va_x_decision`, `va_x_decision_desc`, `va_x_decision_tooltip` |
| Gebäude | `building_x`, `building_x_desc`, Gruppe `bg_x`, `pmg_…`, `pm_…` |
| Gut | `<gut>`; Modifier-Typen `goods_output_<gut>_add` (+ `_desc`), `goods_input_<gut>_add` (+ `_desc`) |
| Scripted Trigger in Tooltips | `<trigger>_tt`, wenn er per `custom_tooltip` erscheint |

Muster einer Loc-Datei:

```
l_english:   # Datei mit BOM speichern
  je_x: "Drive Out Deathholme (AI WRITTEN)"
  je_x_reason: "In the Ghostlands … (AI WRITTEN)"
  <thema>_events.1.f: "\"Let the ashes of the Scourge feed the soil they poisoned.\" (AI WRITTEN)"
```

## Platzhalter-Grafik

**`event_image` → `video`** (häufig in Vanilla): `unspecific_signed_contract`, `unspecific_politicians_arguing`, `unspecific_ruler_speaking_to_people`, `unspecific_military_parade`, `unspecific_trains`, `unspecific_world_fair`, `unspecific_sick_in_hospital`, `unspecific_gears_pistons`, `unspecific_vandalized_storefront`, `unspecific_naval_battle`, `europenorthamerica_before_the_battle`, `europenorthamerica_capitalists_meeting`, `europenorthamerica_political_extremism`, `europenorthamerica_rich_and_poor`, `europenorthamerica_springtime_of_nations`, `votp_monarch_holding_court`, `votp_conspiring`, `votp_agitator_speaking`, `votp_cops_march`, `middleeast_courtroom_upheaval`, `middleeast_battlefield_trenches`, `middleeast_jungle_expedition`, `africa_construction_colony`, `africa_diplomats_negotiating`, `africa_leader_arguing`, `asia_buddhism`, `africa_animism`, `ip3_village_school`, `ep1_transfer_of_authority`.

**Event-/JE-Icons** `gfx/interface/icons/event_icons/`: `event_default`, `event_newspaper`, `event_protest`, `event_portrait`, `event_skull`, `event_map`, `event_military`, `event_election`, `event_scales`, `event_fire`, `event_industry`, `event_trade`, `waving_flag`, `bicorne_hat` (alle `.dds`).

**Modifier-Icons** `gfx/interface/icons/timed_modifier_icons/modifier_<motiv>_<positive|negative>.dds`, Motive: `flag`, `statue`, `gear`, `coins`, `documents`, `rifle`, `fist`.
