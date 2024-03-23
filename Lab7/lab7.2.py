import math


class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def magnitude(self):
        return math.sqrt(self.coordinates[0] ** 2 + self.coordinates[1] ** 2 + self.coordinates[2] ** 2)

    def add(self, vector):
        return Vector([self.coordinates[0] + vector.coordinates[0], self.coordinates[1] + vector.coordinates[1],
                       self.coordinates[2] + vector.coordinates[2]])

    def dot_product(self, vector):
        return (self.coordinates[0] * vector.coordinates[0] + self.coordinates[1] * vector.coordinates[1] +
                self.coordinates[2] * vector.coordinates[2])


v1 = Vector([float(input('Enter x coordinate for vector 1:')), float(input('Enter y coordinate for vector 1:')),
             float(input('Enter z coordinate for vector 1:'))])
v2 = Vector([float(input('Enter x coordinate for vector 2:')), float(input('Enter y coordinate for vector 2:')),
             float(input('Enter z coordinate for vector 2:'))])
print('Magnitude of vector 1:', v1.magnitude())
print('Magnitude of vector 2:', v2.magnitude())
print('Addition of vector 1 and 2 is a vector with coordinates:', v1.add(v2).coordinates)
print('Dot product of vector 1 and 2 is a vector with coordinates:', v1.dot_product(v2))
