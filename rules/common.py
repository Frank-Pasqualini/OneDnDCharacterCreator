"""
Common functions that don't fit anywhere else.
"""


def validate_string(string: str):
    """
    Raises an exception if a string is None or empty
    :param string: a string to validate
    :type string: str
    :return: The input if it passed validation
    :rtype: str
    """

    if string is None or string == "":
        raise Exception("Invalid/empty string")

    return string


def ordinal(number: int):
    """
    Takes an integer and turns it into an ordinal string
    :param number: An integer
    :type number: int
    :return: An ordinal string
    :rtype: str
    """

    if number < 0:
        raise Exception("Int less than zero")

    if number == 0:
        return "0"

    return str(number) + {1: "st", 2: "nd", 3: "rd"}.get(4 if 10 <= number % 100 < 20 else number % 10, "th")


def mod(number: int) -> str:
    return f"{number:+g}"
