"""The calculator game."""

import numexpr
from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    """No arguments needed. Returns question and correct answer."""
    operand_one = randint(1, 15)
    operand_two = randint(1, 15)
    operation = choice(['+', '-', '*'])
    question = str(operand_one) + operation.center(3) + str(operand_two)
    answer = numexpr.evaluate(question)
    return (str(answer), question)
