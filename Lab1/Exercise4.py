#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 1 Exercise 4

values = [50, 12, 27, 33, 61, 49, 28]
size = len(values)
print('Array Before Bubble Sort: ', values)

for i in range(0, size-1):
	if values[i]>values[i+1]:
		values[i],values[i+1]=values[i+1],values[i] #Swaps the Values

print('Array After Bubble Sort: ', values)	
