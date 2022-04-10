"""The GCD game."""


from random import randint


def gcd_game():
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
    return [answer, o_one, o_two]
