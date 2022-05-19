"""The GCD game."""


from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def count_gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 + number2


def generate_question():
    """Define logic of greatest common divider."""
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    answer = count_gcd(number1, number2)
    question = f'{number1} {number2}'
    return (str(answer), question)
