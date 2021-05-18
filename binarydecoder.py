######################################################################################################################
# Name: Joseph Brown, Jacob Dumontier, Seth Gautreaux, Cameron Mitchell, Nikolas Morgan, Carter Ray, Kyle Rousselle, and Austin Scioneaux 
# Team: The Tower
# Date: 3/20/2021
# Description: Converts binary data into its string equivalent
# Python 3.9
######################################################################################################################


   
    
#function to convert binary to ascii
def convert(m):
    #default length is 8 bits
    eightBits = True;

    #check to see if 8 bit or 7 bit
    if(len(m) % 8 == 0):
        #1st place bit will always be 0 in the ascii table range
        for i in range(len(m)):
            if (i % 8) == 0:
                if (m[i] == 1):
                    eightBits = False
                    break
    #it is 7 bits
    else:
        eightBits = False

    #if it is eight bits, we'll start from 7 and go to 0
    if(eightBits):
        bitsnum = 7
    else:
        bitsnum = 6
        
    #defaults
    s = ""
    i = 0

    #go through the whole binary text input
    while(i < len(m)):
        letter = 0;
        #convert either 7 or 8 bit binary into ascii
        for j in range(bitsnum, -1, -1):
            bit = int(message[i])
            letter += (bit * (2 ** j))
            i += 1
        #add to string
        s += chr(letter)

    #print string
    print(s)

##########
###MAIN###
##########

#get message
message = input()

#convert message
message.replace("Zero", "0")
message.replace("One", "1")

convert(message)

