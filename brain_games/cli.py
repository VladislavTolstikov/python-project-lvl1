"""Function to read name of user and greet him."""


import sys
from random import choice, randint

import prompt


def checker(num):
    if num % 2 == 0:
        return 'yes'

    return 'no'


def welcome_user():
    name = ''
    print('Welcome to Brain Games!')
    name = prompt.string('May I have your name?')
    if name.isalpha() is False:
        print('That`s not a name!')
        sys.exit()
    else:
        print('Hello,{0}!'.format(name))
        return name


def wrong_answer(name, your_answer, correct_answer):
    print("\'{0}\' is wrong answer ;(. Correct answer was"
          "\'{1}\'.".format(your_answer, correct_answer),
          )
    print("Let\'s try again, {0}!".format(name))


def even_game():
    name = welcome_user()
    number = 0
    even_answer = ''
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    counter = 0
    while counter < 3:
        number = randint(0, 9999)  # nqa:WPS432
        print('Question: {0}'.format(number))
        even_answer = prompt.string('Your answer:')
        if checker(number) == even_answer:
            print('Correct!')
            counter = counter + 1
        else:
            wrong_answer(name, even_answer, checker(number))
            break
    else:
        print('Congratulations,{0}!'.format(name))


def calc_game():
    name = welcome_user()
    question = ''
    operand_one = 0
    operand_two = 0
    operation = ''
    counter = 0
    solution = ''
    user_answer = ''
    operands = ['+', '-', '*']
    while counter < 3:
        operand_one = randint(1, 15)  # nqa:WPS432
        operand_two = randint(1, 15)  # nqa:WPS432
        operation = choice(operands)
        question = str(operand_one) + operation + str(operand_two)
        solution = eval(question)
        print('Question: {0}'.format(question))
        user_answer = input('Your answer:')
        if int(user_answer) == int(solution):
            print('Correct!')
            counter += 1
        else:
            wrong_answer(name, user_answer, solution)
            break
    else:
        print('Congratulations,{0}!'.format(name))


def gcd_game():
    name = welcome_user()
    counter = 0
    answer = 0
    user_answer = 0
    operand_one = 0
    operand_two = 0
    while counter < 3:
        operand_one = randint(1, 100)  # nqa:WPS432
        operand_two = randint(1, 100)  # nqa:WPS432
        print('Question: {0} {1}'.format(operand_one, operand_two))
        while operand_one != 0 and operand_two != 0:
            if operand_one > operand_two:
                operand_one %= operand_two
            else:
                operand_two %= operand_one
        answer = operand_one + operand_two
        user_answer = input('Your answer:')
        if int(user_answer) == answer:
            print('Correct!')
            counter += 1
        else:
            wrong_answer(name, user_answer, answer)
            break
    else:
        print('Congratulations,{0}!'.format(name))
