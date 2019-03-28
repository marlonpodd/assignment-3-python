#Assignment # 3 PYTHON CODE
#Marlon

#module
import math

#size
sizechoice = int(input("Type 1 for a Large pizza or type 2 for a Extra Large pizza: "))
if sizechoice == 1:
	sizeOfPizza = 6
	print ("Large Pizza requested")
	print (" ")
elif sizechoice == 2:
	sizeOfPizza = 10
	print ("Extra Large Pizza requested")
	print (" ")
else:
	print ("404 size not found :(")

#Toppings
topchoice = int(input("Type 1, 2, 3, or 4 for the number of toppings you would like on your pizza: "))
if topchoice == 1:
	numberOfToppings = 1
	print ("1 Topping requested")
	print (" ")
elif topchoice == 2:
	numberOfToppings = 1.75
	print ("2 Toppings requested")
	print (" ")
elif topchoice == 3:
	numberOfToppings = 2.50
	print ("3 Toppings requested")
	print (" ")
elif topchoice == 4:
	numberOfToppings = 3.35
	print ("4 Toppings requested")
	print (" ")
else:
	print ("404 toppings not found :(")

#function
subtotal = (sizeOfPizza + numberOfToppings)
tax = (subtotal * 0.13)
totalcost = (sizeOfPizza + numberOfToppings)*1.13
taxround = (round(tax, 2))
totalcostround = (round(totalcost, 2))

#Cost textfields
print (" ")
print ("The subtotal is", subtotal)
print ("The tax is ", taxround)
print ("The total cost is", totalcostround)