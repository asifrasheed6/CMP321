#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 5 Exercise 1

from collections import namedtuple
Point = namedtuple('Point', ['name', 'x', 'y'])

# Exception Classes:
class ExistingPointError(Exception):
	pass
class ArgumentsException(Exception):
	pass
class PointNotFoundError(Exception):
	pass

class Polygon:
    # Constructor
	def __init__(self,*args):
		try:
			if len(args)<3:
				raise ArgumentsException # If number of points less than 3
			self.points = []
			for pt in args:
				self.setPoint(pt)
		except ArgumentsException:
			print('Polygon requires 3 points')
	
    # Setter function
	def setPoint(self,pt):
		try:
			if pt in self.points: # Checks for duplicates
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
		return str(self.points)

	# Equality operator
	def __eq__(self, other):
		for point in other.points:
			if point in self.points:
				return True
		return False

p = Polygon( ('A',5,0), ('B',10,5), ('C',5,10), ('D',-2,8) )
print(p)
