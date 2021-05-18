######################################################################################################################
# Name: Joseph Brown, Jacob Dumontier, Seth Gautreaux, Cameron Mitchell, Nikolas Morgan, Carter Ray, Kyle Rousselle, and Austin Scioneaux 
# Team: The Tower
# Date: 3/20/2021
# Description: Gets the time between two dates and generates a hash code for it.
# Python 3.7.7
######################################################################################################################

import hashlib
from datetime import datetime
import pytz

DEBUG = False


def checkDaylightSavings(current, epoch):
    # set the timezone
    timezone = pytz.timezone("US/Central")
    # get the offset in seconds for current
    currentOffset = timezone.localize(current).dst().seconds
    # get the offset in  seconds for the epoch 
    epochOffset = timezone.localize(epoch).dst().seconds
    # return true if the offsets are different since that would mean that one date is in daylight saving while the other is not
    return (not(currentOffset == epochOffset))
        
    

def calculateSeconds(current, epoch):
    # subtract the epoch from the current to get the time in between
    time = current - epoch
    # get the time in seconds
    time = int(time.total_seconds())
    # if one date is inside daylight savings and the other is not, subtract an hour from the time
    if(checkDaylightSavings(current, epoch)):
        time -= 3600
    return time
    
    

def getHash(seconds):
    # hash the string representation of the seconds the first time
    h = hashlib.md5(str(seconds).encode())
    # convert to hex
    h = h.hexdigest()
    # convert the hex into a string and hash it
    h = hashlib.md5(str(h).encode())
    # convert to hex again
    h = h.hexdigest()
    # convert to string
    h = str(h)

    count = 0
    string = ""
    # iterate through the hash to find the first two letters and concatenate to the string
    for i in h:
        if(i in ['a', 'b', 'c', 'd', 'e', 'f']):
            string += i
            count += 1
        if(count >= 2):
            break

    # reverse the string
    h = h[::-1]
    count = 0
    # iterate through the reversed string to find the first two numbers and concatenate to the string
    for i in h:
        if(i not in ['a', 'b', 'c', 'd', 'e', 'f']):
            string += i
            count += 1
        if(count >= 2):
            break
    
        
        
    return string


################## MAIN #####################


if(DEBUG):
    # set epoch date
    epoch = datetime(1999, 12, 31, 23, 59, 59)
    # set current date
    current = datetime(2013, 5, 6, 7, 43, 25)
else:
    # get the current date and time
    date = datetime.now()
    # get the input epoch
    epoch = input()
    # create a datetime object to hold the current date and time
    current = datetime(date.year, date.month, date.day, date.hour, date.minute, date.second)

    # split the epoch into its values at each space and create a list
    epoch = epoch.split(" ")

    # convert each value in the list into an integer
    for i in range(len(epoch)):
        epoch[i] = int(epoch[i])

    # use these value to create a datetime object
    epoch = datetime(epoch[0], epoch[1], epoch[2], epoch[3], epoch[4], epoch[5])
    



# calculate the seconds
seconds = calculateSeconds(current, epoch)

# divide the seconds by 60 and round down
num = seconds // 60
# multiply the rounded down value so that each code will be valid for 60 seconds
seconds = num * 60

# use the value of seconds to get the 4 character code
h = getHash(seconds)

print(h)
