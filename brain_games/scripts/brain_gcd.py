#!/usr/bin/env python3
"""The GCD game."""


from brain_games.brain_engine import common
from brain_games.games import brain_gcd


def main():
    """Script to launch greates commmon divider game."""
    common(brain_gcd)


if __name__ == '__main__':
    main()
