def validate_string(s: str):
    """Raises an exception if a string is None or empty"""
    if s is None or s == "":
        raise Exception("Invalid/empty string")

    return s


def ordinal(n: int):
    """Takes an integer and turns it into an ordinal string."""
    if n < 0:
        raise Exception("Int less than zero")

    if n == 0:
        return "0"

    return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(4 if 10 <= n % 100 < 20 else n % 10, "th")
