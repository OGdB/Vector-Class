def is_valid_number(value):
    """Return whether the input can be converted to a float"""
    if isinstance(value, float) or isinstance(value, int):
        return True

    if isinstance(value, str):  # if string, check if it can be converted to float
        try:
            float(value)
            return True  # only returns True if statement above does not raise error
        except ValueError:
            raise ValueError("Entered value is not a number!")

    raise TypeError("Only floats and integers allowed") 

def to_float(new_value):
    """Return the value as a float, if possible"""
    if is_valid_number(new_value):
        return float(new_value)

class Vector:
    def __init__(self, *args):  # *args == arbitrary length
        self.data = []

        # If argument is a list of values, (try to) add each value.
        for arg in args:
            if isinstance(arg, list):
                for value in arg:
                    self.data.append(to_float(value))
            else:
                self.data.append(to_float(arg))

        self.dim = len(self.data)

        if self.dim == 2:
            self.__class__ = Vector2
        elif self.dim == 3:
            self.__class__ = Vector3

    def append(self, *args):
        for arg in args:
            self.data.append(float(arg))
        self.dim = len(self.data)

    def __str__(self):
        """Return a string of the vector in the form of '<Vector#: x, y, z, p>: '"""
        data_string = ""
        for i in range(len(self.data)):
            dimension_value = self.data[i]
            data_string = data_string + str(dimension_value)

            if i + 1 is not len(self.data):
                data_string += ", "

        return f"<Vector{self.dim}: {data_string}>"


    def __len__(self):
        """Return the amount of dimensions of this vector"""
        return self.dim

    # iv.
    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = to_float(value)

    def __eq__(self, other):
        """Return whether this vector has the same values as the other"""
        if self.dim == other.dim:
            for v in range(len(self)):
                if self[v] != other[v]:
                    return False
        else:
            return False

        return True

    def copy(self):
        """Return deep copy of this vector"""
        deep_copy = Vector(self.data)

        return deep_copy

    def __mul__(self, other):
        rv = self.copy()
        for i in range(len(rv.data)):
            rv[i] = float(rv[i] * other)
        return rv

    def __rmul__(self, other):
        return self * other

    def __add__(self, other):
        if isinstance(other, type(self)):
            rv = self.copy()
            for i in range(len(rv.data)):
                rv[i] = float(rv[i] + other[i])
            return rv
        else:
            raise TypeError(f"You can only add another Vector{self.dim} to this Vector{self.dim}. (You passed {other}).")  #
            # TypeError: You can only add another 
    # Vector3 to this Vector3 (You passed
    # '5'.)

    def __sub__(self, other):
        rv = self.copy()
        for i in range(len(rv.data)):
            rv[i] = float(rv[i] - other[i])
        return rv

    def __neg__(self):
        return -1 * self

    def __truediv__(self, other):
        rv = self.copy()
        for i in range(len(rv.data)):
            rv[i] = float(rv[i] / other)
        return rv


class Vector2(Vector):
    def __init__(self, x, y):
        super().__init__(x, y)

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, new_x):
        self[0] = new_x

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, new_y):
        self[1] = new_y


class Vector3(Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, new_x):
        self[0] = new_x

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, new_y):
        self[1] = new_y

    @property
    def z(self):
        return self[2]

    @z.setter
    def z(self, new_z):
        self[2] = new_z


# Your Name - Oeds de Boer
# ETGG 1803 Lab #3
# Date Completed - 2/10/2022
# Outside Resources - None
# All your code goes here 

if __name__ == "__main__": 
    a = Vector(1, 2, 3, 4)
    v = Vector(1, 2, 3)
    w = Vector(4, 5, 6)
    z = v + w
    print(a) # <Vector4: 1.0, 2.0, 3.0, 4.0>
    print(z) # <Vector3: 5.0, 7.0, 9.0>
    print("v + 5 =", v + 5) # TypeError: You can only add another 
    # Vector3 to this Vector3 (You passed
    # '5'.)
    q = v - w
    print(q) # <Vector3: -3.0, -3.0, -3.0>
    a = v * -2
    print(a) # <Vector3: -2.0, -4.0, -6.0>
    a = -2 * v
    print(a) # <Vector3: -2.0, -4.0, -6.0>
    b = a + (v + w)
    print(b) # <Vector3: 3.0, 3.0, 3.0>
    d = v + (v + v) + w
    print(d) # <Vector3: 7.0, 11.0, 15.0>
    n = -v
    print(n) # <Vector3: -1.0, -2.0, -3.0>
    s = Vector2(3, -2)
    print(s) # <Vector2: 3.0, -2.0)
    print(s.x) # 3.0
    t = Vector(3, -2)
    print(t) # <Vector2: 3.0, -2.0>
    print(t.y) # -2.0
    print(s == t) # True