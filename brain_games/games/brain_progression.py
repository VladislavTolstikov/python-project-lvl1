"""Game with progreesion."""


from random import randint


DESCRIPTION = 'WWhat number is missing in the progression?'


def generate_question():
    """Define progression game logic."""
    first = 0
    plus = 0
    blank_index = 0
    question_string = ''
    answer = 0
    first = randint(1, 1000)
    plus = randint(1, 25)
    blank_index = randint(0, 9)
    prog = [0 for x in range(0, 10)]
    prog[0] = first
    for index in range(1, 10):
        prog[index] = prog[index - 1] + plus
    answer = prog[blank_index]
    prog[blank_index] = '..'
    question_string = ' '.join(str(e) for e in prog)
    return (str(answer), question_string)
