"""The calculator game."""

import numexpr
from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    """No arguments needed. Returns question and correct answer."""
    number1 = randint(1, 15)
    number2 = randint(1, 15)
    operation = choice(['+', '-', '*'])
    question = str(number1) + operation.center(3) + str(number2)
    answer = numexpr.evaluate(question)
    return (str(answer), question)
