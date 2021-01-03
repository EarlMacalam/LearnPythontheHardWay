## This will only accept digits. Alphanumeric are not welcome. The case
## where the user inputs digits such as 098348003, 03423074, 000000323, and
## the likes, then it is his/her problem anymore.

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")

    if choice.isdigit():
        how_much = int(choice)
    else:
        print("Man, learn to type a number.")
        print("Go back!")
        gold_room()

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def dead(why):
    print(why, "Good job!")
    exit(0)

gold_room()
