"""Function to read name of user and greet him."""

import prompt


def welcome_user():
    name = prompt.string('May I have your name?')
    print('Hello,{}!'.format(name))  # noqa:421
