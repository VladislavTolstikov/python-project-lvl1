"""Game with progression."""


from random import randint


DESCRIPTION = 'What number is missing in the progression?'


PROGRESSION_SIZE = 10


def generate_progression():
    first_element = randint(1, 1000)
    step = randint(1, 25)
    progression = []
    progression.append(first_element)
    for index in range(1, PROGRESSION_SIZE):
        progression.append(progression[index - 1] + step)
    return progression


def generate_question():
    """Define progression game logic."""
    blank_index = randint(0, PROGRESSION_SIZE - 1)
    progression = list(map(str, generate_progression()))
    answer = progression[blank_index]
    progression[blank_index] = '..'
    question = ' '.join(e for e in progression)
    return (answer, question)
