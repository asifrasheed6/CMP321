#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 2 Exercise 3

file =  open('/home/runner/work/CMP321/CMP321/Lab2/email.txt', 'r', encoding ='unicode_escape').readlines()

for line in file:
    line = line.replace('\n','') #removes new line character
    words = line.split(' ') #splits the line into words
    
    for word in words:
        if '@'in word:
            #If the word is an email address, searches for domains
            valid = False
            
            domains = ['com', 'edu', 'gov', 'org']
            word = word.replace(';','')
            elements = word.split('@')

            for element in elements:
                if '.' in element:
                    key = element.split('.')
                    
                    for domain in domains:
                        if key[-1] in domain:
                            valid = True

            print(word, 'is '+(not valid)*'in'+'valid')

