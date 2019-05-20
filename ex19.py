# function taken two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


def test_function(arg1, arg2):
    return(f"Value of arg1 = {arg1} and value for arg 2 = {arg2} \n")


print(test_function(1, 2))

a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
print(test_function(a, b))

c = 5
d = 10
print(test_function(c, d))

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def order_stats(total_orders, total_returns):
    print(f"You have {total_orders} orders")
    print(f"You have {total_returns} returns")
    print(f"Your net sales are {total_orders - total_returns}")
    print("Hopefully you had a good month!\n")

# Simple arguments
order_stats(4321, 1234)

# Math
order_stats(102+321, 456*4) # ouch, bad month

# Variables
jims_sales = 395
sally_sales = 72
joan_sales = 5481 # way to go Joan!
returns = 32
order_stats(jims_sales+sally_sales+joan_sales, returns)

# Variables and math
order_stats((jims_sales*4)+(sally_sales%4)+(joan_sales%4), returns)

# Assign the function to a variable? (it works!)
order_totals = order_stats
order_totals(30,1)

# With a variable number of arguments - a la *args? (it works!)
var_stats = (560, 42)
order_stats(*var_stats)

# function to function? (it works!)
def func_to_func():
    value1 = 20
    value2 = 30
    order_stats(value1, value2)
func_to_func()

# user input - Don't forget to specify a type of input! In this case an integer
print("how much did you sell this month?")
user_sales = int(input('>>>'))
order_stats(user_sales, returns)
