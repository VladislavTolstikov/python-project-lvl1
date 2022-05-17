#!/usr/bin/env python3
"""Game of checking even."""


from brain_games.brain_engine import play
from brain_games.games import brain_even


def main():
    """Script to launch even game."""
    play(brain_even)


if __name__ == '__main__':
    main()
