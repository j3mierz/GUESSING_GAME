from random import randint

win_number = randint(1, 100)

def game():
    while True:
        try:
            user_number = float(input("Guess the number: "))
        except ValueError:
            print("it's not a number")
            continue
        if user_number < win_number:
            print("Too small")
        elif user_number > win_number:
            print("Too big")
        else:
            print("you win!")
            return
game()