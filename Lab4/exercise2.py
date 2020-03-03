#PART A
def enum(arg):
    li = list(range(len(arg)))
    return list(zip(li,arg))

output = enum( ['A', 'B', 'C'] )
print(output)

#PART B
def enum(arg, start=0, step=1): #Start is 0 and Step is 1 by default
    li = list(range(start,start+(len(arg)*step),step))
    return list(zip(li,arg))

output = enum( ['A', 'B', 'C'], 5 )
output2 = enum( ['A', 'B', 'C'], 4, 2 )
print(output)
print(output2)
