"""
Author: Ao Wang
Date: 09/05/19
Description: Affine cipher with decrypter/hack
"""

# The function loads the English alphabet 
def loadAlphabet():
    alphabet = ""
    for i in range(26):
        alphabet += chr(ord("a") + i)
    return alphabet

# The function returns the greatest common denominator using Euclid's algorithm 
def gcd(num1, num2):
    while num1 != 0:
        num1, num2 = num2 % num1, num1
    return num2

# The function returns the modular inverse using Euclid's extended algorithm
def modInverse(num1, num2):
    if gcd(num1, num2) != 1:
        return -1
    
    u1, u2, u3 = 1, 0, num1
    v1, v2, v3 = 0, 1, num2
    
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1-q*v1), (u2-q*v2), (u3-q*v3), v1, v2, v3
        
    return u1 % num2

# The function returns the integer used for the cipher using key1 and key2
def equation(num, slope, intercept):
    return slope * num + intercept

# The function encrypts the plain text using the Affine cipher
def encrypt(plain_text, key_a, key_b):
    cipher_text = ""
    for symbol in plain_text:
        if symbol.lower() in ALPHABET:
            idx = equation(ALPHABET.index(symbol.lower()), key_a, key_b) % len(ALPHABET)
            if symbol.isupper():
                cipher_text += ALPHABET[idx].upper()
            else:
                cipher_text += ALPHABET[idx]
        else:
            cipher_text += symbol
    return cipher_text

# The function is a simple decryption that needs the keys 
def decrypt(cipher_text, key_a, key_b):
    plain_text = ""
    for symbol in cipher_text:
        if symbol.lower() in ALPHABET:
            idx = abs((ALPHABET.index(symbol.lower()) - key_b)*modInverse(key_a, len(ALPHABET)) % len(ALPHABET))
            if symbol.isupper():
                plain_text += ALPHABET[idx].upper()
            else:
                plain_text += ALPHABET[idx]
        else:
            plain_text += symbol
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

def brute_force(cipher_text):
    print("Hacking...")
    
    percentages = {}
    key1 = 1
    while key1 != 26:
        while gcd(key1, 26) != 1:
            key1 += 1
            
        for key2 in range(26):
            if getEnglishCount(decrypt(cipher_text, key1, key2)) > 80:
                percentages[str(key1) + " " + str(key2)] = getEnglishCount(decrypt(cipher_text, key1, key2))
        key1 += 1
        
    key_break = list(map(int, findMaxInd(percentages).split()))
    print("Key 1: " + str(key_break[0]))
    print("Key 2: " + str(key_break[1]))
    print("Percentage accuracy: " + str(percentages[findMaxInd(percentages)]))
    return decrypt(cipher_text, key_break[0], key_break[1])
                
            
# The function finds the highest percentage of words in the dictionary and returns the key
def findMaxInd(keys):
    maximum = -1
    max_key = -1
    for key in keys:
        if keys[key] > maximum:
            maximum = keys[key]
            max_key = key
    return max_key

def main():
    global ALPHABET
    ALPHABET = loadAlphabet()
    print("Welcome to the Affine Encrypted and Decrypter!")
    choice = input("Would you like to encrypt (e) or decrypt (d)? ")
    print()
    
    if choice.lower() == "e":
        msg = input("What would you like to encrypt? ")
        key1 = int(input("Key 1? "))
        
        while key1 == 0 or key1 == 1 or gcd(key1, len(ALPHABET)) != 1 or key1 < 0:
            if gcd(key1, len(ALPHABET)) != 1:
                print("Sorry the Key 1: " + str(key1) + " has to be coprime, meaning the greatest common denominator has to be 1")
            if key1 == 0 or key1 == 1:
                print("Key 1: " + str(key1) + " is a poor key")
            if key1 < 0:
                print("Key 1: " + str(key1) + " has to be positive")
            key1 = int(input("Key 1? "))
            
        key2 = int(input("Key 2? "))
        while key2 < 0:
            print("Key 2: " + str(key2) + " has to be positive")
            key2 = int(input("Key 2? "))
                
        print("Plain text: " + msg)
        print("Cipher text: " + encrypt(msg, key1, key2))
        
        
    elif choice.lower() == "d":
        msg = input("What would you like to decrypt? ")
        
        hack = input("Do you have the keys (k) or would you like to brute force (b) it? ")
        hack = hack.lower().strip()
        plain_text = ""
        
        if hack == "k":
            key1 = int(input("Key 1? "))
            key2 = int(input("Key 2? "))
            plain_text = decrypt(msg, key1, key2)
        elif hack == "b":
            plain_text = brute_force(msg)
            
        print("Cipher text: " + msg)
        print("Plain text: " + plain_text)
        
    else:
        print("There seems to be a problem. Run again?")
        
    
if __name__ == "__main__":
    main()
