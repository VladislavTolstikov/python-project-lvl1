#!/usr/bin/env python3
"""The calculator game."""


from brain_games.engine import play
from brain_games.games import calc


def main():
    """Script to launch even game."""
    play(calc)


if __name__ == '__main__':
    main()
