"""The launcher."""

import prompt


TRIES = 3


def play(game):
    """ Main prints and stuff for games."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    for counter in range(0,TRIES):
        correct_answer, question = game.generate_question()
        print(game.DESCRIPTION)
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(. Correct answer was"
                  "'{1}'.".format(user_answer, correct_answer)
                  )
            print("Let\'s try again, {0}!".format(name))
            break
    else:
        print('Congratulations, {0}!'.format(name))
