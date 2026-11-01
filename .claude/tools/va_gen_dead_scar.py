# Erzeugt die regionsweisen Teile der Todesschneisen-Heilung (VA-046): Balken, Schalter, Monatsprüfung, Loc.
import sys

ROOT = sys.argv[1]
BOM = '﻿'

# (Schlüssel, State-Region, englischer Name)
REGIONS = [
    ('sunwell_plateau', 'STATE_SUNWELL_PLATEAU', 'Sunwell Plateau'),
    ('ruins_of_silvermoon', 'STATE_RUINS_OF_SILVERMOON', 'Ruins of Silvermoon'),
    ('west_sanctum', 'STATE_WEST_SANCTUM', 'West Sanctum'),
    ('east_sanctum', 'STATE_EAST_SANCTUM', 'East Sanctum'),
    ('tranquillien', 'STATE_TRANQUILLIEN', 'Tranquillien'),
    ('deathholme', 'STATE_DEATHHOLME', 'Deathholme'),
]
DURATION = 20  # Monate aktiver Heilung je Region
START_COST = 100000  # Einmalkosten beim Einschalten eines Rituals (Kono 2026-10-31)


def write(path, text):
    with open(f'{ROOT}/{path}', 'w', encoding='utf-8', newline='\n') as f:
        f.write(BOM + text)


# --- Fortschrittsbalken ---
bars = ['# Ein Balken je Region der Todesschneise (VA-046), erzeugt von .claude/tools/va_gen_dead_scar.py.\n'
        '# Vorbild: Vanilla bavarocracy-Balken (scripted_progress_bars/00_greece_progress_bars.txt).\n'
        '# Scope in monthly_progress: das Land selbst (nicht der Journal Entry). Fortschritt nur mit Ritual Site in der Region, die all ihre Inputs (Mana, Papier) bekommt (Kono 2026-11-01: gilt auch für Untote ohne Mana-Entzug).\n']
for key, region, name in REGIONS:
    bars.append(f'''
va_dead_scar_bar_{key} = {{
	name = "va_dead_scar_bar_{key}"
	desc = "va_dead_scar_bar_{key}_desc"

	default_green = yes

	monthly_progress = {{
		if = {{
			limit = {{
				any_scope_state = {{
					state_region = s:{region}
					va_state_on_dead_scar_trigger = yes
					any_scope_building = {{
						is_building_type = building_va_scar_ward
						building_has_goods_shortage = no
					}}
				}}
			}}
			add = {{
				desc = "va_dead_scar_bar_progress_desc"
				value = 1
			}}
		}}
		# Stillstand im Tooltip sichtbar machen (Kono 2026-11-01)
		else_if = {{
			limit = {{
				any_scope_state = {{
					state_region = s:{region}
					any_scope_building = {{
						is_building_type = building_va_scar_ward
						building_has_goods_shortage = yes
					}}
				}}
			}}
			add = {{
				desc = "va_dead_scar_bar_stalled_desc"
				value = 0
			}}
		}}
	}}

	start_value = 0
	min_value = 0
	max_value = {DURATION}
}}
''')
write('common/scripted_progress_bars/va_dead_scar_progress_bars.txt', ''.join(bars))

# --- Schalter ---
btn = ['# An-/Aus-Schalter der Heilung je Region (VA-046), erzeugt von .claude/tools/va_gen_dead_scar.py.\n'
       '# Vorbild: Vanilla je_haitian_debt_payment_button (scripted_buttons/00_hispaniola_buttons.txt).\n'
       '# An: Ritual Site im eigenen State der Region bauen. Aus: wieder abreißen (Fortschritt bleibt im Balken).\n']
for key, region, name in REGIONS:
    btn.append(f'''
va_dead_scar_start_{key}_button = {{
	name = "va_dead_scar_start_{key}_button"
	desc = "va_dead_scar_start_button_desc"

	visible = {{
		any_scope_state = {{
			state_region = s:{region}
			va_state_on_dead_scar_trigger = yes
			NOT = {{ has_building = building_va_scar_ward }}
		}}
	}}

	possible = {{
		custom_tooltip = {{
			text = va_dead_scar_ward_not_bankrupt_tt
			NOT = {{ has_modifier = declared_bankruptcy }}
		}}
	}}

	ai_chance = {{
		value = 0
		if = {{
			limit = {{
				NOT = {{ has_modifier = va_mana_withdrawal }}
				scaled_debt <= 0
			}}
			add = 25
		}}
	}}

	effect = {{
		add_treasury = -{START_COST}
		random_scope_state = {{
			limit = {{
				state_region = s:{region}
				va_state_on_dead_scar_trigger = yes
			}}
			create_building = {{
				building = building_va_scar_ward
				level = 1
				activate_production_methods = {{ pm_ritual_circles_building_va_scar_ward }}
			}}
		}}
	}}
}}

va_dead_scar_stop_{key}_button = {{
	name = "va_dead_scar_stop_{key}_button"
	desc = "va_dead_scar_stop_button_desc"

	visible = {{
		any_scope_state = {{
			state_region = s:{region}
			has_building = building_va_scar_ward
		}}
	}}

	ai_chance = {{
		value = 0
		if = {{
			limit = {{
				OR = {{
					has_modifier = declared_bankruptcy
					scaled_debt > 0.5
				}}
			}}
			add = 50
		}}
	}}

	effect = {{
		# Eigener Tooltip: Vanilla-Text zu remove_building ist kaputt (BUG: missing perspective)
		custom_tooltip = va_dead_scar_stop_tt
		hidden_effect = {{
			every_scope_state = {{
				limit = {{
					state_region = s:{region}
					has_building = building_va_scar_ward
				}}
				remove_building = building_va_scar_ward
			}}
		}}
	}}
}}
''')
write('common/scripted_buttons/va_dead_scar_buttons.txt', ''.join(btn))

# --- Monatsprüfung: volle Balken heilen die Region ---
eff = ['# Monatsprüfung der Todesschneisen-Heilung (VA-046), erzeugt von .claude/tools/va_gen_dead_scar.py.\n'
       '# Country-Scope aus je_va_dead_scar (on_monthly_pulse). Voller Balken + Region noch verdorben → Ritual Site weg, Region heilen, Event.\n'
       '# Vorbild: Balkenabfrage wie Vanilla je_expedition (00_antarctica.txt).\n\n'
       'va_dead_scar_heal_pulse_effect = {\n']
for key, region, name in REGIONS:
    eff.append(f'''	if = {{
		limit = {{
			scope:journal_entry = {{ "scripted_bar_progress(va_dead_scar_bar_{key})" >= {DURATION} }}
			any_scope_state = {{
				state_region = s:{region}
				va_state_on_dead_scar_trigger = yes
			}}
		}}
		random_scope_state = {{
			limit = {{
				state_region = s:{region}
				va_state_on_dead_scar_trigger = yes
			}}
			save_scope_as = va_healed_state
		}}
		scope:va_healed_state = {{
			if = {{
				limit = {{ has_building = building_va_scar_ward }}
				remove_building = building_va_scar_ward
			}}
			va_heal_dead_scar_state_effect = yes
		}}
		trigger_event = {{ id = dead_scar_events.1 popup = yes }}
	}}
''')
eff.append('}\n')
write('common/scripted_effects/va_dead_scar_effects.txt', ''.join(eff))

# --- Loc ---
loc = ['l_english:\n']
for key, region, name in REGIONS:
    loc.append(f'  va_dead_scar_bar_{key}: "Healing: {name}"\n')
    loc.append(f'  va_dead_scar_bar_{key}_desc: "{name}"\n')  # kurz, der Balken schneidet lange Texte ab
    loc.append(f'  va_dead_scar_start_{key}_button: "Start Ritual: {name}"\n')
    loc.append(f'  va_dead_scar_stop_{key}_button: "Stop Ritual: {name}"\n')
# Handgeschriebene Einträge (alles ab der ersten Leerzeile) bleiben erhalten
LOC = 'localization/replace/english/va_dead_scar_regions_l_english.yml'
try:
    with open(f'{ROOT}/{LOC}', encoding='utf-8-sig') as f:
        old = f.read()
    cut = old.find('\n\n')
    if cut >= 0:
        loc.append(old[cut + 1:])
except FileNotFoundError:
    print('Hinweis: keine bestehende Loc-Datei, nur generierte Einträge geschrieben')
write(LOC, ''.join(loc))

# --- JE-Knöpfe zum Einfügen ---
print('\n'.join(f'\tscripted_progress_bar = va_dead_scar_bar_{k}' for k, _, _ in REGIONS))
print('\n'.join(f'\tscripted_button = va_dead_scar_start_{k}_button\n\tscripted_button = va_dead_scar_stop_{k}_button' for k, _, _ in REGIONS))
