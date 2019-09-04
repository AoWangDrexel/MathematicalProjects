"""
Author: Ao Wang
Date: 08/16/19
Description: Encryption and Decryption of Transposition Columnar Cipher
** Found a way to decipher the encryption w/o the key, but it takes a long time with long messages
"""

import numpy as np
import math
import random
from itertools import permutations

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
    
    #plain_text = plain_text.replace(" ", "")
    
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
#             else:
#                 r = random.randint(ord("A"), ord("Z"))
#                 grid[i,j] = chr(r)
                
    cipher_text = ""    
    idx = 0
    # stores the cipher by the order from the list returned from def order(word)
    while idx != col:
        i = ordering.index(idx)
        for j in range(row):
            cipher_text += grid[j,i]
        idx += 1

    #cipher_text = cipher_text.replace(" ", "")
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
    while idx < col:
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

# -------------------- Brute force section ------------------------
LETTERS_AND_SPACE = "abcdefghijklmnopqrstuvwxyz" + ' \t\n'

# The function returns a list of words from two word text files
def loadDictionary():
    with open("words.txt", "r") as f1, \
         open("morewords.txt", "r") as f2:
        file1 = f1.read().split("\n")
        file2 = f2.read().split("\n")
    
    # second text file was all uppercase, so needed to become lowercase
    for i in range(len(file2)):
        file2[i] = file2[i].lower()
        
    # extend the second file by adding the first
    file2.extend(file1)
    
    return file2
    
ENGLISH_WORDS = loadDictionary()

# The function removes non characters in the LETTERS_AND_SPACE variable
def removeNonLetters(msg):
    lettersOnly = []
    for symbol in msg:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return "".join(lettersOnly)

# The function returns the percentage of words in the dictionary
def getEnglishCount(msg):
    msg = msg.lower()
    msg = removeNonLetters(msg)
    possibleWords = msg.split()
    if possibleWords == []:
        return 0
    matches = 0
    
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return 100 * float(matches)/len(possibleWords)

# The function brute forces
def brute_force(cipher_text):
    print("Hacking...")
    global percentages
    percentages = {}
    
    # goes from 1 to the length of the text-1
    for length in range(1, len(cipher_text)):
        ordering = list(range(0,1+length))
        permutation_list = list(permutations(ordering))
        
        # goes through every single permutation
        for p in permutation_list:
            len_of_col = len(p)
            row = math.ceil(len(cipher_text)/len_of_col)
            grid = np.full((row, len_of_col), " ")

            idx = 0
            l = 0
    
            # storing back the letters of the cipher in the matrix
            # in the same order from which it came
            while idx < len_of_col:
                i = p.index(idx)
                for j in range(row):
                    if l < len(cipher_text):
                        grid[j,i] = cipher_text[l]
                        l += 1
                idx += 1

            # getting the plaintext out
            plain_text = ""
            for i in range(row):
                for j in range(len_of_col):
                    plain_text += grid[i,j]
            # has to have 90% of words from dictionary
            # can be adjusted to get more accurate decryption
            threshold = 90
            if getEnglishCount(plain_text) >= threshold and getEnglishCount(plain_text) <= 100:
                return p
    return -1
    
# The function is just a separate part of brute force to make it more concise 
def break_cipher(key_break, cipher_text):
    len_of_col = len(key_break)
    row = math.ceil(len(cipher_text)/len_of_col)
    grid = np.full((row, len_of_col), " ")

    idx = 0
    l = 0
 
    while idx < len_of_col:
        i = key_break.index(idx)
        for j in range(row):
            if l < len(cipher_text):
                grid[j,i] = cipher_text[l]
                l += 1
        idx += 1

    plain_text = ""
    for i in range(row):
        for j in range(len_of_col):
            plain_text += grid[i,j]
    print("Key: " + str(key_break))                        
    return plain_text  

# The function finds the highest percentage of words in the dictionary and returns the key
def findMaxInd(keys):
    maximum = -1
    max_key = -1
    for key in keys:
        if keys[key] > maximum:
            maximum = keys[key]
            max_key = key
    return max_key
 
# testing using wikipedia example
# print(decrypt(encrypt("WE ARE DISCOVERED FLEE AT ONCE", "ZEBRAS"),"ZEBRAS"))
# print(encrypt("WE ARE DISCOVERED FLEE AT ONCE", "ZEBRAS"))
# print()

def main():
    print("Welcome to the Columnar Transposition Cipher!")

    choice = input("Would you like to encrypt (e) or decrypt (d): ")
    print()
    choice = choice.lower().strip()
    
    if choice == "e":
        plain_text = input("What would you like to encrypt?: ")
        key = input("What is the key?: ")
        print()
        print("Plaintext: " + plain_text)
        print("Ciphertext: " + encrypt(plain_text, key))
    elif choice == "d":
        cipher_text = input("What would you like to decrypt?: ")
        hack = input("Do you have the key (k)? Or would you like to brute force it? (b) ")
        hack = hack.lower().strip()
        plain_text = ""
        
        if hack == "k": 
            key = input("What is the key?: ")
            plain_text = decrypt(cipher_text, key)
        elif hack == "b":
            print("**WARNING** Brute force method will take a lot of time for long messages because the method checks all the permutations")
            plain_text = break_cipher(brute_force(cipher_text), cipher_text)
            
        print()
        print("Ciphertext: " + cipher_text)
        print("Plaintext: " + str(plain_text))
    else:
        print("Sorry! There seems to be an error")

if __name__ == "__main__":
    main()
