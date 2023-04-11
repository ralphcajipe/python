# Cookie Jar

class Jar:
    """A simple attempt to represent a cookie jar."""

    def __init__(self, capacity=12):
        """
        The function __init__() initializes the class with a capacity of 12
        which is optional.

        :param capacity: the maximum number of items that can be stored in the
        parameter
        """
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        """
        Returns a string of cookie emojis, where the number of emojis
        is equal to the size of the cookie.

        :return: The string "🍪" is being returned.
        """
        return "🍪" * self._size

    def deposit(self, n):
        """
        This lets you add n cookies to the jar. If adding that many would
        exceed the cookie jar's capacity, instead raise a ValueError.

        :param n: the number of cookies to deposit
        """
        if self._size + n > self._capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        """
        This lets you remove n cookies from the cookie jar.
        If there aren't that many cookies in the cookie jar,
        instead raise a ValueError.

        :param n: the number of cookies to withdraw
        """
        if self._size < n:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
