'''
This is a finance calculation program to calculate investment or bond repayment based on user input
This code defines two functions, investment calculator and bond repayment calculator. 

The user is prompted for their choice (either investment or bond).
If the user selects investment, then two calculations options are displayed (either simple interest or compound interest).
The user is further prompted to choose one of the two interest options above 
further input is required such as investment amount, interest rate and period of investment
calculation is then done based on user input.

Else, if the user selects 'Bond' from the initial prompt, 
the user has to enter further input such as present value of the house, interest rate and repayment months
then calculation is done based on user input.
'''



import math


# Function to calculate investment turnover
def investment_calculator():
    # Prompt user to input investment details
    deposit_amount = float(input("Enter the intended investment amount here: "))
    annual_interest_rate1 = float(input("Enter the interest rate here (percentage e.g. 8): ")) / 100
    investment_years = int(input("Enter the intended number of investment years here: "))
    interest_type = input("Choose 'simple' or 'compound' interest: ").lower()

    # Calculate simple interest
    if interest_type == "simple":
        total_investment_turnover = deposit_amount * (1 + annual_interest_rate1 * investment_years)
        print("Your total investment turnover after", investment_years, "years with simple interest is:", total_investment_turnover)

    # Calculate compound interest
    elif interest_type == "compound":
        total_investment_turnover = deposit_amount * math.pow((1 + annual_interest_rate1), investment_years)
        print("Your total investment turnover after", investment_years, "years with compound interest:", total_investment_turnover)

    else:
        print("Invalid selection! Please enter 'simple' or 'compound'.")

# Function to calculate bond repayments
def bond_repayment_calculator():
    # Prompt user to input investment details
    present_value = float(input("Enter the present value of the house: "))
    annual_interest_rate2 = float(input("Enter the annual interest rate (percentage): ")) / 100
    monthly_interest_rate = annual_interest_rate2 / 12
    repayment_period = int(input("Enter the number of months you intend to repay the bond: "))

    # Calculate monthly repayments
    monthly_bond_repayment = (monthly_interest_rate * present_value) / (1 - (1 + monthly_interest_rate) ** (-repayment_period))
    print("Your monthly repayment amount is :", monthly_bond_repayment)


# Main program loop
print("Dear User, you are welcome to your Finance Calculator!")
print("Please choose the operation that you would like to perform at this time")
print("Option 1: INVESTMENT - to calculate the amount of interest you will earn on your investment")
print("Option 2: BOND - to calculate the amount you will have to pay on a home loan")

selection = input("Enter your choice here 'investment' or 'bond' ").lower()

if selection == "investment":
    investment_calculator()
elif selection == "bond":
    bond_repayment_calculator()
else:
    print("Invalid selection! Please enter 'investment' or 'bond' to proceed.")

