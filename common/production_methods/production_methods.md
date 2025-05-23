    pm_key = {									# a pm's key must be unique for its building
        texture = "path/to/texture"				# pm icon
        is_default = yes/no						# is this the default pm for its group? if no pm in a group is designated as the default, the first pm is considered the default.

        country_modifiers = {					# these modifiers are applied to the country if this pm is active
            workforce_scaled = {				# these modifiers are scaled by the staffing level of the building, note that staffing level scales between 0.0 and building level.
                # modifier definition
            }
            level_scaled = {					# these modifiers are scaled by the level of the building
                # modifier definition
            }
            unscaled = {						# these modifiers are not scaled
                # modifier definition
            }
        }

        state_modifiers = {						# these modifiers are applied to the state if this pm is active
            # same as country_modifiers
        }

        building_modifiers = {					# these modifiers are applied to the building if this pm is active
            # same as country_modifiers
        }

        timed_modifiers = {						# these modifiers are applied to the building after pm is changed. Duration is BUILDING_TIMED_MODIFIER_WEEKS
            # list of modifiers
        }

	    required_input_goods = key				# a pm may list one or more goods as a required input goods, those goods need to be accessible to the building to be able to activate the this pm

        unlocking_laws = {						# optional list of required laws to be able to activate this pm
            # list of law keys
        }

        unlocking_technologies = {				# optional list of required technologies to be able to activate this pm
            # list of technology keys
        }

        unlocking_production_methods = {		# optional list of required pm's to be able to activate this pm
            # list of pm keys					# these must refer to pm keys on the same building
        }

        unlocking_global_technologies = {		# optional list of technologies that need to be invented in the world to be able to activate this pm
            # list of technology keys
        }

        unlocking_principles = {				# optional list of Power Bloc principles required for a country to activate this pm
            # list of principle keys
        }
	
        unlocking_identity = key				# optional key for Power Bloc identity required for a country to activate this pm (repeateable)
	
        ai_weight = fixed_point					# base AI weight, default 1.0
        pollution_generation = fixed_point		# how much visual pollution does this building add to its state region while this pm is active (total pollution in state region is scaled by arable land), default 0.0
    }