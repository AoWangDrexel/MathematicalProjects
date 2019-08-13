"""
Author: Ao Wang
Date: 08/12/19
Description: Caesar cipher encryption and decryption, also a reverse encryption
"""
# The function reverses the string parameter
def reverse(plain_text):
    cipher_text = ""
    for letter in range(len(plain_text)):
        
        # starts at the end of the string, -1 and moves its way to the left
        cipher_text += plain_text[-1-letter]
    return cipher_text

# The function encrypts the text with a certain key
def caesar_cipher(plain_text, key):
    cipher_text = ""
    
    # loops through each letter of the text
    for letter in plain_text:
        
        # checks if letter is uppercase or lowercase and in the alphabet
        # if not add it as any other character
        if letter.isupper() and (ord(letter) >= ord("A") and ord(letter) <= ord("Z")):
            cipher_text += chr((ord(letter) + key - ord("A")) % 26 + ord("A"))
        elif letter.islower and (ord(letter) >= ord("a") and ord(letter) <= ord("z")):
            cipher_text +=  chr((ord(letter) + key - ord("a")) % 26 + ord("a"))
        else:
            cipher_text += letter
    return cipher_text

# The function returns a dictionary that counts the frequency of the alphabet
def letter_count(text):
    letter_dict = {}
    text = text.upper()
    for letter in text:
        
        # makes sure that spaces are not counted
        if not " " in letter:
            if not letter in letter_dict.keys():
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict

# The function decrypts the cipher by finding the most frequent letter
def decrypt(cipher_text):
    alphabet = []
    
    # storing alphabet in list
    for letter in range(26):
        alphabet.append(chr(ord("A")+letter))
    
    letter_dict = letter_count(cipher_text)
    high = 0
    high_key = ""
    
    # get the most frequent letter
    for keys in letter_dict.keys():
        if letter_dict.get(keys) > high:
            high = letter_dict.get(keys)
            high_key = keys
    
    # gets the key by finding where the most frequent letter is in the alphabet and subtract it 
    # where E is in the alphabet (the most frequent letter)
    break_key = alphabet.index(high_key) - alphabet.index("E")
    
    # if key is negative, add 26
    if break_key <= 0:
        break_key = break_key + 26
    print("The key is: " + str(break_key))
    
    # 26 - by the key reverses the effect of the cipher
    # 26 - key + key = 26 nullifies the effect of the cipher
    return caesar_cipher(cipher_text, 26 - break_key)

# The function prints out all the possibilities of the cipher by testing keys from 0-25
def brute_force(cipher_text):
    for key in range(26):
        print(caesar_cipher(cipher_text, key))
        
print("Welcome to the Caesar Cipher/Breaker!")
choice = input("Would you like to encrypt (e) or decrypt (d): ")
print()
if(choice == "e"):
    text = input("What would you like to encrypt?: ")
    key = int(input("What is the key?: "))
    print()
    print("Plaintext: " + text)
    print("Ciphertext: " + caesar_cipher(text, key))
elif(choice == "d"):
    text = input("What would you like to decrypt?: ")
    print("Ciphertext: " + text)
    print("Plaintext: " + decrypt(text))
else:
    print("Oops there seems to be an error")
print()

# testing
with open("caesar.txt","r") as file:
    f = file.read()
brute_force("Gdkkn sgdqd H gnod xnt zqd njzx")
print()
print(caesar_cipher("Hello there I hope you are okay", -1))
print()
print(decrypt("Gdkkn sgdqd H gnod xnt zqd njzx"))
print()
print(decrypt(f))
