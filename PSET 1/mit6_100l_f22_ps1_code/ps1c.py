## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_house = 800_000
months = 36
steps = 0
r = 0.0
low = 0.0
high = 1.0

# Derived
down_payment_needed = cost_house * 0.25

def get_amount_saved():
    return initial_deposit * ((1 + r/12) ** months)

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

while (abs(down_payment_needed - get_amount_saved()) >= 100):
    if (initial_deposit >= down_payment_needed - 100):
        break

    if (r >= high):
        r = None
        break

    if (get_amount_saved()) < down_payment_needed:
        low = r
    else:
        high = r
    r = (low + high) / 2.0
    steps += 1