def is_valid_number(value):
    if isinstance(value, float) or isinstance(value, int):
        return True

    if isinstance(value, str):  # if string, check if it can be converted to float
        try:
            float(value)
            return True  # only returns True if statement above does not raise error
        except ValueError:
            raise ValueError("Entered value is not a number!")

    raise TypeError("Only floats and integers allowed")  #

def to_float(new_value):
    if is_valid_number(new_value):
        return float(new_value)

class Vector:
    def __init__(self, *args):  # *args == arbitrary length
        self.data = []
        for arg in args:
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
        data_string = ""
        for i in range(len(self.data)):
            dimension_value = self.data[i]
            data_string = data_string + str(dimension_value)

            if i + 1 is not len(self.data):
                data_string += ", "

        return f"<Vector{self.dim}: {data_string}>"


    def __len__(self):
        return self.dim

    # iv.
    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = to_float(value)

    def __eq__(self, other) -> bool:
        if self.dim == other.dim:
            for v in range(len(self)):
                if self[v] != other[v]:
                    return False
        else:
            return False

        return True

    def copy(self):
        deep_copy = Vector()
        for v in self.data:
            deep_copy.append(v)

        return deep_copy

    def __mul__(self, other):
        rv = self.copy()
        for i in range(len(rv.data)):
            rv[i] = float(rv[i] * other)
        return rv

    def __rmul__(self, other):
        return self * other

    def __add__(self, other):
        rv = self.copy()
        for i in range(len(rv.data)):
            rv[i] = float(rv[i] + other[i])
        return rv

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


v1 = Vector3(10, 20, 30)
v1.x = "69"
print(v1)