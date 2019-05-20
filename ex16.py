from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
# break script command or continue to running script
print(f"If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
#open file in write mode
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
#empties the file
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# writing to the file
target.write('{}\n{}\n{}\n'.format(line1, line2, line3))

# closing the file
print("And finally, we close it.")
target.close()

print("This is content of your new file: ")
with open(filename) as f:
    text = f.read()
    print(text)
