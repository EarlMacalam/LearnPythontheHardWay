name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, {weight} I get {total}.")

# conversion
height_to_cm = height * 2.54
print(f"My height in centimeters is {height_to_cm}.")
weight_to_kg = weight * 0.454
print(f"My weight in kilograms is {weight_to_kg}.")
