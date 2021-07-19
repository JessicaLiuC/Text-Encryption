import random 
import numpy as np

def ask():
    type = input("Which type of encryption would you like? Please enter the number: 1. Caesar Cipher 2. Vigenere Cipher 3. Railfence Cipher")
    if int(type) == 1:
        return caesar() 
    elif int(type) == 2:
        return vig()
    elif int(type) == 3:
        return rail()
    else:
        print("Please enter the number")
        return ask()
    
def caesar():
    text = input("Please type down the content you want to encrypt: ")
    num = input("Please enter the number for shifting: ")
    encr_text = ""
    for i in range(len(text)):
        #check if the alphebat is capital or lowercase
        if ord(text[i]) <= 90 and ord(text[i]) >= 65:
            new = ord(text[i])+ int(num)
            if new > 90 or new <65:
                encr_text += chr(new-90+64)
            else:
                encr_text += chr(new)
        elif ord(text[i]) <= 122 and ord(text[i]) >= 97:
            new = ord(text[i]) + int(num)
            if new > 122 or new < 97:
                encr_text += chr(new-122+96)
            else:
                encr_text += chr(new)
        else:
            encr_text += text[i]
    print("Here is your encrypted message: " + encr_text)
    return encr_text

def vig():
    text = input("Please type down the content you want to encrypt: ")
    key = input("Please enter the Cipher key: ")
    encr_text = ""

    key_list = list(key)
    j = 0
    for i in range(len(text)):
        key_word = j%len(key_list)
        if ord(text[i]) <= 90 and ord(text[i]) >= 65:
            new = ((ord(text[i])-65) + (ord(key_list[key_word])-65))%26
            encr_text += chr(new +65)
            j += 1
        elif ord(text[i]) <= 122 and ord(text[i]) >= 97:
            new = ((ord(text[i])-97) + (ord(key_list[key_word])-65))%26
            encr_text += chr(new +97)
            j+= 1
        else:
            encr_text += text[i]

    print("Here is your encrypted message: "+ encr_text)
    return encr_text
        
def rail():
    text = input("Please type down the content you want to encrypt: ")
    text = text.strip()
    text = text.replace(" ","")

    one, two, three = {}, {}, {}
    encr_text = ""
    #put element into dictionary first
    for i in range(len(text)):
        if len(text[:i]) % 4 == 0:
            ind4 = len(text[:i]) // 4
            one[ind4] = text[i]
        elif len(text[:i]) % 2 == 1:
            ind2 = len(text[:i]) // 2
            two[ind2] = text[i]
        elif len(text[:i]) % 4 == 2:
            ind3 = len(text[:i]) // 4
            three[ind3] = text[i]

    num1, num2, num3 = one.keys(), two.keys(), three.keys()
    count = 0

    for i in num1:
        encr_text += one.get(i)
    for i in num2:
        encr_text += two.get(i)
    for i in num3:
        encr_text += three.get(i)

    print("Here is the encryption: "+encr_text)
    return encr_text

ask()


