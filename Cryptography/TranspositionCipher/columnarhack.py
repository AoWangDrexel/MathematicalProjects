"""
Author: Ao Wang
Date: 08/27/19
Description: Brute force decryption of the Simplified Columnar Cipher w/o asking the key
"""

LETTERS_AND_SPACE = "abcdefghijklmnopqrstuvwxyz" + ' \t\n'

# The function returns a list of words from two word text files
def loadDictionary():
    with open("words.txt", "r") as f1:
        file1 = f1.read().split("\n")
        
    with open("morewords.txt", "r") as f2:
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

# The function hacks the Columnar Transposition Cipher and prints out the key, decrypted message, and percentage
# of the words in the dictionary
def hackTransposition(msg):
    print("Hacking...")
    
    percentages = {}
    
    # try keys from 1 to the length of the message
    for key in range(1, len(msg)):
        decryptedText = decrypt(msg, key)
        
        # if the percentage of words in the word dictionary is above 80%, then add the keys and percentages
        # into the dictionary
        threshold = 80
        if getEnglishCount(decryptedText) > threshold:
            percentages[key] = getEnglishCount(decryptedText)

    key_break = findMaxInd(percentages)
    
    if key_break == -1:
        print("Failed to hack cipher :(")
    else:
        print("Cipher hacked! :)")
        
    print()
    print("The key is: " + str(key_break))
    print("Decrypted text: " + decrypt(msg, key_break) + "\n")
    print("Percentage of words in dictionary: " + str(percentages[key_break]))
        
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
    with open("msg.txt", "r") as file:
        myMessage = file.read()
    hackTransposition(myMessage)
    
if __name__ == "__main__":
    main()
