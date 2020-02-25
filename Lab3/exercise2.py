list=[(10,8,12),(111,64,45),(11,22,33),(44,55,66),(77,88,99)]
list.pop()
list.insert(len(list)-1,(99,99,99))
print("  X   Y   Z")
for i in list:
    print("%3d %3d %3d"% (i[0],i[1],i[2]))
    #%3d display an integer and reserve 3 spaces for it
