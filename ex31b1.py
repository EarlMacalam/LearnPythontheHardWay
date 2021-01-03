
# 1. Make new parts of the game and change what decisions people can make.
# Expand the game out as much as you can before it gets ridiculous.

print("""You enter a dark room with three doors.
Do you go through door #1, door #2, door #3?""")

door = input("> ")

if door == "1":
    print("There is a gian bear here eating a cheescake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Kill the bear!")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "3":
        print("The bear will fight.")
        print("You combat with it!")
        print("But you win! Congrats!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into an endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling molodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("Your arrived into a new dimension place!")
    print("It's called the limbo, a place for unbaptized infants.")
    print("You meet satan there what will you do?")
    print("1. Talk and ask about spiritual stuffs.")
    print("2. Ask how hell was created.")
    print("3. Let him introduce hiself.")

    decision = input("> ")

    if decision == "1":
        print("Ask him if God really exists?")
    elif decision == "2":
        print("Will I go to hell?")
    else:
        print("Be friends with Satan.")

else:
    print("You stumble around and fall on a knife and die. Good job.")
