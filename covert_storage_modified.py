##MODIFIED FOR CHALLNEGE
######################################################################################################################
# Name: Joseph Brown, Jacob Dumontier, Seth Gautreaux, Cameron Mitchell, Nikolas Morgan, Carter Ray, Kyle Rousselle, and Austin Scioneaux 
# Team: The Tower
# Date: 4/2/2021
# Description: Finds covert message hidden in file permissions on FTP server
# Python 3.9.3
######################################################################################################################


METHOD = 10


if(not(METHOD == 7 or METHOD == 10)):
        print("No valid method, please change METHOD to 7 or 10")
        exit(-1)

#ftp connection
###############
        
from ftplib import FTP

# FTP server details
IP = "138.47.102.106"
PORT = 8008
USER = "thesun"
PASSWORD = "myfirstchallenge"
FOLDER = "/.secretstorage/.folder2/.howaboutonemore"
USE_PASSIVE = True # set to False if the connection times out

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)
# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

# decode
###############

# get the folder contents
s = ""
for f in files:
        #if we only use 7 bits
        if (METHOD == 7):
                #discard files without empty first 3 bits
                if(f[:3] == "---"):
                        #append to string
                        s += f[3:10]
        #if we use all the bits
        if (METHOD == 10):
                s += f[:10]
#emtpy message
message = ""
for letter in s:
        #if -, its a 0
        if (letter == '-'):
                message += "0"
        #if its a letter, its a 1
        else:
                message += "1"

#defaults
s = ""
i = 0

#go through the whole binary text input
while(i < len(message)):
        letter = 0;
        if((len(message) - i) < 6):
                break
        for j in range(6, -1, -1):
                bit = int(message[i])
                letter += (bit * (2 ** j))
                i += 1
        
        #add to string
        s += chr(letter)

#print string
print(s)
