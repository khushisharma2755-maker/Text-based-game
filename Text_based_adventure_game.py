def start():
    print("You wake up in a dark forest. Two paths lie ahead.")
    print("1. Take the left path")
    print("2. Take the right path")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice, try again.")
        start()

def left_path():
    print("\nYou walk down the left path and find a river.")
    print("1. Try to swim across")
    print("2. Follow the river")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        print("\nThe current is too strong. You drown. Game Over.")
    elif choice == "2":
        print("\nYou follow the river and find a village. You are safe! You win!")
    else:
        left_path()

def right_path():
    print("\nYou walk down the right path and meet a hungry wolf.")
    print("1. Run away")
    print("2. Fight the wolf")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        print("\nYou escape safely but remain lost in the forest. Game Over.")
    elif choice == "2":
        print("\nThe wolf is too strong. You lose. Game Over.")
    else:
        right_path()


start()
