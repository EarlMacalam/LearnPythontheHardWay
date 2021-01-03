from sys import exit
from sys import argv
game = argv

# intro
print(f"""
Welcome to game {game}. {game} is the game I created cause
Zed told us to make our own any kind of game utlizing what we
learned from the previous exercise.
""")

print("So how do I call you?")
name = input("Hey! Put your name here bastard: ")

print(f"""This game sucks as your name {name} is.
But still, welcome.
Hope you enjoy this {name}.""")


# City
def city():
    print("""
    Unluckily, the city is inhabited with zombies resulted from unknown virus.
    With a shotgun you picked beside the street, you can choose to go inside
    the city or return back and pick another route.
    """)

    choice = input("> ")

    if choice == "go":
        print("The air is the virus.")
        print("You become zombie automatically zombie.")
        dead("You will be undead forever.")

    elif choice ==  "go back":
        road()

    else:
        print("Only 'go' and 'go back' are the valid response.")
        city()

# Forest
def forest():
    print("The forest is inhabited with cannibals.")
    print("Do you wish to proceed or go back and pick another route?")

    choice = input("> ")

    if choice == "go":
        print("""
        You will be hunted by cannibals.
        You will keep on running.
        You will be captured as a sacarifice to the Flying Sphagetti god.
        You die!
        """)
        print("But wait!!! There's more!")
        print("You meet the Mr. Flying Sphagetti at the eternal life.")
        print("You have three wishes!")

        wish1 = input("Wish #1: ")
        print("Wish #1 granted!")
        wish2 = input("Wish #2: ")
        print("Wish #2 granted!")
        wish3 = input("Wish #3: ")
        print("Wish #3 granted!")
        print("CONGRATS!!!")

    elif choice == "go back":
        road()

    else:
        print("Only 'go' and 'go back' are the valid response.")
        forest()

# Beach
def beach():
    print("The beach is full of sharks!")
    print("Do you wanna still go or return and pick another route?")

    choice = input("> ")

    if choice == "go":
        print("The sharks eat you bit by bit including your soul.")
        dead("You die forever.")

    elif choice == "go back":
        road()

    else:
        print("Only 'go' and 'go back' are the valid response.")
        beach()

# Three roads
def road():
    print("""
    There are three roads.
    One leads to city,
    another is forest,
    and lastly to beach.
    Each of the road has their own adventure.
    Where do you wanna go?
    """)

    choice = input("> ")

    if choice == "city":
        city()

    elif choice == "forest":
        forest()

    elif choice == "beach":
        beach()

    else:
        print("You damn undecesive piece of shit! Go home.")
        start()


# dead
def dead(why):
    print(why,"GAME OVER!")
    exit(0)

# start
def start():
    print("WARNING: This game is addictive!")
    print("Do you wanna proceed or not?")

    choice = input("> ")

    if choice == "yes":
        print("""
        It's a sunny day and you have nothing to do.
        You are in the middle of deciding to go outside or
        just stay in the bed and do nothing.
        """)

        do = input("Please decide: ")

        if do == "go outside":
            road()
        else:
            dead("Then we are done")

    else:
        dead("YOU SCARED BITCH!")

start()
