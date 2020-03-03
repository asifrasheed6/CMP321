
#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 4 Exercise 3
#PART A
def member(key, list):
    if len(list) == 0:
        return False
    if key == list[0]:
        return True
    return member(key,list[1:])

output = member( 2, [1, 3, 5] )
output2 = member( 4, [1, 2, 3, 4, 5] )

print(output)
print(output2)

#PART B
def member(key, list, i=0):
    if i>=len(list):
        return -1
    if key==list[i]:
        return i
    return member(key,list,i+1)

output = member( 2, [1, 3, 5] )
output2 = member( 4, [1, 2, 3, 4, 5] )

print(output)
print(output2)
