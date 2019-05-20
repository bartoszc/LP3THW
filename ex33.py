from sys import argv

_ , number, incrementator = argv

number = int(number)
incrementator = int(incrementator)

def while_loop(n, inc):
    i = 0
    numbers = []

    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += int(inc)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


        print("The numbers: ")

        for num in numbers:
            print(num)


def for_loop(n, inc):
    numbers = []

    for i in range(0, n, inc):
        numbers.append(i)
        print(f"I is {i}")
        print("Numbers now: ", numbers)

    print("The numbers: ")

    for num in numbers:
        print(num)


while_loop(number, incrementator)
for_loop(number, incrementator)
