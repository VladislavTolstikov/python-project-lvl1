"""The launcher."""


import sys

import prompt
from brain_games.games.brain_calc import calc_game
from brain_games.games.brain_even import even_game
from brain_games.games.brain_gcd import gcd_game
from brain_games.games.brain_prime import prime_game
from brain_games.games.brain_progression import prog_game


def wrong_answer(name, your_answer, correct_answer):
    """Print of incorrect answer message.

    Arguments:
    name -- user name
    your_answer -- user`s answer
    correct_answer -- the correct answer
    """
    print("'{0}' is wrong answer ;(. Correct answer was"
          "'{1}'.".format(your_answer, correct_answer),
          )
    print("Let\'s try again, {0}!".format(name))


def common(game):
    """ Main prints and stuff for games."""
    result = []
    counter = 0
    name = ''
    user_answer = ''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    if name.isalpha() is False:
        print('That`s not a name!')
        sys.exit()
    else:
        print('Hello, {0}!'.format(name))
    while counter < 3:
        if game == 'even':
            result = even_game()
            if counter == 0:
                print('Answer "yes" if the number is even,'
                      'otherwise answer "no".'
                      )
            print('Question: {0}'.format(result[1]))
            user_answer = prompt.string('Your answer:')
        elif game == 'calc':
            result = calc_game()
            if counter == 0:
                print('What is the result of the expression?')
            print('Question: {0}'.format(result[1]))
            user_answer = input('Your answer:')
            user_answer = int(user_answer)
        elif game == 'gcd':
            result = gcd_game()
            if counter == 0:
                print('Find the greatest common divisor of given numbers.')
            print('Question: {0} {1}'.format(result[1], result[2]))
            user_answer = input('Your answer:')
            user_answer = int(user_answer)
        elif game == 'progression':
            result = prog_game()
            if counter == 0:
                print('What number is missing in the progression?')
            print('Question: {0} '.format(result[1]))
            user_answer = input('Your answer:')
            user_answer = int(user_answer)
        elif game == 'prime':
            result = prime_game()
            if counter == 0:
                print('Answer "yes" if given number is prime.'
                      ' Otherwise answer "no".',
                      )
            print('Question: {0} '.format(result[1]))
            user_answer = input('Your answer:')

        if user_answer == result[0]:
            print('Correct!')
            counter += 1
        else:
            wrong_answer(name, user_answer, result[0])
            break
    else:
        print('Congratulations, {0}!'.format(name))
