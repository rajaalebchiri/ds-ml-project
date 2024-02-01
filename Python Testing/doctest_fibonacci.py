"""
This is the "example" module.

The example module supplies one function, fibonacci().  For example,

>>> fibonacci(13)
233
"""

def fibonacci(n):
    """Return the fibonacci of n, an exact integer >= 0.

    >>> [fibonacci(n) for n in range(5)]
    [0, 1, 1, 2, 3]
    >>> fibonacci(30)
    832040
    >>> fibonacci(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> fibonacci(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer

    >>> fibonacci(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    if n in (0,1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()