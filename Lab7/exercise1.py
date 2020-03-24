# CMP321L PROGRAMMING LANGUAGES LAB 7 EXERCISE 1
# AUTHORS ABDULLAH KHAN, ASIF RASHEED

# Counter Function
def counter():
    count = 0
    while True:
        yield count
        count = count+1

call = counter()

# Testing the counter
print(next(call))
print(next(call))
print(next(call))
print(next(call))

# Enumerate function
def enum(gen, lst):
    return list(zip(gen,lst))

# Testing enumerate function
lst=['cat','dog','rat']
print(enum(counter(),lst))
