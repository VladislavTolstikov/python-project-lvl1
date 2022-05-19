#!/usr/bin/env python3
"""The GCD game."""


from brain_games.engine import play
from brain_games.games import gcd


def main():
    """Script to launch greates commmon divider game."""
    play(gcd)


if __name__ == '__main__':
    main()
