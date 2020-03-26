# CMP321L PROGRAMMING LANGUAGES LAB 7 EXERCISE 3
# AUTHORS ABDULLAH KHAN, ASIF RASHEED

# PART A
# Checks if the given number is prime or not
def isPrime(n, i=2): return True if i>(n**(1/2)) else False if n%i==0 else isPrime(n,i+1)

# Returns prime number larger than the given argument
def genPrime(i=1):
    while True:
        i+=1
        if isPrime(i): yield i

prime = genPrime()

# The first 20 prime numbers
for i in range(20): print(next(prime), end =' ')
print()

# PART B
lst = [next(prime) for x in range(20)] # next 20 prime numbers using list comprehension
print(lst)

from itertools import islice
lst2 = list(islice(genPrime(1000000),0,20)) # first 20 prime numbers more than 1000000 (the generator generates prime numbers larger than the given argument)
print(lst2)

# iterator using generator expression to print first 100 prime numbers greater than 1million
prime = genPrime(1000000)
iter = (next(prime) for i in range(100))
for i in iter:
    print(i, end=' ')
print()

# Using iterator from previous to make a list of first 100 prime numbers larger than 1million with last 2 digits identical
prime = genPrime(1000000)
iter = (next(prime) for i in range(100))

lst = [i for i in iter if(str(i)[-2]==str(i)[-1])]
print(lst)

# Creating an Prime iterator class
class iterPrime:
    def __init__(self, start=2):
        while not isPrime(start):
            start+=1
        self.current, self.next = start, start+1
        while not isPrime(self.next):
            self.next+=1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        val = self.current
        self.current = self.next
        self.next+=1
        while not isPrime(self.next):
            self.next+=1
        return val
        
print(list(islice(iterPrime(1000000),0,20)))
