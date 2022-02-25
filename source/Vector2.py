"""Vector2."""
import math


class Vector2():
    """
    2D Vector object.

    :param __values: float[2+] representing values of vector
    :param __magnitude: float representing length of vector
    :param __angle: float representing angle of vector from +x axis (radians)
    """

    def __init__(self, valuesInit=[0, 0]):
        """
        Initialize.

        :param valuesInit: Initial values for vector
        """
        self.__values = valuesInit
        self.__magnitude = self.__calculateMagnitude()
        self.__angle = self.__calculateAngle()

    def __calculateMagnitude(self):
        return sum([x**2 for x in self.__values]) ** .5

    def __calculateAngle(self):
        return math.atan2(self.__values[1], self.__values[0])

    # Magic methods
    def __add__(self, other):
        """Add another Vector2."""
        if (type(other) == type(self)):
            return Vector2(
                [x+y for x, y in zip(self.__values, other.__values)])
        else:
            raise TypeError("Cannot add vector to scalar")

    def __sub__(self, other):
        """Subtract another Vector2."""
        self.__add__(self.__mul__(-1))

    def __mul__(self, other):
        """Multiply by scalar."""
        try:
            int(other)  # Check numeric
            return Vector2([x * other for x in self.__values])
        except ValueError:
            raise TypeError("Cannot multiply vector")

    def __str__(self):
        """Represent as String."""
        return self.__values

    # Accessors
    def getValues(self):
        """Get current values."""
        return self.__values

    def setValues(self, newValues):
        """Set new values."""
        self.__values = newValues
        self.__angle = self.__calculateAngle()
        self.__magnitude = self.__calculateMagnitude()

    def getPolar(self):
        """Get vector in polar form."""
        return (self.__magnitude, self.__angle)
