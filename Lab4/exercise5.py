
#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 4 Exercise 5
#PART A
def accumulator(arg):
    if arg == 0:
        return int(1)
    out = arg * accumulator(arg-1)
    return out

def fact(arg):
    def check(arg):
        return isinstance(arg,int)
    if check(arg):
        return accumulator(arg)

output = fact('s')
output2 = fact(5)
print(output)
print(output2)

#PART B
def T(n):
    #Calculated nCk
    def C(k):
        return fact(n)/(fact(n-k)*fact(k))
    return C
f = T(10)
print(f(3))
print(T(10)(3))
