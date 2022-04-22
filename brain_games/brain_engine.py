"""The launcher."""


import sys
from random import randint

from brain_games.cli import get_user_answer, welcome_user


def generate_number():
    """Random number generator."""
    return randint(1, 100)


def check_answer(name, your_answer, correct_answer):
    """Print of incorrect answer message.

    Arguments:
    name -- user name
    your_answer -- user`s answer
    correct_answer -- the correct answer
    """
    if your_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print("'{0}' is wrong answer ;(. Correct answer was"
              "'{1}'.".format(your_answer, correct_answer)
              )
        print("Let\'s try again, {0}!".format(name))
        return False


def common(game):
    """ Main prints and stuff for games."""
    counter = 0
    name = welcome_user()
    while counter < 3:
        correct_answer, question = game.generate_question()
        print(game.DESCRIPTION)
        print('Question: {0}'.format(question))
        user_answer = get_user_answer()
        res = check_answer(name, user_answer, correct_answer)
        if not res:
            sys.exit()
        counter += 1
    else:
        print('Congratulations, {0}!'.format(name))
