#Authors Asif Rasheed, Abdullah Khan
#Programming Languages (CMP 321) Lab 1 Exercise 2

#Finding the required sum using for loop and if statements
oddsum = 0;
evensum = 0;

for i in range(1,1001): #1 is a odd number
	if i%2==0:
		evensum+=i
	else:
		oddsum+=i

print('Sum of odd numbers between 1 and 1000: ', oddsum)
print('Sum of even numbers between 1 and 1000: ', evensum)

#Finding the required sum using only for loops
oddsum = 0;
evensum = 0;

for i in range(1,1001,2): #loop for odd numbers
	oddsum+=i

for i in range(2,1001,2): #loop for even numbers
	evensum+=i

print('Sum of odd numbers between 1 and 1000: ', oddsum)
print('Sum of even numbers between 1 and 1000: ', evensum)
