class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other) -> any:
        if isinstance(other, Distance):
            return Distance((self.km + other.km))

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> any:
        return f"Distance(km={self.km})"

    def __iadd__(self, other) -> any :
        if isinstance(other, Distance):
            self.km += other.km
        return Distance(self.km)

    def __mul__(self, other) -> any:
        if isinstance(other, Distance):
            return Distance(self.km * other.km)

    def __truediv__(self, other: (int, float)):
        return Distance(round(self.km / other.km, 2))

    def __lt__  (self, other) -> any:
        if isinstance(other, Distance):
            return self.km < other.km

    def __gt__(self, other) -> any:
        if isinstance(other, Distance):
            return self.km > other.km

    def __eq__(self, other) -> any:
        if isinstance(other, Distance):
            return self.km == other.km

    def __le__(self, other) -> any:
        if isinstance(other, Distance):
            return self.km <= other.km

    def __ge__(self, other) -> any:
        if isinstance(other, Distance):
            return self.km >= other.km

