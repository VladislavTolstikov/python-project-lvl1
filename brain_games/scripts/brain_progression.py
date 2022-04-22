#!/usr/bin/env python3
"""Game with poregression."""


from brain_games.brain_engine import common
from brain_games.games import brain_progression


def main():
    """Script to launch progression game."""
    common(brain_progression)


if __name__ == '__main__':
    main()
