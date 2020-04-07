#CMP 321 Lab 8 Exercise 2
#Authors Abdullah Khan, Asif Rasheed
import csv
import urllib.request

import urllib;from urllib.request import urlopen

# Part a
url="https://sketchengine.co.uk/wp-content/uploads/word-list/english/english-word-list-total.csv"

lst = []

try:
    for line in urlopen(url):
        lst.append(line.decode('utf8'))
except urllib.error.URLError:
    print("Error: Check the url")

for i in range(4): lst.pop(0) # Ignoring the first 4 lines

words = [] # List of words
for lines in lst:
    words.append(lines.split(";")[1])

print("Top 20 Most Popular Words: ")

for i in range(20): print(i+1,".'",words[i],end="' - ")
