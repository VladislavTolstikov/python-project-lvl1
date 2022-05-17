#!/usr/bin/env python3
"""Game with poregression."""


from brain_games.brain_engine import play
from brain_games.games import brain_progression


def main():
    """Script to launch progression game."""
    play(brain_progression)


if __name__ == '__main__':
    main()
