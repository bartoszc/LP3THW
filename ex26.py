from sys import argv # fixed - added import steatment

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input() # fixed - added new variable height
print("How much do you weigh?", end=' ') # fixed - added '('
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filename) # fixed - typo in word filename

print(f"Here's your file {filename}:") # fixed - added 'f' at the begging of the print steatment
print(txt.read()) # fixed - typo in word txt

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read()) # fixed - typo in name of variable txt_again


print("Let's practice everything.") # fixed - wrong paranthesis
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') # fixed - multiline string

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") # fixed - missing " character
print(poem)
print("--------------") # fixed - missing " character


five = 10 - 2 + 3 - 6 # fixed - added number 6
print(f"This should be five: {five}") # fixed - missing ) character

def secret_formula(started): #  fixed - missing colon
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars + 100 # fixed - missing math character
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # fixed - missing one unpack value

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # fixed - wrong variable name
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30 # fixed - typo in cats
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!") # fixed - missing () arround print

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # fixed - missing colon
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: # fixed - missing colon
    print("People are less than or equal to dogs.") # fixed - missing " character

if people == dogs: # fixed - = replaced by ==
    print("People are dogs.")
