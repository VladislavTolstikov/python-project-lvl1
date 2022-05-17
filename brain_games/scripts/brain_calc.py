#!/usr/bin/env python3
"""The calculator game."""


from brain_games.brain_engine import play
from brain_games.games import brain_calc


def main():
    """Script to launch even game."""
    play(brain_calc)


if __name__ == '__main__':
    main()
