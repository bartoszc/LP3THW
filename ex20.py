from sys import argv

# unpack variables
script, input_file = argv

# function definition
def print_all(f):
    print(f.read())

# The method seek() sets the file's current position at the offset.
def rewind(f):
    f.seek(0)

# function takes two arguments - number of line and file. Prints line count number and one line of the fie
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

# open the file in read mode
current_file = open(input_file)

print("First let's print the whole file:\n")

# print all content of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# calling function
rewind(current_file)

print("Let's print three lines:")

current_line = 1 # 1
print_a_line(current_line, current_file)

current_line +=1 # 2
print_a_line(current_line, current_file)

current_line += 1 # 3
print_a_line(current_line, current_file)
