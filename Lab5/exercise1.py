#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 5 Exercise 1

from collections import namedtuple
import turtle
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

# Draw function, only works with objects of type polygon
def draw_polygon(pol, speed=2, color='black'): # Default speed is 2 and color is black
	try:
		if not isinstance(pol,Polygon):
			raise TypeError
		turtle.speed(speed)
		turtle.color(color)
		turtle.hideturtle()
		origin = pol.points[0]
		turtle.penup()
		turtle.goto(origin.x,origin.y)
		turtle.pendown()
		for point in pol.points:
			turtle.goto(point.x,point.y)
			turtle.write(point.name)
		turtle.goto(origin.x,origin.y)
		turtle.exitonclick()
	except TypeError:
		print('Type Exception Thrown')

p = Polygon( Point('A',150,80), Point('B',150,50), Point('C',5,10), Point('D',-150,50) )
print(p)
q = Polygon( Point('A',150,80), Point('B',150,50), Point('C',5,10), Point('D',-150,50) )
print(p==q)

p.setPoint(Point('A',150,80)) # Throws Exception
p.getPoint('E') # Throws Exception
p.deletePoint('E') # Throws Exception

p.setPoint(Point('E',200,250))
print(p)
k = p.getPoint('E')
print(k)
p.deletePoint('E')
print(p)
print('There are',len(p),'points in p')

draw_polygon(p)
