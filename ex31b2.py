

###### THE GAME OF CONSEQUENCES ######
print("""
What's life?
How do we live it?
Is there a right formula to live it?
Even science and philosophy have no fixed answer to these questions.
But what do religion say about these things?
Let's play the game of consequences. Enjoy :)
""")

print("How will you live you life? Choose one among the three choices:")
print("Choice #1: The Diest Path")
print("Choice #2: The Athiest Path")
print("Choice #3: The Agnostic Path")

print("NOTE! Type 1 or 2 or 3 for your choice.")

choice = input("> ")

if choice == "1":
    print("WARNING! KNOW THE ROOTS!")
    print("""
    For simplicity we will focus on Christianity.
    Religious dogmatism is the main weapon here.
    Lot's of tasks and responsibilities that were based on a book called Bible.
    """)

    print("Is Bible true of not.")
    print("1. Yes, it is!")
    print("2. Ofcourse not.")

    bible = input("> ")

    if bible == "1":
        print("Then congrats! You'll be sent to heaven")
    elif bible == "2":
        print("Bye bye goodluck to hell.")

elif choice == "2":
    print("WARNING! DONT BECOME A NIHILIST!")
    print("""
    Your'e one of the freethinker.
    Your'e brave!
    You live your life on your own.
    No more excuses! No more pretending! No more guilt!
    Just be fucking moral without conditions and dependencies.
    """)

elif choice == "3":
    print("ARE YOU A COWARD ATHIEST?")
    print("""
    You believe in flying sphagetti.
    Lacks courage.
    Maybe a Christian 10%.
    """)

else:
    print("INVALID CHOICE!")
    print("More chance of dying.")
