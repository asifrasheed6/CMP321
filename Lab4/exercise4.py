
#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 4 Exercise 4
from math import sqrt

def is_odd(arg): return False if arg%2==0 else True

#PART A
def apply_to_all(func, list):
    if len(list) == 0:
        return []

    result = func(list[0])
    out = [result]
    out = out + apply_to_all(func, list[1:])
    return out

output = apply_to_all( sqrt, [4, 9, 16, 25] )
print(output)

#PART B
def apply_select(func, list):
    if len(list) ==0:
        return []
    out = []
    if func(list[0]):
        out.append(list[0])
    out = out+apply_select(func, list[1:])
    return out
output = apply_select( is_odd, [2, 3, 5, 8, 9] )
print(output)
