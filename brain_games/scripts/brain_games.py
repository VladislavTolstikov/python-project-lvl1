"""first file."""

import sys

import prompt


def main():
    """Needed greeting."""
    name = ''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    if name.isalpha() is False:
        print('That`s not a name!')
        sys.exit()
    else:
        print('Hello, {0}!'.format(name))


if __name__ == '__main__':
    main()
