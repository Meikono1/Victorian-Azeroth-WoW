	pm_group_key = {								        
		production_methods = {												# A list of Production Methods contained in this group. One and only one must be active at any one time
			pm_bakery
			pm_sweeteners
			pm_baking_powder
		}
		is_hidden_when_unavailable = no										# Whether PMs in this group should be visible at all if they cannot currently be switched to
		ai_selection = most_productive										# Affects how the AI chooses between PMs. Current options: most_profitable, most_productive. Default most_profitable
		texture = "gfx\interface\icons\generic_icons\mixed_icon_base.dds"	# Different types of PM Groups should have different icons for when the Building panel has mixed configuration
	}