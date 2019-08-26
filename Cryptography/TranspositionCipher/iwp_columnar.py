"""
Author: Ao Wang
Date: 08/25/19
Description: Simplified version of the Columnar Cipher, inspired from Invent W/ Python
https://inventwithpython.com/cracking/chapter7.html
https://inventwithpython.com/cracking/chapter8.html
"""

"""
Encryption: 
plain text: "Common sense is not so common."
key = 8

    0 1 2 3 4 5 6 7 
0   C o m m o n   s
1   e n s e   i s 
2   n o t   s o   c
3   o m m o n .

output: Cenoonommstmme oo snnio. s s c

['Ceno', '', '', '', '', '', '', '']
['Ceno', 'onom', '', '', '', '', '', '']
['Ceno', 'onom', 'mstm', '', '', '', '', '']
['Ceno', 'onom', 'mstm', 'me o', '', '', '', '']
['Ceno', 'onom', 'mstm', 'me o', 'o sn', '', '', '']
['Ceno', 'onom', 'mstm', 'me o', 'o sn', 'nio.', '', '']
['Ceno', 'onom', 'mstm', 'me o', 'o sn', 'nio.', ' s ', '']
['Ceno', 'onom', 'mstm', 'me o', 'o sn', 'nio.', ' s ', 's c']
"""

"""
Decryption:
cipher text: 
Cenoonommstmme oo snnio. s s c
key = 8

find length of text, divide by key, and round the result up to find number of column
30/8 = 3.75 --> 4
key is the number of rows

   0 1 2 3
0  C e n o 
1  o n o m
2  m s t m 
3  m e   o
4  o   s n
5  n i o .
6    s   
7  s   c

goes back to "Common sense is not so common."
"""

import math
def encrypt(plain_text, key):
    cipher_text = [""] * key
    
    for i in range(key):
        row = i
        while row < len(plain_text):
            cipher_text[i] += plain_text[row]
            row += key
        print(cipher_text)
    return "".join(cipher_text)

def decrypt(cipher_text, key):
    num_of_col = math.ceil(len(cipher_text)/float(key))
    num_of_row = key
    
    excess = num_of_col * num_of_row - len(cipher_text)
    plain_text = [""] * num_of_col
    
    col = 0
    row = 0
    for letter in cipher_text:
        plain_text[col] += letter
        col += 1
        
        if (col == num_of_col) or (col == num_of_col - 1 \
           and row >= num_of_row - excess):
            col = 0
            row += 1
    print(plain_text)
    return "".join(plain_text)

def main():
    print("Welcome to the Simplified Columnar Tranposition Cipher!")
    choice = input("Would you like to encrypt (e) or decrypt (d)? ")
    print()
    if choice == "e":
        plain_text = input("What would you like to encrypt? ")
        key = int(input("What is the key? "))
        print()
        print("Plain text: " + plain_text)
        print("Cipher text: " + encrypt(plain_text, key))
    elif choice == "d":
        cipher_text = input("What would you like to decrypt? ")
        key = int(input("What is the key? "))
        print()
        print("Cipher text: " + cipher_text)
        print("Plain text: " + decrypt(cipher_text, key))
    else: 
        print("Incorrect input, run again!")

if __name__ == "__main__":
    main()
