###################################################
# Covert Chat Client
# Team: The Tower
# Names: Carter Ray, Kyle Rousselle, Seth Gautreaux, Austin Ovide, Cameron Mitchell, Jacob DuMontier, Joseph Brown, Nik Morgan
# Python 3.9
###################################################

#imports
import socket
from sys import stdout, argv
from time import time

# CONTROL VARIABLES
DEBUG = False
MASS_OUTPUT = False
VALUE = 0.055

# optional execution syntaxes
#   python3 client.py -c                    - mass output decode with many test values, also disables constant flush to stdout
#                                               the above is for use in challenge when latency might be an issue
#   python3 client.py [float number]        - specify a value to use to separate the ones and zeroes
#   python3 client.py [float number] -c     - both above

#handles optional inputs
try:
    if(len(argv) == 2):
        if(argv[1] == "-c"):
            MASS_OUTPUT = True
        else:
            VALUE = float(argv[1])

    if(len(argv) == 3):
        if("-c" == argv[2]):
            MASS_OUTPUT = True
        VALUE = float(argv[1])

    VALUE = round(VALUE, 3)
except:
    print("Invalid syntax\nTry: python3 client.py [optional float] [optional -c]\nExecuting normal mode\n")



#conversion function 
def convert(msg):
    i = 0
    string = ""
    msglen = len(msg)
    while(msglen - i  >= 8):
        letter = 0;
        #convert 8 bits at a time
        for j in range(7, -1, -1):
                bit = int(msg[i])
                letter += (bit * (2 ** j))
                i += 1 
        #add to string
        string += chr(letter)

    return string


# set the server's IP address and port
ip = "138.47.102.120"
port = 31337


deltas = []

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))
comparetime = time()
# receive data until EOF
data = s.recv(4096).decode()
print("Overt Message:")
while (data.rstrip("\n") != "EOF"):
        #output the data
        stdout.write(data)
        if(MASS_OUTPUT):
            pass
        else:
            stdout.flush()
        # start the "timer", get more data, and end the "timer"
        t0 = time()
        data = s.recv(4096).decode()
        t1 = time()
        # calculate the time delta (and output if debugging)
        delta = round(t1 - t0, 3)
        deltas.append(delta)
        
        if (DEBUG):
                stdout.write(" {}\n".format(delta))
                stdout.flush()
                
# close the connection to the server
s.close()

#for MASS_OUTPUT
#outputs a lot of trial decoding values
test = .030
if(MASS_OUTPUT):
    while(test < 0.090):
        testmsg = ""
        print(test)
        for val in deltas:
            if(val >= test):
                testmsg += "1"
            else:
                testmsg += "0"
        test += .001
        test = round(test, 3)
        try:
            print(convert(testmsg))
        except:
            print("\ncould not decode with test value : {}".format(test))



#use the default VALUE (or the optional input) to convert the timings to ones and zeroes
msg = ""
for val in deltas:
        if(val >= VALUE):
            msg += "1"
        else:
            msg += "0"
            
#convert the ones and zeroes to a string
string = convert(msg)

#remove eof
string = string.replace("EOF", "")

print("\n\nCovert Message:")
print(string)

#print the timing used so that the user can specify a different timing if he needs to on next run.
print("\nDecode Time Divider: {}".format(VALUE))

