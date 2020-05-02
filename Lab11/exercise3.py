# Programming Languages Lab (CMP321L)
# Lab 11 Exercise 3
# Authors Asif Rasheed, Abdullah Khan
import re

file = open('Lab11-InputFile-Markdown.txt', 'r', encoding ='unicode_escape').read()
file = re.sub(r'(.+)(\n==+)',r'<h1>\1</h1>',file)
file = re.sub(r'(.+)(\n--+)',r'<h2>\1</h2>\n',file)
file = re.sub(r'(\n###)(([\s]|[\w]|[\d])+)(\n)',r'<h3>\2</h3>',file)
file = re.sub(r'(\n#)(([\s]|[\w]|[\d])+)(#\n)',r'<h1>\2</h1>',file)
file = re.sub(r'(\n##)(([\s]|[\w]|[\d])+)(##\n)',r'<h2>\2</h2>',file)
file = re.sub(r'(\n###)(([\s]|[\w]|[\d])+)(###\n)',r'<h3>\2</h3>',file)
file = re.sub(r'(\n)((\d\..+\n)+)',r'<ol>\n\2</ol>',file)
file = re.sub(r'([1-9]\.)(.+)',r'<li>\2</li>\n',file)

file = re.sub(r'(\n)(([\+\-\*].+\n)+)',r'<ul>\n\2</ul>\n',file)
file = re.sub(r'([\+\-\*])(.+)',r'<li>\2</li>\n',file)

print(file)
