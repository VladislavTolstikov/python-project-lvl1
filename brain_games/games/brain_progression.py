"""Game with progression."""


from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def fill_progression():
    first = 0
    plus = 0
    first = randint(1, 1000)
    plus = randint(1, 25)
    progression = [0 for x in range(0, 10)]
    progression[0] = first
    for index in range(1, 10):
        progression[index] = progression[index - 1] + plus
    return progression


def generate_question():
    """Define progression game logic."""
    blank_index = 0
    question_string = ''
    answer = 0
    blank_index = randint(0, 9)
    progression = fill_progression()
    answer = progression[blank_index]
    progression[blank_index] = '..'
    question_string = ' '.join(str(e) for e in progression)
    return (str(answer), question_string)
