#!/usr/bin/env python3
"""Game of checking prime."""


from brain_games.engine import play
from brain_games.games import brain_prime


def main():
    """Script to launch prime game."""
    play(brain_prime)


if __name__ == '__main__':
    main()
