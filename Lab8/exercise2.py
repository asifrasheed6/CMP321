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

lst_words = [] # List of words
for lines in lst:
    print(lines)
    words = lines.split(';')
    lst_words.append(words[1])

print(lst_words)
