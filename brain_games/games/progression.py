"""Game with progression."""


from random import randint


DESCRIPTION = 'What number is missing in the progression?'


PROGRESSION_SIZE = 10


def generate_progression():
    first_element = 0
    step = 0
    first_element = randint(1, 1000)
    step = randint(1, 25)
    progression = [0 for x in range(0, PROGRESSION_SIZE)]
    progression[0] = first_element
    for index in range(1, PROGRESSION_SIZE):
        progression[index] = (progression[index - 1] + step)
    return list(map(str, progression))


def generate_question():
    """Define progression game logic."""
    blank_index = 0
    question_string = ''
    answer = 0
    blank_index = randint(0, PROGRESSION_SIZE - 1)
    progression = generate_progression()
    answer = progression[blank_index]
    progression[blank_index] = '..'
    question_string = ' '.join(str(e) for e in progression)
    return (answer, question_string)
