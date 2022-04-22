"""The even game."""


from brain_games.brain_engine import generate_number


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    """Define even game logic."""
    question = generate_number()
    if question % 2 == 0:
        answer = 'yes'
        return (answer, question)
    answer = 'no'
    return (answer, question)
