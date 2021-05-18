######################################################################################################################
# Name: Joseph Brown, Jacob Dumontier, Seth Gautreaux, Cameron Mitchell, Nikolas Morgan, Carter Ray, Kyle Rousselle, and Austin Scioneaux 
# Team: The Tower
# Date: 3/22/2021
# Description: Encrypts or decrypts a string using the Vigenere Cypher
# Python 2.7.16
######################################################################################################################

import sys


if(len(sys.argv) != 2):
    print("Wrong usage. Do python3 xor.py [key] < [text]")
    exit(-1)

#read the key
key = bytearray(sys.stdin.buffer.read())

#read the cipher
cipherfile = open(sys.argv[1], "rb")
text = bytearray(cipherfile.read())
cipherfile.close()

#make sure the text and key are the same length
if(len(text) != len(key)):
    print("Key and Text different lengths. Exiting. . .")
    exit(-1)

#xor them together
output = bytearray()
for i in range(len(key)):
    output.append(key[i] ^ text[i])

#write to stdout
sys.stdout.buffer.write(output)
