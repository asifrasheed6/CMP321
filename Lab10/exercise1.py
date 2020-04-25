# Programming Languages (CMP321) Lab 10 Exercise 1
# Authors: Abdullah Khan, Asif Rasheed

def constructor(self, arg):
    self.no_of_sides = arg
Polygon= type ('Polygon',(object,),{'no_of_sides' :0,
                                    '__init__': constructor,
                                    'getSides':(lambda obj: obj.no_of_sides)})

def addSubClass(arg):
    def triangle(self, num=arg, side1=0, side2=0, side3=0):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def setterSides(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def area(self):
        s =(self.side1+self.side2+self.side3)/2
        ar = (s * (s-self.side1) * (s-self.side2) * (s-self.side3))**(1/2)
        return ar
    def createSubClass(num):
        Triangle = type ('Triangle',(arg,),
        {'no_of_sides' :num, 'side1':0,'side2':0,'side3':0,'__init__': triangle,
        'setSides':setterSides, 'findArea':area})
        return Triangle()
    return createSubClass

def toString(self):
    variables = [var for var in dir(self) if not callable(getattr(self, var)) and not var.startswith("__")]
    var = []
    for i in variables:
        var.append(i+": "+str(getattr(self,i)))
    return '\n'.join(var)
    
def strFix(obj):
    if getattr(obj,'__str__')()==repr(obj):
        type(obj).__str__ = toString

triangle= addSubClass(Polygon)(3)
triangle.setSides(4,5,6)
print(triangle.findArea())

strFix(triangle)
print(triangle)
