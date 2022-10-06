def validate_string(string: str):
    """Raises an exception if a string is None or empty"""
    if string is None or string == "":
        raise Exception("Invalid/empty string")

    return string


def ordinal(number: int):
    """Takes an integer and turns it into an ordinal string."""
    if number < 0:
        raise Exception("Int less than zero")

    if number == 0:
        return "0"

    return str(number) + {1: 'st', 2: 'nd', 3: 'rd'}.get(4 if 10 <= number % 100 < 20 else number % 10, "th")
