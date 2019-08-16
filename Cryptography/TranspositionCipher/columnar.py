"""
Author: Ao Wang
Date: 08/16/19
Description: Encryption and Decryption of Transposition Columnar Cipher
** Still need to find a way to decipher the encryption w/o a key
"""

import numpy as np
import math
import random

# The function returns a list of the order the letter of the words should be
# alphabetically i.e. ZEBRAS 632415
def order(word):
    
    word_list = []
    # makes the list store each letter of word
    for letter in word:
        word_list.append(letter)
    
    # list from 0 to the length of the word
    order_list = list(range(len(word)))
    
    # create np arrays so it will be possible to order the numbers 
    # the way ZEBRAS was ordered
    letters = np.array(word_list)
    nums = np.array(order_list)
    inds = letters.argsort()
    nums = nums[inds]
    nums = list(nums)
    
    new_nums = list(range(len(nums)))
    n = 0
    for i in nums:
        new_nums[i] = n
        n += 1
    return new_nums

# The function encrypts the plain text with a word
def encrypt(plain_text, key):
    
    # the key is the number of columns in the matrix
    col = key
    ordering = order(col)
    col = len(col)
    
    plain_text = plain_text.replace(" ", "")
    
    # find the number of rows by rounding up the length of the text and num of columns
    row = math.ceil(len(plain_text)/col)
    
    # create a numpy 2D array full of whitespace
    grid = np.full((row, col), " ")
    
    # stores the letters of the plain text in the matrix, if not all filled
    # store in random letters from A - Z
    idx = 0
    for i in range(row):
        for j in range(col):
            if(idx < len(plain_text)):
                grid[i,j] = plain_text[idx]
                idx += 1
            else:
                r = random.randint(ord("A"), ord("Z"))
                grid[i,j] = chr(r)
                
    cipher_text = ""    
    idx = 0
    
    # stores the cipher by the order from the list returned from def order(word)
    while not idx > row:
        i = ordering.index(idx)
        for j in range(row):
            cipher_text += grid[j,i]
        idx += 1

    cipher_text = cipher_text.replace(" ", "")
    print(grid)
    return cipher_text

# The function decrypts the cipher
def decrypt(cipher_text, key):
    
    # similar concepts from the encrypt method
    col = key
    ordering = order(col)
    col = len(col)
    
    row = math.ceil(len(cipher_text)/col)
    grid = np.full((row, col), " ")
    
    idx = 0
    l = 0
    
    # storing back the letters of the cipher in the matrix
    # in the same order from which it came
    while not idx >= col:
        i = ordering.index(idx)
        for j in range(row):
            if l < len(cipher_text):
                grid[j,i] = cipher_text[l]
                l += 1
        idx += 1
    
    # getting the plaintext out
    plain_text = ""
    for i in range(row):
        for j in range(col):
            plain_text += grid[i,j]
    return plain_text

# testing using wikipedia example
# print(decrypt(encrypt("WE ARE DISCOVERED FLEE AT ONCE", "ZEBRAS"),"ZEBRAS"))
# print(encrypt("WE ARE DISCOVERED FLEE AT ONCE", "ZEBRAS"))
# print()

print("Welcome to the Columnar Transposition Cipher!")

choice = input("Would you like to encrypt (e) or decrypt (d): ")
print()

if choice == "e":
    plain_text = input("What would you like to encrypt?: ")
    key = input("What is the key?: ")
    print()
    print("Plaintext: " + plain_text)
    print("Ciphertext: " + encrypt(plain_text, key))
elif choice == "d":
    cipher_text = input("What would you like to decrypt?: ")
    print("I'm sorry to ask, but I have yet to decrypt the cipher without the key")
    key = input("What is the key?: ")
    print()
    print("Ciphertext: " + cipher_text)
    print("Plaintext: " + decrypt(cipher_text, key))
else:
    print("Sorry! There seems to be an error")

