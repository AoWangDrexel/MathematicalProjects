"""
Author: Ao Wang
Date: 08/12/19
Description: Morse code encryper and decryter
"""

# The function retrieves the morse code from a text file and cleans it up so the letters
# can be stored in the keys and code into the values
def loadMorseTable():
    codes = ""
    with open("morseTable.txt", "r") as code:
        codes = code.read()

    # removes the escape sequences and white spaces
    codes.split("\n")
    codes = codes.split()

    keys = []
    values = []

    for i in range(len(codes)):
        if(i % 2 == 0):
            keys.append(codes[i])
        else:
            values.append(codes[i])

    # creates the morse code dictionary
    morse_dict = {}
    for i in range(len(keys)):
        morse_dict[keys[i]] = values[i]

# The function encrypts the plaintext into ciphertext and returns the string
def encrypt(plain_text):
    word = ""
    plain_text = plain_text.upper()
    for letter in plain_text:
        if(letter in morse_dict):
            # each letter is separated by a space
            word += morse_dict.get(letter) + " "
        else:
            # each word is seperated by 7 spaces
            word += "       " 
    return word

# The function returns the key by inputting a value of the key
# if values not in dictionary, return -1
def values_by_keys(dictionary, value):
    for keys, values in dictionary.items():
        if(value == values):
            return keys
    return -1

# The function decrypts the ciphertext
def decrypt(cipher_text):
    decoded = ""
    
    # creates a list by seperating each letter by the space
    cipher_text = cipher_text.split(" ")
    for code in cipher_text:
        
        # if a space is in the elements of the list, add a space to the
        # decoded message and remove the space from the element, so it can be identified
        if " " in code:
            decoded += " " + values_by_keys(morse_dict, code.strip())
        decoded += str(values_by_keys(morse_dict, code))
    
    # the space in the code is not a morse symbol, so the values_by_keys method returns -1
    # therefore replaces the 7 spaces of between the words that became 7 -1's to become a single space
    decoded = decoded.replace("-1-1-1-1-1-1-1"," ")
    return decoded

# intro
def main():
    loadMorseTable()
    print("Welcome to the Morse Code Encoding and Decoder!")
    print("CAUTION: Please seperate each morse symbol with a space and each word by seven spaces\n")
    choice = input("Would you like to encrypt (e) or decrypt (d)? ")
    print()

    if(choice == "e"):
        text = input("What would you like to encrypt? ")
        print()
        print("Plaintext: " + text)
        print("Ciphertext: " + encrypt(text))

    elif(choice == "d"):
        text = input("What would you like to decrypt? ")
        print()
        print("Ciphertext: " + text)
        print("Plaintext: "+ decrypt(text))
    else:
        print("There must have been a problem! Please try again")

if __name__ == "__main__":
    main()
