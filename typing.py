from pynput.keyboard import Key, Controller
from random import randint
from termios import tcflush, TCIFLUSH 
from sys import stdin, stdout
from time import time


DEBUG = False


password = input()
features = input()

password = password.split(",")
password = password[:len(password)//2 + 1]
password = "".join(password)

features = features.split(",")
features = [float(a) for a in features]


keypress = features[:len(features)//2+1]
keyinterval = features[len(features)//2+1:]

keyboard = Controller()

i = 0

if(DEBUG):
    for char in password:
        ts = time()
        keyboard.press(char)
        while(time() - ts < keypress[i]):
            pass
        keyboard.release(char)
        print(time() - ts)
        if(i == len(keyinterval)):
            break
        ts = time()
        while(time() - ts < keyinterval[i]):
            pass
        
        i += 1


else:
    for char in password:
        ts = time()
        keyboard.press(char)
        while(time() - ts < keypress[i]):
            pass
        keyboard.release(char)
        if(i == len(keyinterval)):
            break
        ts = time()
        while(time() - ts < keyinterval[i]):
            pass
        
        i += 1


tcflush(stdout, TCIFLUSH)

