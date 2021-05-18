######################################################################################################################
# Name: Joseph Brown, Jacob Dumontier, Seth Gautreaux, Cameron Mitchell, Nikolas Morgan, Carter Ray, Kyle Rousselle, and Austin Scioneaux 
# Team: The Tower
# Date: 3/22/2021
# Description: Encrypts or decrypts a string using the Vigenere Cypher
# Python 2.7.16
######################################################################################################################

import sys

#read left to right (b) or right to left (l)
ENDIAN = 'b'

#initial values
QUIT = False

METHOD = ''
MODE = ''
OFFSET = 0
INTERVAL = 1
WRAPPER = bytearray()
HIDDEN = bytearray()
sentlist = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
SENTINEL = bytearray(sentlist)

#read arguments
for i in range (0, len(sys.argv)):

    if(sys.argv[i] == "-s"):
        METHOD = 's'
    elif(sys.argv[i] == "-r"):
        METHOD = 'r'

    if(sys.argv[i] == "-b"):
        MODE = 'b'
    elif(sys.argv[i] == "-B"):
        MODE = 'B'

    if ("-o" == sys.argv[i][:2]):
        OFFSET = int(sys.argv[i][2:])

    if("-i" == sys.argv[i][:2]):
        INTERVAL = int(sys.argv[i][2:])

    if("-w" == sys.argv[i][:2]):
        thefile = open(sys.argv[i][2:], "rb")
        WRAPPER = bytearray(thefile.read())
        thefile.close()

    if("-h" == sys.argv[i][:2]):
        thefile = open(sys.argv[i][2:], "rb")
        HIDDEN = bytearray(thefile.read())
        thefile.close()

#if method was not set
if(METHOD == ''):
    QUIT = True
#if mode was not set
if(MODE == ''):
    QUIT = True
#if hiding nothing
if(METHOD == 's' and len(HIDDEN) == 0):
    print("You must specify a file to hide")
    QUIT = True
#if there's no wrapper
if(len(WRAPPER) == 0):
    print("You must specify a wrapper file")
    QUIT = True

#quit if any of the above conditions are met
if(QUIT):
    print("Wrong usage, try:\npython3 steg.py -(sr) -(bB) -o<va> [-i<val>] -w<val> [-h<val>]")
    quit(-1)

######## STORAGE ########

if(METHOD == 's'):

    ### BYTE ###

    if(MODE == 'B'):
        for byte in HIDDEN:
            WRAPPER[OFFSET] = byte
            OFFSET += INTERVAL

        for byte in SENTINEL:
            WRAPPER[OFFSET] = byte
            OFFSET += INTERVAL

        sys.stdout.buffer.write(WRAPPER)

    ### BIT ###

    if(MODE == 'b'):
        if(ENDIAN == 'b'):
            i = 0
            while(i < len(HIDDEN)):
                for k in range(8):
                    WRAPPER[OFFSET] &= 0b11111110
                    WRAPPER[OFFSET] |= ((HIDDEN[i] & 0b10000000) >> 7)
                    HIDDEN[i] = (HIDDEN[i] << 1) & (2 ** 8 - 1)
                    OFFSET += INTERVAL
                i += 1
            i = 0 
            while(i < len(SENTINEL)):
                for k in range(8):
                    WRAPPER[OFFSET] &= 0b11111110
                    WRAPPER[OFFSET] |= ((SENTINEL[i] & 0b10000000) >> 7)
                    SENTINEL[i] = (SENTINEL[i] << 1) & (2 ** 8 - 1)
                    OFFSET += INTERVAL
                i += 1

        if(ENDIAN == 'l'):
            i = 0
            while(i < len(HIDDEN)):
                for k in range(8):
                    WRAPPER[len(WRAPPER) - 1 - OFFSET] &= 0b11111110
                    WRAPPER[len(WRAPPER) - 1 - OFFSET] |= ((HIDDEN[i] & 0b10000000) >> 7)
                    HIDDEN[i] = (HIDDEN[i] << 1) & (2 ** 8 - 1)
                    OFFSET += INTERVAL
                i += 1

            i = 0
            while(i < len(SENTINEL)):
                for k in range(8):
                    WRAPPER[len(WRAPPER) - 1 - OFFSET] &= 0b11111110
                    WRAPPER[len(WRAPPER) - 1 - OFFSET] |= ((SENTINEL[i] & 0b10000000) >> 7)
                    SENTINEL[i] = (SENTINEL[i] << 1) & (2 ** 8 - 1)
                    OFFSET += INTERVAL
                i += 1

        sys.stdout.buffer.write(WRAPPER)


####### RETRIEVAL #######

if(METHOD == 'r'):   
    i = 0

    ### BYTE ###

    if(MODE == 'B'):
        while(OFFSET < len(WRAPPER)):
            b = WRAPPER[OFFSET]
            if(b == SENTINEL[i]):
                i += 1
                if(i == len(SENTINEL)):
                    HIDDEN = HIDDEN[:len(HIDDEN) - len(SENTINEL) + 1]
                    sys.stdout.buffer.write(HIDDEN)
                    break
            else:
                i = 0
            HIDDEN.append(b)
            OFFSET += INTERVAL

    ### BIT ###

    if(MODE == 'b'):

        if(ENDIAN == 'b'):
            i = 0
            while(OFFSET < len(WRAPPER)):
                b = 0
                for j in range(8):
                    b |= (WRAPPER[OFFSET] & 0b00000001)
                    if(j < 7):
                        b = (b << 1) & (2 ** 8 - 1)
                        OFFSET += INTERVAL

                if(b == SENTINEL[i]):
                    print(b)
                    i += 1
                    if (i == len(SENTINEL)):
                        HIDDEN = HIDDEN[:len(HIDDEN) - len(SENTINEL) + 1]
                        sys.stdout.buffer.write(HIDDEN)
                        break
                else:
                    i = 0

                HIDDEN.append(b)
                OFFSET += INTERVAL

        
        if(ENDIAN == 'l'):
            i = 0
            while(len(WRAPPER) - 1 - OFFSET >= 0):
                b = 0
                for j in range(8):
                    b |= ((WRAPPER[len(WRAPPER) - 1 - OFFSET]) & 0b00000001)
                    if(j < 7):
                        b = (b << 1) & (2 ** 8 - 1)
                        OFFSET += INTERVAL

                if(b == SENTINEL[i]):
                    i += 1
                    if (i == len(SENTINEL)):
                        HIDDEN = HIDDEN[:len(HIDDEN) - len(SENTINEL) + 1]
                        sys.stdout.buffer.write(HIDDEN)
                        break
                else:
                    i = 0

                HIDDEN.append(b)
                OFFSET += INTERVAL

