# txt list
import random

n = open("statsNumbers.txt", "w")

for i in range(1000):
    n.write(str(random.randint(1, 100)) + '\n')

n.close()


# coordinate list
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Coordinate({0.x:d}, {0.y:d})'.format(self)



#x, y are the base value for each coordinate, n is how many
def generate_coordinates(x, y, n):
    coordinates = []
    for i in range(n):
        c = Coordinate(x + random.randrange(-3, 3), y + random.randrange(-3, 3))
        coordinates.append(c)
    return coordinates

#generate_coordinates(x, y, n)

# for x in range(len(coordinates)):
#     print (coordinates[x])



