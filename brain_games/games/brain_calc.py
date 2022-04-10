"""The calculator game."""


from random import choice, randint


def calc_game():
    """No arguments needed. Returns question and correct answer."""
    operand_one = randint(1, 15)  # noqa: S311
    operand_two = randint(1, 15)  # noqa: S311
    operation = choice(['+', '-', '*'])  # noqa: S311
    question_calc = str(operand_one) + operation.center(3) + str(operand_two)
    solution = eval(question_calc)  # noqa: WPS421, S307
    return [solution, question_calc]
