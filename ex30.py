people = 100
cars = 78
trucks = 29

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We cann't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")



if cars > people or trucks == cars:
    print("We should take the cars.")
elif cars < people and trucks < cars:
    print("We should not take the cars.")
else:
    print("We cann't decide.")

if trucks > cars and people <= trucks:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We can't decide.")

if people > trucks or trucks >= cars:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
