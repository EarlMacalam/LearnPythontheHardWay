from sys import argv
script, alien, monster, user_name = argv
prompt = '>>> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"Are you an {alien}?")
alien = input(prompt)

print(f"Are you a {monster}?")
monster = input(prompt)


print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer}. Nice.
Also you told me that you're {alien} and {monster}!!!
""")