#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 3 Exercise 3
def dic(string):
    r = ''.join([x for x in string if x.isalnum()])
    r = r.upper()

    result = {}

    for char in r:
        if char in result:
            result[char]+=1
        else:
            result[char] = 1
    return result
result = dic('The best programs are written so that computing machines can perform them quickly and so that human beings can understand them clearly. A programmer is ideally an essayist who works with traditional aesthetic and literary forms as well as mathematical concepts, to communicate the way that an algorithm works and to convince a reader that the results will be correct...')

print(result)
