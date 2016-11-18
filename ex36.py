import random

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
        _hp = 8
        _atk = 5
        _def = 5
        _spd = 1
        _spe = "STENCH"

    elif choice == "Binky":
        print " HP: 4\n ATK: 3\n DEF: 7\n SPD: 3"
        print " SPE: GREEDY - You gain double the gold after each battle"
        _hp = 4
        _atk = 3
        _def = 7
        _spd = 3
        _spe = "GREEDY"

    elif choice == "Bloopy":
        _hp = 10
        _atk = random.randint(1, 10)
        _def = random.randint(1, 10)
        _spd = random.randint(1, 10)
        _spe = "BLOOP"
        print " HP: 10\n ATK: %d\n DEF: %d\n SPD: %d" % (_atk, _def, _spd)
        print " SPE: BLOOP - Items you find may randomly change into other items of higher or lower value"

    elif choice == "Buppy":
        print " HP: 5\n ATK: 8\n DEF: 2\n SPD: 8"
        print " SPE: CRIT - Your attacks do double the damage"
        _hp = 5
        _atk = 8
        _def = 2
        _spd = 8
        _spe = "CRIT"

    return choice, _hp, _atk, _def, _spd, _spe

def start(start_choice):
    if start_choice == "1":
        character, _hp, _atk, _def, _spd, _spe = select_character()
        #print character, _hp, _atk, _def, _spd, _spe

def save(character, _hp, _atk, _def, _spd, _spe, room):
    data = [character, _hp, _atk, _def, _spd, _spe, room]
    save = open(data.txt, 'w')
    for i in data:
        save.write(i)
        save.write("\n")


print "1. New Game"
print "2. Load Game"
print "3. Quit"

start_choice = raw_input("> ")

start(start_choice)
