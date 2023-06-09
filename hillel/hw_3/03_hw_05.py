import random


def simple_game():
    for i in range(3):
        user_num = int(input('Insert the number from 1 to 10: '))
        rand_num = random.randint(1, 10)
        if rand_num == user_num:
            print('You won!')
            break
        else:
            if i == 2:
                print('You lose. Game over.')
            else:
                print('You lose. Try again')


simple_game()

