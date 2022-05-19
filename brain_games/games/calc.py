"""The calculator game."""

from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    """No arguments needed. Returns question and correct answer."""
    number1 = randint(1, 15)
    number2 = randint(1, 15)
    operation = choice(['+', '-', '*'])
    question = str(number1) + operation.center(3) + str(number2)
    if operation == '+':
        answer = number1 + number2
    elif operation == '-':
        answer = number1 - number2
    elif operation == '*':
        answer = number1 * number2
    return (str(answer), question)
