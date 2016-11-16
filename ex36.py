import random

def start(start_choice):
    if start_choice == "1":
        select_character()


def select_character():
    print "Choose your character:"
    print "Stinky"
    print "Binky"
    print "Bloopy"
    print "Buppy"

    choice = raw_input("> ")
    print "You chose %s. These are your stats" % choice

    if choice == "Stinky":
        print " HP: 8\n ATK: 5\n DEF: 5\n SPD: 1"
        print " SPE: STENCH - Enemies and allies take 1 damage per turn"

    elif choice == "Binky":
        print " HP: 4\n ATK: 3\n DEF: 7\n SPD: 3"
        print " SPE: GREEDY - You gain double the gold after each battle"

    elif choice == "Bloopy":
        print " HP: 10\n ATK: %d\n DEF: %d\n SPD: %d" % (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
        print " SPE: BLOOP - Items you find may randomly change into other items of higher or lower value"

    elif choice == "Buppy":
        print " HP: 5\n ATK: 8\n DEF: 2\n SPD: 8"
        print " SPE: Crit - Your attacks do double the damage"

    return choice


print "1. New Game"
print "2. Load Game"
print "3. Quit"

start_choice = raw_input("> ")

start(start_choice)
