"""Game with progreesion."""


from random import randint


def prog_game():
    """Define progression game logic."""
    first = 0
    plus = 0
    blank_index = 0
    question_string = ''
    answer = 0
    first = randint(1, 1000)  # noqa:WPS432, S311
    plus = randint(1, 25)  # noqa:WPS432, S311
    blank_index = randint(0, 9)  # noqa:WPS432, S311
    prog = [0 for x in range(0, 10)]
    prog[0] = first
    for index in range(1, 10):
        prog[index] = prog[index - 1] + plus
    answer = prog[blank_index]
    prog[blank_index] = '..'
    question_string = ' '.join(str(e) for e in prog)
    return [answer, question_string]
