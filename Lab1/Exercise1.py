#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 1 Exercise 1

a = 5 #The coefficient of x square
b = 6 #The coefficient of x
c = 1 #The Constant

d = (b**2)-(4*a*c)
sqrtd = d**(1/2) #Square root of d

if d>-1:
	print('Solution 1:',((-b+sqrtd)/(2*a)))
	print('Solution 2:',((-b-sqrtd)/(2*a)))
