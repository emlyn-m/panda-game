"""Vector2."""
import math


class Vector2():
    """
    2D Vector object.

    :param __values: Values of vector
    :type __values: float[2]
    :param __magnitude: Length of vector
    :type __magnitude: float
    :param __angle: Angle of vector from +x axis (radians)
    :type __angle: float
    """

    def __init__(self, valuesInit=[0, 0]):
        """
        Initialize.

        :param valuesInit: Initial values for vector
        :type valuesInit: float[2]
        """
        self.__values = valuesInit
        self.__magnitude = self.__calculateMagnitude()
        self.__angle = self.__calculateAngle()

    def fromPolar(polarValues):
        x = polarValues[0] * math.cos(polarValues[1])
        y = polarValues[0] * math.sin(polarValues[1])
        return Vector2([x, y])


    def __calculateMagnitude(self):
        return sum([x**2 for x in self.__values]) ** .5

    def __calculateAngle(self):
        return math.atan2(self.__values[1], self.__values[0])

    # Magic methods
    def __add__(self, other):
        """Add another Vector2.

        :type other: Vector2
        :rtype: Vector2
        :raises TypeError: If other is not a Vector2
        """
        if (type(other) == type(self)):
            return Vector2(
                [x+y for x, y in zip(self.__values, other.__values)])
        else:
            raise TypeError("Cannot add vector to scalar")

    def __sub__(self, other):
        """Subtract another Vector2.

        :type other: Vector2
        :rtype: Vector2
        :raises ValueError: If other is not a Vector2
        """
        return self.__add__(self.__mul__(-1))

    def __mul__(self, other):
        """
        Multiply.

        :type other: Scalar OR Vector2
        :rtype: Vector2
        :raises TypeError: If other is not a scalar OR Vector2
        """

        if type(self) == type(other):  # Dot product
            return sum([x*y for x, y in zip(list(self), list(other))])

        try:
            int(other)  # Check numeric
            return Vector2([x * other for x in self.__values])
        except ValueError:
            raise TypeError("Cannot multiply vector")

    def __div__(self, other):
        """Divide by scalar.

        :type other: Scalar
        :rtype: Vector2
        :raises ValueError: If other is not a scalar
        """
        try:
            int(other)
            return self.__mul__(1/other)
        except ValueError:
            raise TypeError("Cannot divide vector")

    def __str__(self):
        """Represent as String."""
        return "(" + ",".join(map(str, self.__values)) + ")"

    def __list__(self):
        """Represent as List."""
        return self.__values

    def __getitem__(self, idx):
        return self.__values[idx]

    def __setitem__(self, idx, val):
        self.__values[idx] = val

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

    def getNormalized(self):
        return self * (1/self.getPolar()[0])
