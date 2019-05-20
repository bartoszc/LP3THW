# creating a variable
types_of_people = 10

# format string
x = f"There are {types_of_people} types of people."

# Sets variable y to string with two embedded format strings
# (binary and do_not)
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print x
print(x)

# print y
print(y)

# 2
print(f"I said: {x}")
print(f"I also said: '{y}'")

# boolean value
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
