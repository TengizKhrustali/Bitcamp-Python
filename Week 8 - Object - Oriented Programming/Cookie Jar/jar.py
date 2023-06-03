class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer")
        if self.cookies + n > self.capacity:
            raise ValueError("Cookie jar capacity exceeded")
        self.cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer")
        if self.cookies - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self.cookies -= n

    @property
    def size(self):
        return self.cookies

    @property
    def capacity(self):
        return self._capacity


jar = Jar()
jar.deposit(7)
jar.withdraw(1)
print(jar)
