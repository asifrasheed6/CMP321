#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 1 Exercise 3

grades = [40, 86.5 , 67.8, 55, 43.7, 85] #list of grades
grades.extend([96,71]) #Adds grades 96 and 71 to the list

grades.sort()

print('Sorted Grades: ', grades)

fails = [i for i in grades if i<=59] #Extracting fail grades to a new list

print('Fail Grades: ')
for i in fails:
	print(i)

