# CMP321 PROGRAMMING LANGUAGES LAB 6
# AUTHORS ABDULLAH KHAN, ASIF RASHEED
from functools import reduce
from operator import add
# Part A
class TempConvert:
    def convertCelsius(self, fahTemp:float) -> float:
        return round(((fahTemp-32)*(5.0/9.0)),3)

tempFah = [50.45,60.0,75.50,90.0]
    #Converting temperature using map
tempCel = list(map(TempConvert().convertCelsius,tempFah))
print(tempCel)

# Part B
    #Converting temperature using lambda expression
print(list(map(lambda i:TempConvert().convertCelsius(i),tempFah)))
    #Converting temperature using list comprehension
print([TempConvert().convertCelsius(x) for x in tempFah])
    #finding the average temperature using reduce
avg = reduce(add,tempCel)/len(tempCel)
print(avg)
    # Calculating list that consists of (xi – avg)2
lst = [(lambda i: (i-avg)**2)(x) for x in tempCel]
print(lst)
    #Finding standard deviation using reduce
sdev = (reduce(add,lst)/(len(tempCel)-1))**(1/2)
print(sdev)
    #Filtering negative temperatures
print(list(filter(lambda i: i<0,tempCel)))
