
#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 4 Exercise 1

#PART A: Iterative Function

def func(arg1, arg2, arg3):
    out=['{} from {} lives in {}'.format(arg1[0],arg3[0],arg2[0])]
    for i in range(1,len(arg1)):
        out.append('{} from {} lives in {}'.format(arg1[i],arg3[i],arg2[i]))
    return out

output = func( ["Ahmed", "John", "Zina"], ["Dubai", "Sharjah", "Al Ain"], 
    ["COE", "CMP", "ELE"] )
print(output)

#PART B: Recursive Function
def func(arg1,arg2,arg3):
    if len(arg1) == 0:
        return []
    out = ['{} from {} lives in {}'.format(arg1[0],arg3[0],arg2[0])]
    out =  out+func(arg1[1:],arg2[1:],arg3[1:])
    return out

output = func( ["Ahmed", "John", "Zina"], ["Dubai", "Sharjah", "Al Ain"],["COE", "CMP", "ELE"] )
print(output)

#PART C: Zip Function
def func(arg1,arg2,arg3):
    out = []
    for name, place, major in zip(arg1,arg2,arg3 ):
        out.append('{} from {} lives in {}'.format(name,major,place))
    return out

output = func( ["Ahmed", "John", "Zina"], ["Dubai", "Sharjah", "Al Ain"], 
    ["COE", "CMP", "ELE"] )
print(output)
