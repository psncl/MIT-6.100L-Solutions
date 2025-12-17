def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	portion_down_payment = 0.25
	amount_saved = 0
	rate_annual = 0.05
	months = 0
	
	## Derived
	full_down_payment = cost_of_dream_home * portion_down_payment
	monthly_salary_saved = (yearly_salary * portion_saved) / 12
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	
	while (amount_saved < full_down_payment):
	    amount_saved += amount_saved * (rate_annual / 12)
	    amount_saved += monthly_salary_saved
	    months += 1
	return months