"""Game of checking prime."""


from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(question):
    if question <= 1:
        return False
    else:
        flag = 0
        start = 2
        while start ** 2 <= question and flag != 1:
            if question % start == 0:
                flag = 1
            start += 1
        if flag == 1:
            return False
        return True


def generate_question():
    """Define prime game main logic."""
    question = randint(-100, 501)
    if check_prime(question) is True:
        return ('yes', question)
    else:
        return('no', question)