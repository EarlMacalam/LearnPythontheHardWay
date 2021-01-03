def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    print(f"Subtract {a} and {b}")
    return a - b

def multiply(a, b):
    print(f"Multiply {a} and {b}")
    return a * b

def divide(a, b):
    print(f"Divide {a} and {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "\nCan you do it by hand?")

### DRILL ###
# normal formula
def normal_formula(w, x, y, z):
    print("Here's the combined formula")
    return w + (x - (y * (z / 2)))

whatv2 = normal_formula(age, height, weight, iq)
print(f"Result: {whatv2}")

# modifying the formula
def normal_formula(w, x, y, z):
    print("Here's the modified formula")
    return w + (y * (x - (z / 2)))

whatv2 = normal_formula(age, height, weight, iq)
print(f"Result: {whatv2}")

# doing the inverse
# my_own_formula = 500 - (((64 / 4) * 28) + 35) = 17

apple = add(250, 250)
mango = multiply(8, 8)
banana = divide(56, 2)
pineapple = subtract(40, 5)

print(f"Apple: {apple}, Mango: {mango}, Banana: {banana}, Pineapple: {pineapple}")
my_formula = subtract(apple, add(multiply(divide(mango, 4), banana), pineapple))
print(f"Own Formula Result: {my_formula}")
