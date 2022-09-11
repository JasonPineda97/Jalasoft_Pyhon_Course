"""
Loan payment calculator
"""

# Get the details of the loan from the user: How much money do you owe, in dollars?​
money = input("How much money do you owe, in dollars?")
# Convert input to float​
money_owed = float(money)
# Get the annual percentage rate: what us the annual percentage rate?​
annual_rate = int(input("What us the annual percentage rate?"))
# Get the monthly payment: what will your monthly payment be, in dollars?​
monthly_payment = float(input("What will your monthly payment be?"))
# Get  months to calculate results: how many months do you want to see the results for?​
months = int(input("How many months do you want to see the results for?"))
# Repeat the calculation for all the months the user  wants to see results for​
for month_count in range(0, months, 1):
    # Divide annual percentage rate by 100 to make it a percent, then divide by 12 to get the monthly insterest rate
    monthly_rate = annual_rate/100/12
    #   monthly_rate = apr/100/12
    # add in  interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed * interest_paid
    #   interest_paid = money_owed * monthly_rate
    #   money_owed = money_owed + interest_paid
    # Make payment
    money_owed = money_owed - monthly_payment
    #   money_owed = money_owed - payment
    # Print the results 
    print("Paid", monthly_payment, "of which", interest_paid, "was interest")
    print("Now, I owe", money_owed)
    #   print("Paid", payment, "of which", interest_paid, "was interest")
    #   print("Now, I owe", money_owed)

    # add control to check if money_owed - payment < 0 then print messages and break repetition
    if(money_owed - monthly_payment < 0):
        print("You have already paid your debt")
        break
    print("The last payment is", money_owed)
    print("You pay off the loan in", month_count, "months")
#   print("the last payment is", money_owed)
#   print("You pay off the loan in", month_count, "months")

# round the dollar amount to two decimals 