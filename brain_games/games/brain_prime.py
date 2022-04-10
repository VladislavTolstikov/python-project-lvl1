"""Game of checking prime."""


from random import randint


def prime_game():
    """Define prime game main logic."""
    question = randint(4, 501)  # noqa:S311
    flag = 0
    start = 2
    while start ** 2 <= question and flag != 1:
        if question % start == 0:
            flag = 1
        start += 1
    if flag == 1:
        return ['no', question]
    return ['yes', question]
