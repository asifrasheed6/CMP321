# Programming Languages Lab (CMP321L)
# Lab 11 Exercise 1
# Authors Asif Rasheed, Abdullah Khan
import re

while True:
    number = input('Enter phone number: ')

    if re.search('([(]\d\d\d[)]\s|\d\d\d[-]|[0])([234679]|50|55|56)-\d\d\d\d\d\d\d',number):
        print('The number is valid!')
    else:
        print('Invalid Number!')
