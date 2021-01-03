# Assigning names to an object
types_of_people = 10

# Print the variable types_of_people inside the string
x = f"There are {types_of_people} types of people."

# Assigning names to an object
binary = "binary"
# Assigning names to an object
do_not = "don't"
# Print the variables binary and do_not inside the string
y = f"Those who know {binary} and those who {do_not}."

# print
print(x)
# print
print(y)

# Print the variable x inside the string
print(f"I said: {x}")
# Print the variable y inside the string
print(f"I also said: '{y}'")

# Assigning names to an object, in this case logical object
hilarious = False
# Just another string with a reserved slot fo a variable
joke_evaluation = "Isn't that joke so funny?! {}"
# printing the string at the same time putting a variable to the reserved slot
print(joke_evaluation.format(hilarious))

# Assigning names to an object, in this case string object
w = "This is the left side of..."
# Assigning names to an object, in this case string object
e = "a string with a right side."

# Concatinate/join/combine the two strings
print(w + e)
