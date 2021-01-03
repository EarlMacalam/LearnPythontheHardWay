# and
print(5 == 6 and 7 == 7)

# as
from sys import argv
script, first = argv

with open(first, "w") as file:
    file.truncate()
    file.write("Hello")

# assert
def age(x):
    assert x > 0, "Age can't be negative!"
    print("""Prints age.""")
    print(f"My age is {x}.")

# break
n = 0

while n < 5:
    print(f"n above is {n}.")
    print(n)

    if n == 3:
        print("We break.")
        break

    n += 1
    print(f"n below is {n}.")

# continue
n = 0

while n < 5:
    print(f"n above is {n}.")
    n += 1

    if n == 3:
        print("Skip this.")
        continue

    print(n)
    print(f"n below is {n}.")


# class
class Employee:

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.email = first + "." + last + "@yahoo.com"
        self.pay = pay

    def full_name(self):
        return f"{self.firstname} {self.lastname}"


employee_1 = Employee("Maria", "Lina", 60000)
employee_2 = Employee("Earl", "Macalam", 50000000)

print(employee_1.email)
print(employee_1.firstname)
print(employee_2.email)
print(employee_2.firstname)

print(employee_1.full_name())
print(employee_2.full_name())


# del
list = ["a", 2, 3, 4, 'x', 'z']
del list[0]
print(list)

# except
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as e:
    print(e)

# finally (do everything no matter except executes)
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err:
    print(err)
finally:
    print("Executing everything....")

# exec (for evaluating statements in a string)
exec("c = 'mello'")
exec("c = 3")
print(c)

# global
x = 5 # this global

def sample():
    y = 67 # this is local since its inside the function
    print(y)
    print(x)

print(y) # note that this is outside the function and this is local so it produces error
sample() # but x still prints even its inside the function since its global

# lambda (creates anonymous function)
s = lambda y: y ** y; print(s(3))
y = lambda x, y: x * y; print(y(2, 3))

# pass
for i in range(100):
    print(i)
    if i > 5:
        pass # unlike continue which return on the loop, this do nothing and just proceed no matter what
    else:
        print("Hello")

    print("Please come here.")

# raise (raise exception of our own to that particular code)
try:
    f = open('sample.txt')
    if f.name == 'sample1.txt':
        raise Exception

except Exception:
    print('Error!')

else:
    f.truncate()

finally:
    print("Executing everything...")


# yield
def squarring_num(list):
    for i in list:
        yield(i * i)

my_list = [1, 2, 3, 4, 5]
results =  squarring_num(my_list)

for i in results:
    print(i)
