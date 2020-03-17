def selectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        minIndex=i
        for j in range(i+1,n):
            if(arr[j]<arr[minIndex]):
                minIndex=j
        if (minIndex!=i):
            tmp=arr[i]
            arr[i]=arr[minIndex]
            arr[minIndex]=tmp
    return arr 
                
    
