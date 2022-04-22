"""The calculator game."""


from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    """No arguments needed. Returns question and correct answer."""
    operand_one = randint(1, 15)  # noqa: S311
    operand_two = randint(1, 15)  # noqa: S311
    operation = choice(['+', '-', '*'])  # noqa: S311
    question = str(operand_one) + operation.center(3) + str(operand_two)
    answer = eval(question)  # noqa: WPS421, S307
    return (str(answer), question)
