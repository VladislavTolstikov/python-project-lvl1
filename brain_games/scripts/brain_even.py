"""Game of checking even."""

from random import randint

import prompt


def checker(num):
    if num % 2 == 0:
        return 'yes'

    return 'no'


def main():
    name = ''
    number = 0
    user_answer = ''
    print('Welcome to Brain Games!')
    name = prompt.string('May i have your name?')
    print('Hello,{0}!'.format(name))
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    counter = 0
    while counter < 3:
        number = randint(0, 9999)  # nqa:WPS432
        print('Question: {0}'.format(number))
        user_answer = prompt.string('Your answer:')
        if checker(number) == user_answer:
            print('Correct!')
            counter = counter + 1
        else:
            print("\'{0}\'is wrong answer ;(. Correct answer was"
                  " \'{1}\'.".format(user_answer, checker(number)),
                  )
            print("Let\'s try again, {0}!".format(name))
            break
    else:
        print('Congratulations, {0}!'.format(name))
