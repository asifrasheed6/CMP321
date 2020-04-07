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

for i, word in zip([str(i+1)+".'" for i in range(20)],words[0:20]): 
	print(i+word,end="' - ")
print()

# Part b
url="http://textfiles.com/100/famous.bug"

lst = []

try:
    for line in urlopen(url):
        lst.append(line.decode('utf8'))
except urllib.error.URLError:
    print("Error: Check the url")

S = "\n".join(lst)

# Part d
word_count = {}

for line in S.split("\n"):
	for word in line.split(): 
	# Would avoid empty character and '\r' (for linux)
		if not word==' ' and not word=="\r":
			if word.lower() in word_count:
				word_count[word.lower()]+=1
			else:
				word_count[word.lower()]=1

word_count = sorted(word_count.items(), key = lambda kv:(kv[1],kv[0]), reverse=True)
for i, word in zip([str(i+1)+".'" for i in range(20)],[i for i,r in word_count[0:20]]):
	print(i+word,end="' - ")
print()
