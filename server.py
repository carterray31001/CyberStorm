ZERO = 0.025
ONE = 0.1

# use Python 3
import socket
from time import sleep

# set the port for client connections
port = 1337

# create the socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))

# listen for clients
# this is a blocking call
s.listen(0)
print("Server is listening...")

# a client has connected!
c, addr = s.accept()

# set the message
msg = "Some sort of overt message is being transmitted here. But there is a hidden message being covertly transmitted! Can you guess it? "

covertmsg = "Spectacular achievement is always preceded by unspectacular preparation. -- Robert H. Schuller"

covertmsg = "Hello there, how are you"

encodedmsg = ""
for letter in covertmsg:
	encodedmsg += (bin(ord(letter))[2:]).zfill(8)
# send the message, one letter at a time
i = 0
j = 0
while (i < len(encodedmsg)):
	c.send(msg[j].encode())
	# delay a bit in between each letter
	if(encodedmsg[i] == "0"):
		sleep(ZERO)
	else:
		sleep(ONE)
		
	i += 1
	j += 1
	if(j == len(msg)):
		j = 0

# send EOF and close the connection to the client
c.send("EOF".encode())
print("Message sent...")
c.close()

print(encodedmsg)
