# reversed Guessing game

print('think of number between 1 and 1000 i will guess it in max 10 tries')


# next number equation
def computer_next_number(a, b):
    return int((b - a) / 2 + a)


# playing loop
def player_guessing():
    max_2 = 1000
    min_2 = 1
    print(computer_next_number(min_2, max_2))
    answer = input()
    while not answer == "you win":

        if answer == 'too small':
            min_2 = computer_next_number(min_2, max_2)
        if answer == 'too big':
            max_2 = computer_next_number(min_2, max_2)

        print(computer_next_number(min_2, max_2))
        answer = input()
    print('I won')
    return


player_guessing()
