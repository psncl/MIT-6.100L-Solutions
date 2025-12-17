## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
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