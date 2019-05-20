# import argv
from sys import argv

# parameters to variables
script, filename = argv

# opening the file
txt = open(filename)

# print filename
print(f"Here's your file {filename}:")

# calling method read on textfile
print(txt.read())
txt.close()

# another print
print("Type the filename again:")

# fancy input
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
