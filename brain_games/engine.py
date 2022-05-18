"""The launcher."""

import prompt


TRIES = 3


def play(game):
    """ Main prints and stuff for games."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    counter = 0
    while counter < TRIES:
        correct_answer, question = game.generate_question()
        print(game.DESCRIPTION)
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was"
                  "'{1}'.".format(user_answer, correct_answer)
                  )
            print("Let\'s try again, {0}!".format(name))
            break
    else:
        print('Congratulations, {0}!'.format(name))
