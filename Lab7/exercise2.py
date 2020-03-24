# CMP321L PROGRAMMING LANGUAGES LAB 7 EXERCISE 2
# AUTHORS ABDULLAH KHAN, ASIF RASHEED

from collections import namedtuple
Point = namedtuple('Point', ['name', 'x', 'y'])

# Exception Classes:
class ExistingPointError(Exception):
    pass
class ArgumentsException(Exception):
    pass
class PointNotFoundError(Exception):
    pass
class TypeError(Exception):
    pass

class Polygon:
    # Constructor
    def __init__(self,*args):
        self.points = []
        for pt in args:
            self.setPoint(pt)
    
    # Setter function
    def setPoint(self,pt):
        try:
            for point in self.points:
                if (pt.name == point.name) or (pt.x==point.x and pt.y==point.y): # Checks for duplicates
                    raise ExistingPointError #If there is a duplicate
            self.points.append(pt) # If no duplicates
        except ExistingPointError:
            print('Duplicate point found!')
 
    # Getter function
    def getPoint(self, name):
        try:
            for point in self.points:
                if point.name == name: # Checking if name exist
                    return point # If name exist
            raise PointNotFoundError # If name doesn't exist
        except PointNotFoundError:
            print('Invalid Point Name!')
 
    #Delete function
    def deletePoint(self, name):
        try:
            for i in range(len(self.points)):
                if self.points[i].name == name: # Checking if name exist
                    self.points.pop(i) # Id name exist
                    return
            raise PointNotFoundError # Id name doesn't exist
        except PointNotFoundError:
            print('Invalid Point Name!')
 
    # Returns number of points
    def __len__(self):
        return len(self.points)
 
    # Returns string (to allow print(Polynomial))
    def __str__(self):
        buffer = []
        for point in self.points:
            buffer.append(point.name+': ('+str(point.x)+','+str(point.y)+')')
        return '-> '.join(buffer)

    # Equality operator
    def __eq__(self, other):
        for point in other.points:
            if point in self.points:
                return True
        return False
    
    # Iterator
    def __iter__(self):
        return iter(self.points)

p = Polygon()
p.setPoint(Point('A',0,50))
p.setPoint(Point('B',300,150))
p.setPoint(Point('C',200,100))
for x in p: print(x)
