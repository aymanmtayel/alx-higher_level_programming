#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """function to print a text with 2 new lines after sepecific characters

    Args:
        text: string at which there are characters to\
        print the 2 new lines after (., ?, :)

    Raises:
        TypeError: if text is not a string with a custom message
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".:?":
        text = (char + "\n\n").join(
                [line.strip(" ") for line in text.split(char)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
