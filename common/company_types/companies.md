company_key = {
	icon = "texture path"
	background = "texture path"
	
	flavored_company = yes/no

	uses_dynamic_naming = yes/no
	dynamic_company_type_names = {
	}
	
	building_types = { 
	}

	replaces_company = other_company_key
	
	# The following three triggers are used to split companies into four different categories: hidden/potential/attainable/available
	# All of them are evaluated in country scope.
	# If a company fails the first trigger it is hidden, if it passes the first but fails the second it is shown as a potential company,
	# so and so forth until if it passes all three triggers then it is shown as an available company.
	potential = {
		# A trigger evaluated in country scope to determine if this company type should be shown to the player as a potential company
	}
	attainable = {
		# A trigger evaluated in country scope to determine if this company type should be shown to the player as an attainable company
	}
	possible = { 
		# A trigger evaluated in country scope to determine if this company type should be available to the player
	}
	can_establish_in = {
		# A trigger evaluated in state scope to determine if this company type can have its building located in the scoped state
	}
	
	prosperity_modifier = {
	}	
	
	ai_weight = {
	}
}
