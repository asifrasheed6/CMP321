#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 3 Exercise 1

def mult(left,right):
    #Matrix multiplication
    if len(left[0]) != len(right):
        print('Exception Thrown!\nMatrix size donot match')
        exit(0)
    
    result = []
    for i in range(len(left)):
            rows = []
            for j in range(len(right[0])):
                rows.append(0)
            result.append(rows)
    print(result)

    for i in range(len(left)):
        for j in range(len(right[0])):
            for k in range(len(right)):
                result[i][j]+= left[i][k]*right[k ][j]
r = [[1,2],[2,1]]
p = [[1,2],[2,1]]
mult(r,p)
