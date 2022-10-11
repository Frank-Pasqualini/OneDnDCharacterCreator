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


def calculate_string_width(string: str) -> float:
    """
    Calculate the width of a string when printed in a non monospace font
    https://gist.github.com/aminnj/5ca372aa2def72fb017b531c894afdca
    :param string: the string to find the width of
    :type string: str
    :return: the width of the string
    :rtype: float
    """

    size = 0.0

    widths = {
        " ": 4.4453125,
        "!": 4.4453125,
        '"': 5.6796875,
        "#": 8.8984375,
        "$": 8.8984375,
        "%": 14.2265625,
        "&": 10.671875,
        "'": 3.0546875,
        "(": 5.328125,
        ")": 5.328125,
        "*": 6.2265625,
        "+": 9.34375,
        ",": 4.4453125,
        "-": 5.328125,
        ".": 4.4453125,
        "/": 4.4453125,
        "0": 8.8984375,
        "1": 7.7228125,
        "2": 8.8984375,
        "3": 8.8984375,
        "4": 8.8984375,
        "5": 8.8984375,
        "6": 8.8984375,
        "7": 8.8984375,
        "8": 8.8984375,
        "9": 8.8984375,
        ":": 4.4453125,
        ";": 4.4453125,
        "<": 9.34375,
        "=": 9.34375,
        ">": 9.34375,
        "?": 8.8984375,
        "@": 16.2421875,
        "A": 10.671875,
        "B": 10.671875,
        "C": 11.5546875,
        "D": 11.5546875,
        "E": 10.671875,
        "F": 9.7734375,
        "G": 12.4453125,
        "H": 11.5546875,
        "I": 4.4453125,
        "J": 8,
        "K": 10.671875,
        "L": 8.8984375,
        "M": 13.328125,
        "N": 11.5546875,
        "O": 12.4453125,
        "P": 10.671875,
        "Q": 12.4453125,
        "R": 11.5546875,
        "S": 10.671875,
        "T": 9.7734375,
        "U": 11.5546875,
        "V": 10.671875,
        "W": 15.1015625,
        "X": 10.671875,
        "Y": 10.671875,
        "Z": 9.7734375,
        "[": 4.4453125,
        "\\": 4.4453125,
        "]": 4.4453125,
        "^": 7.5078125,
        "_": 8.8984375,
        "`": 5.328125,
        "a": 8.8984375,
        "b": 8.8984375,
        "c": 8,
        "d": 8.8984375,
        "e": 8.8984375,
        "f": 4.15921875,
        "g": 8.8984375,
        "h": 8.8984375,
        "i": 3.5546875,
        "j": 3.5546875,
        "k": 8,
        "l": 3.5546875,
        "m": 13.328125,
        "n": 8.8984375,
        "o": 8.8984375,
        "p": 8.8984375,
        "q": 8.8984375,
        "r": 5.328125,
        "s": 8,
        "t": 4.4453125,
        "u": 8.8984375,
        "v": 8,
        "w": 11.5546875,
        "x": 8,
        "y": 8,
        "z": 8,
        "{": 5.34375,
        "|": 4.15625,
        "}": 5.34375,
        "~": 9.34375,
    }

    for char in str(string):
        size += widths[char]

    return size
