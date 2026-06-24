# inputs we need from the user
# total rent
# total food 
# electricity 
# charge per unit
# people living in flat

#output
#total amount you have to pay

rent =  int(input("enter your flat rent = "))
food = int(input("enter the amount of food ordered = "))
electricty_spent = int(input("enter the amount of the electricity that has been spent = "))
charge_per_unit = int(input("enter the charge per unit = "))
people = int(input("enter the amount of people living inside of the flat = "))

total_bill = electricty_spent * charge_per_unit + rent + food / people
print (f"total bill is = ", round(total_bill))


