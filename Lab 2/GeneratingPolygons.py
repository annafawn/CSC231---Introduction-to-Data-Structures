import math, csv

class RegularPolygon:
    def __init__(self, num_sides,side_length):
        self.num_sides = int(num_sides)
        self.side_length = float(side_length)
    def compute_perimeter(self):
        return round(self.num_sides * self.side_length, 2)

class EquilaterialTriangle(RegularPolygon):
    def get_class(self):
        return 'EquilateralTriangle'
    def compute_area(self):
        return round(math.sqrt(3)/4 * (self.side_length)**2, 2)

class Square(RegularPolygon):
    def get_class(self):
        return 'Square'
    def compute_area(self):
        return round((self.side_length)**2, 2)

polygons = []

with open('polygons.csv') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        num_sides = row[0]
        side_length = row[1]
        if num_sides == '3':
            tri = EquilaterialTriangle(num_sides, side_length)
            polygons.append(tri)
        elif num_sides == '4':
            sqr = Square(num_sides, side_length)
            polygons.append(sqr)
        else:
            print('Invalid number of sides')

for i in polygons:
    print(i.get_class(), i.num_sides, i.side_length, i.compute_perimeter(), i.compute_area())