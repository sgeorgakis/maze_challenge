class Point:

    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def __str__(self):
        return "{0}, {1}".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __hash__(self):
        return (((10 ^ 5) * self.x) + self.y)
