"""The GCD game."""


from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question():
    """Define logic of greatest common divider."""
    operand_one = randint(1, 100)  # noqa:WPS432, S311
    operand_two = randint(1, 100)  # noqa:WPS432, S311
    o_one = operand_one
    o_two = operand_two
    while operand_one != 0 and operand_two != 0:
        if operand_one > operand_two:
            operand_one %= operand_two
        else:
            operand_two %= operand_one
    answer = operand_one + operand_two
    question = f'{o_one} {o_two}'
    return (str(answer), question)
