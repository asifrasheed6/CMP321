# CMP321L PROGRAMMING LANGUAGES LAB 6 EXERCISE 2
# AUTHORS ABDULLAH KHAN, ASIF RASHEED

    # PART A: literal conversion of the code
def selectionSort(arr):
      for i in range(len(arr)-1):
            minIndex = i
            for j in range(i+1,len(arr)):
                  if arr[j] < arr[minIndex]:
                        minIndex = j
            if minIndex != i:
                  tmp = arr[i]
                  arr[i] = arr[minIndex]
                  arr[minIndex] = tmp

lst = [5,3,4,1,2]
selectionSort(lst)
print(lst)

    # PART B: conversion using python features
from functools import reduce

def selectionSort(args):
    for i in range(len(args)-1):
        min = reduce(lambda x,y: x if args[x]<args[y] else y, list(range(i+1,len(args))))
        if args[min]<args[i]:
           args[i],args[min] = args[min],args[i]

lst = [5,3,4,1,2]
selectionSort(lst)
print(lst)
