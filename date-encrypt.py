import datetime
import os
while True:
    ix = input("command (send or recieve)> ")
    if "send" in ix:
        strtosend = ix[5:len(ix)]
        key = str(datetime.datetime.now())
        key1 = key
        if len(key) < len(strtosend):
            key = key * (len(strtosend) // len(key))
            key += key[0:len(strtosend) % len(key)]
        stout = ""
        key = key[::-1]
        for i in range(0,len(strtosend)):
            b = int(ord(key[i]))-60
            stout += chr(int(ord(strtosend[i]))+b)
        finalmsg = stout + "/#&0#/" + key1
        file1 = open("message.msg","w")
        file1.writelines(finalmsg)
        file1.close()
        print("sent encrypted message as:",finalmsg)
    if "recieve"in ix:
        file1 = open("message.msg","r")
        L = []
        L = file1.readline().split("/#&0#/")
        strtosend,key = L[0],L[1]
        if len(key) < len(strtosend):
            key = key * (len(strtosend) // len(key))
            key += key[0:len(strtosend) % len(key)]
        stout = ""
        key = key[::-1]
        for i in range(0,len(strtosend)):
            b = int(ord(key[i]))-60
            stout += chr(int(ord(strtosend[i]))-b)
        print("recieved message: ",stout)
        
