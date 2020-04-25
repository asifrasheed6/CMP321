# Programming Languages (CMP321) Lab 10 Exercise 2
# Authors: Abdullah Khan, Asif Rasheed

def Formula(expression):
    def constructor(self, args, exp = expression):
        for arg in args.split(', '):
            var, val = arg.split('=')
            setattr(self,var,val)
        self.exp = exp
    def calc(self):
        return eval(''.join([getattr(self,var,None) if var.isalpha() and not getattr(self,var,None) is None else var for var in self.exp[:]]))
    NewClass = type ('Expression',(object,),
    {'exp':expression,'__init__': constructor,'calc':calc})
    return NewClass

# Example 1
triangle_hypotenuse = Formula('(a*a + b*b)**0.5')
print(triangle_hypotenuse('a=3, b=4') .calc())

# Example 2
from math import pi
PI = pi
cylinder_volume = Formula('PI * r**2 * h')
print(cylinder_volume('r= 1, h=2') .calc())
print(cylinder_volume('r= 2.222, h=3') .calc())

# Example 3
print(Formula(input('Formula: '))(input('Variables: ')).calc())
