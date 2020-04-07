#CMP 321 Lab 8 Exercise 1
#Authors Abdullah Khan, Asif Rasheed
import random
import string

# Part a
def RandomCipher():
    ret = {}
    for key, val in zip(string.ascii_lowercase, random.sample(string.ascii_lowercase,26)):
        ret[key]=val
    return ret

dic = RandomCipher();

# Part b
def Encode(text):
    ret = []
    for i in range(len(text)):
        if text[i].lower() in string.ascii_lowercase:
            ret.append(dic[text[i].lower()])
        else:
            ret.append(text[i])
    return ''.join(ret)

# Part c
def Decode(text):
    ret = []
    dec = {v: k for k, v in dic.items()}
    for i in range(len(text)):
        if text[i] in string.ascii_lowercase:
            ret.append(dec[text[i]])
        else:
            ret.append(text[i])
    return ''.join(ret)
            
# Testing the functions
text = "hellow, world!"
text = Encode(text);
print("Encoded Text: ",text)
text = Decode(text);
print("Decoded Text: ",text)
# END
