from sys import exit

def sweet_room():
    print("This room is full of sweets... how many sweets do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Hey, learn to type a whole number")

    if how_much <50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy tike!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear grabs you and eats you, yum!")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets fed up and eats you!")
        elif choice == "open door" and bear_moved:
            sweet_room()
        else:
            print("I have not idea what that means.")

def sarlak_room():
    print("Here you see the great hungry Sarlak.")
    print("He, it, whatever will digest you slowly.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Game over!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

sweet_room()
start()
