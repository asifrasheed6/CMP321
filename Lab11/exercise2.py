# Programming Languages Lab (CMP321L)
# Lab 11 Exercise 2
# Authors Asif Rasheed, Abdullah Khan
import re

op = '[\+\-\*\/\%]'
letter = '([a-z]|[A-Z])'
digit = '[0-9]'
numerical_literal = '(\+|\-)'+digit+'+.'+digit+'+'
identifier = letter+'('+letter+'|'+digit+')*'
assignment_statement = '('+identifier+')\=(('+identifier+')|'+'('+numerical_literal + '(('+op+identifier+')|('+numerical_literal+'))*))'

while True:
    assignment = input('Enter Assignment: ')

    if re.search(assignment_statement,assignment):
        print('Valid syntax!')
    else:
        print('Invalid syntax!')
