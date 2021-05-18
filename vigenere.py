######################################################################################################################
# Name: Joseph Brown, Jacob Dumontier, Seth Gautreaux, Cameron Mitchell, Nikolas Morgan, Carter Ray, Kyle Rousselle, and Austin Scioneaux 
# Team: The Tower
# Date: 3/22/2021
# Description: Encrypts or decrypts a string using the Vigenere Cypher
# Python 2.7.16
######################################################################################################################

import sys

#encode
def encode(key, text):
    
    #make array to aid in shifting the message
    shiftarr = [0] * (len(key))
    for i in range(0, len(key)):
        shiftarr[i] = ord(key[i]) - ord('a')

    #default values
    e_txt = ""
    k = 0

    #for the entire input text
    for j in range(0, len(text)):
        #shift the text through the alphabet
        charNum = ord(text[j]) + shiftarr[k]
        
        #keep the capital and lowercase letters as separate alphabets
        #capital
        if(ord(text[j]) > 64 and ord(text[j]) < 91):
            #if it goes out of range, bring it back into range
            if (charNum > 90):
                charNum -= 26
        #lowercase
        elif(ord(text[j]) > 96 and ord(text[j]) < 123):
            #if it goes out of range, bring it back into range
            if (charNum > 122):
                charNum -= 26
        #if its not a letter / is a symbol
        else:
            #keep it
            charNum = ord(text[j])
            #dont move to the next shift value for the key
            k -= 1

        #append each shifted character to the encoded text string
        e_txt += chr(charNum)

        #move to the next shift value by incrementing the k counter
        k += 1

        #if we're out of range of the shift array, start at the beginning
        if(k == len(shiftarr)):
            k = 0

    #print the result
    print(e_txt)


def decode(key, text):
    
    #make array to aid in shifting the message
    shiftarr = [0] * (len(key))
    for i in range(0, len(key)):
        shiftarr[i] = ord(key[i]) - ord('a')

    #default values
    d_txt = ""
    k = 0
    
    #for the entire input text
    for j in range(0, len(text)):
        #unshift the text
        charNum = ord(text[j]) - shiftarr[k]

        #keep the capital and lowercase letters as separate alphabets
        #capital
        if(ord(text[j]) > 64 and ord(text[j]) < 91):
            #if it goes out of range, bring it back into range
            if (charNum < 65):
                charNum += 26
        #lowercase
        elif(ord(text[j]) > 96 and ord(text[j]) < 123):
            #if it goes out of range, bring it back into range
            if (charNum < 97):
                charNum += 26
        #not a letter / is a symbol
        else:
            #keep it
            charNum = ord(text[j])
            #dont move to the next shift value for the key
            k -= 1

        #append each unshifted character to the decoded text string
        d_txt += chr(charNum)
        
        #move to the next shift value by incrementing the k counter
        k += 1

        #if we're out of range of the shift array, start at the beginning
        if(k == len(shiftarr)):
            k = 0

    #print the result 
    print(d_txt)


########
# MAIN #
########

#if the command is used improperly, show usage
if(len(sys.argv) != 3):
    print("Wrong usage. < -e or -d > [key]")
    exit(0)

#key is the 3rd argument
key = sys.argv[2]
key = key.lower()
key = key.replace(' ', '')

#method is the second character of the second input (e or d)
method = sys.argv[1][1]

#if you used anything other than e or d.
if(not(method == "e" or method == "d")):
    print("No valid method selected. Choose '-e' or '-d' when executing")
    exit(0)

#encode input text
while( method == "e"):
    #try taking input from user;
    #there will be an error if the user used file redirection
    try:
        text = input()
        encode(key, text)
    except:
        text = sys.stdin.readline()
        encode(key, text)
        break

#decode text input from redirect
while (method == "d"):
    #try taking input from user;
    #there will be an error if the user used file redirection
    try:
        text = input()
        decode(key, text)
    except:
        text = sys.stdin.readline()
        decode(key, text)
        break

