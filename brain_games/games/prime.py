"""Game of checking prime."""


from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    start = 2
    while start ** 2 <= number:
        if number % start == 0:
            return False
        start += 1
    return True


def generate_question():
    """Define prime game main logic."""
    question = randint(-100, 501)
    answer = 'yes' if is_prime(question) else 'no'
    return (answer, question)