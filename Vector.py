import math

class Vector2 () :

    def __init__(self, x, y) :

        self.x = x
        self.y = y

    def __add__(self, other) :

        if type(other) == Vector2 :

            x = self.x + other.x
            y = self.y + other.y

        else :

            x = self.x + other
            y = self.y + other

        return Vector2(x, y)
    
    def __mul__(self, other) :

        if type(other) == Vector2 :

            x = self.x * other.x
            y = self.y * other.y

        else :

            x = self.x * other
            y = self.y * other

        return Vector2(x, y)
    
    def __truediv__(self, other) :

        if type(other) == Vector2 :

            x = self.x / other.x
            y = self.y / other.y

        if type(other) == int or type(other) == float :

            x = self.x / other
            y = self.y / other

        return Vector2(x, y)
    
    def __sub__(self, other) :

        if type(other) == Vector2 :

            x = self.x - other.x
            y = self.y - other.y

        else :

            x = self.x - other
            y = self.y - other

        return Vector2(x, y)
    
    def __radd__(self, other) :

        if type(other) == Vector2 :

            x = self.x + other.x
            y = self.y + other.y

        else :

            x = self.x + other
            y = self.y + other

        return Vector2(x, y)

    def __rmul__(self, other) :

        if type(other) == Vector2 :

            x = self.x * other.x
            y = self.y * other.y

        else :

            x = self.x * other
            y = self.y * other

        return Vector2(x, y)
    
    def __rtruediv__(self, other) :

        if type(other) == Vector2 :

            x = self.x / other.x
            y = self.y / other.y

        if type(other) == int or type(other) == float :

            x = self.x / other
            y = self.y / other

        return Vector2(x, y)
    
    def __rsub__(self, other) :

        if type(other) == Vector2 :

            x = self.x - other.x
            y = self.y - other.y

        else :

            x = self.x - other
            y = self.y - other

        return Vector2(x, y)
    
    def __str__(self) :

        return f"{self.x}, {self.y}"
    
    def dot(self, other) :

        return((self.x * other.x) + (self.y * other.y))
    
    def normalise(self, length = 1) :

        new_length = math.sqrt(self.x ** 2 + self.y ** 2)
        division = length / new_length

        self.x *= division
        self.y *= division

    def normalised(self, length = 1) :

        new_length = math.sqrt(self.x ** 2 + self.y ** 2)
        division = length / new_length

        x = self.x * division
        y = self.y * division

        return Vector2(x, y)
    
    def get_normal_line(self, vector) :

        dif_x = vector.x - self.x
        dif_y = vector.y - self.y

        direction_vector = Vector2(-dif_y, dif_x)

        direction_vector.normalise()

        return direction_vector
    
    def get_normal(self, vector) :

        dif_x = vector.x - self.x
        dif_y = vector.y - self.y

        direction_vector = Vector2(dif_x, dif_y)

        direction_vector.normalise()

        return direction_vector
    
    def inverse(self) :

        x = -1 * self.x
        y = -1 * self.y

        return Vector2(x, y)

    def hyp(self) :

        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def rotate90(self) :

        x = self.y
        y = self.x * -1

        return Vector2(x, y)
    
    def rotate270(self) :

        x = self.y * -1
        y = self.x

        return Vector2(x, y)
    
    def dis(self, other) :

        x = self.x - other.x
        y = self.y - other.y

        return Vector2(x, y).hyp()