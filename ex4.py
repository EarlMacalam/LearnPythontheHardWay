
# assigning names and values
cars = 100
# assigning names and values
space_in_a_car = 4.0
# assigning names and values
drivers = 30
# assigning names and values
passengers = 90
# computing
cars_not_driven = cars - drivers
# assigning names and values
cars_driven = drivers
# computing
carpool_capacity = cars_driven * space_in_a_car
# computing
average_passengers_per_car = passengers / cars_driven

# print strings and the variable car
print("There are", cars, "cars available.")
# print strings and the variable drivers
print("There are only", drivers, "drivers available.")
# print strings and the variable cars_not_driven
print("There will be", cars_not_driven, "empty cars today.")
# print strings and the variable carpool_capacity
print("We can transport", carpool_capacity, "people today.")
# print strings and the variable passengers
print("We have", passengers, "to carpool today.")
# print strings and the variable average_passengers_per_car
print("We need to put about", average_passengers_per_car, "in each car.")
