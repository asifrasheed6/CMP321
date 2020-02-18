#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 2 Exercise 1

#PART A
nameList = ["Abdulla mhd zayed", "rashid asif", "john elton rowan smith", "Ali Rami"] 

for name in nameList:
    seperated = name.split(' ') #Splits name into first name, middle name (if any) and last name
    print(seperated[0][0].upper()+seperated[-1][0].upper())#Prints first letter of first name and first letter of last name in upper case

#PART B
string = 'Welcome to UAE. uae are awsome, right?'
count = string.upper().count('UAE') #Counts the number of occurences of UAE
print('UAE occurs {} times in "{}"'.format(count,string))

#PART C
list = [1,2,3,4,5,6,7,8]
min = 4
max = 6
sublist = [x for x in list if (min<=x<=max)] #creates a sublist of list with elements between min and max (upper limit and lower limit included)
print('Number of elements between {} and {} in list {} are'.format(min,max,list),len(sublist))
