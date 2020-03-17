from functools import reduce

def selectionSort(arr):
    for i in range (len(arr)-1): #len and range in one line
        minIndex=reduce(lambda x,y: arr.index(min(arr[i:])),arr) #reduce helps compare values from arr and stores in Minindex
        if minIndex != i:
            arr[i],arr[minIndex]=arr[minIndex],arr[i] #parallel swap
    return arr            

    
# some error in logic, works fine for any list, but not for duplicates ie: l=[5,8,7,2,5,6,3,5,2,4,6,99,0]  
    
    
