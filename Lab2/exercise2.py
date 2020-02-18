#Authors Abdullah Khan, Asif Rasheed
#Programming Languages (CMP 321) Lab 2 Exercise 2

#PART A
integer = 314159265358979
str_int= str(integer)
j = len(str_int);
list = []

#slices the string into pairs of 3 from right
for i in range(len(str_int)-3,-1,-3):
    list.append(str_int[i:j])
    j=i

#if the length of integer not a multiple of 3 then:
if len(str_int)%3!=0:
    list.append(str_int[0:j])

list.reverse()
out = '-'.join(list)
print(out)

#PART B
def phone(num, format):
    #Converts the given number to given format
    if((not isinstance(num,int))or(not isinstance(format,str))):
        print('Type Mismatch!')

    pairs = format.split('+')
    j = 0
    key = str(num)
    out = []
    for i in pairs:
        out.append(key[j:j+int(i)])
        j+=int(i)
    print('-'.join(out))

phone(971506455734,"3+2+3+4")
phone(33109758351,"2+1+2+2+2+2")
phone(918966428361,"2+3+7")
