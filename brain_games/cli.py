"""Command interface of the Brain Games."""

import prompt


def welcome_user():
    """Ask for a user name, and welcome.

    Returns:
        Name of the user.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
