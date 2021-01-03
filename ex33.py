i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print(f"Numbers now: {numbers}")

    print(f"At the bottom i is {i}")

print("The numbers: ")

for number in numbers:
    print(number)


# STUDY DRILLS

def while_funtion(x):
    i = 0
    numbers = []

    while i < x:
        print(f"At the top i is {i}.")
        numbers.append(i)

        i = i + 1
        print(f"The numbers: {numbers}")
        print(f"At the bottom i is {i}")

while_funtion(10)
while_funtion(9)
while_funtion(8)

def while_funtion(x, y):
    i = 0
    numbers = []

    while i < x:
        print(f"At the top i is {i}.")
        numbers.append(i)

        i = i + y
        print(f"The numbers: {numbers}")
        print(f"At the bottom i is {i}")

while_funtion(6, 2)


# rewriting to for loop
def for_loop(x):
    numbers = []
    i = 0

    for i in range(0, x):
        print(f"At the top i is {i}.")
        numbers.append(i)

        i += 1
        print(f"The numbers: {numbers}")
        print(f"At the bottom i is {i}.")

for_loop(6)
