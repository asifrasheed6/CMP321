#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 3 Exercise 1

def mult(left,right):
    #Matrix multiplication
    if len(left[0]) != len(right):
        print('Exception Thrown!\nMatrix size donot match')
        exit(0)
    
    result = [[0 for i in range(len(left))], [0 for i in range(len(right[0]))]]

    for i in range(len(left)):
        for j in range(len(right[0])):
            for k in range(len(right)):
                result[i][j]+= left[i][k]*right[k ][j]
    return result

A =  [ [1,3,5] , [2,4,6] ]	
B =  [ [10,3] , [6,7] , [4,9] ]
result = mult(A,B)
print(result)
