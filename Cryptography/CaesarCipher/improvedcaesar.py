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
    global break_key
    break_key = alphabet.index(high_key) - alphabet.index("E")
    
    # if key is negative, add 26
    if break_key <= 0:
        break_key += 26
    
    # 26 - by the key reverses the effect of the cipher
    # 26 - key + key = 26 nullifies the effect of the cipher
    return caesar_cipher(cipher_text, 26 - break_key)

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


# The function prints out all the possibilities of the cipher by testing keys from 0-25
def brute_force(cipher_text):
    print("Hacking...")
    
    percentages = {}
    for key in range(1, 26):
        decryptedText = caesar_cipher(cipher_text, key)

        # if the percentage of words in the word dictionary is above 80%, then add the keys and percentages
        # into the dictionary
        threshold = 80
        if getEnglishCount(decryptedText) > threshold:
            percentages[key] = getEnglishCount(decryptedText)

    key_break = findMaxInd(percentages)
   
    if key_break != -1:
        print("Cipher hacked! :)\n")
        print("The key is: " + str(26 - key_break))
        print("Decrypted text: " + caesar_cipher(cipher_text, key_break) + "\n")
        print("Percentage of words in dictionary: " + str(percentages[key_break]))
    else:
        print("Failed to hack cipher :(")

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
    print("Welcome to the Caesar Encrypter and Decrypter!")
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
        print("------------------------------Cryptanalysis------------------------------------")
        print("Ciphertext: " + text)
        decrypted_message = decrypt(text)
        print("Plaintext: " + decrypt(text))
        print("The key is: " + str(break_key))
        
        if(getEnglishCount(decrypted_message) < 70):
            print("-----------------------------Brute Force---------------------------------------")
            print("It seems that the crytoanalysis failed. Let's try brute-force!")
            brute_force(text)
    else:
        print("Oops there seems to be an error")
    print()
    
if __name__ == "__main__":
    main()

# testing

# it seems that cryptanalysis method works best if there is a good amount of text
with open("caesar.txt","r") as file:
    f = file.read()
print(decrypt(f))
print()

# brute force works just as well, but most likely not as efficient
print(brute_force(f))
