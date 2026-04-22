import string
import random

#validation of the password
def f(password):
    global n, sp, sa
    has_digit = has_punct = has_letter = False
    
    for element in password:
        if element in n:
            has_digit = True
        elif element in sp:
            has_punct = True
        elif element in sa:
            has_letter = True
            
    return has_digit and has_punct and has_letter

n = list(map(str,range(0,10)))  # numbers
sp = list(string.punctuation)   # punctuations
sa = list(string.ascii_letters) # letters(capital & small letters) 
s = n + sp + sa # all symbols


# getting the length of the password from the user
while True:
    length = int(input("Enter password length (minimum 8): "))
    if length >= 8:
        break
    print("Length must be at least 8.")

x = ''
r = ['"',',','.','/','|','[',']','{','}','~','`','=','>','<',';',':','?','\\',]
for j in r:
    s.remove(j)


# creating a password consisting of random symbols
while True:

    for i in range(length):
        x += random.choice(s)
    
    # checking if the password is valid
    '''Valid password should consist of
       letters, numbers, and punctuations!!!'''
    if f(x) == True:
        break
    else:
        x = ''

#printing the result
print(x)
