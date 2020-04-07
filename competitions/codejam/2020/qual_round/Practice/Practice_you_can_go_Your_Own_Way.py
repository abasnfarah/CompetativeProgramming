# Abas Farah - CodeJam 2020
# Practice round

# You can go your own way Solution

import sys

def printTranspose(num, l):
    for i in range(1,num*2,2):
        t = getTranspose(l[i])
        print("Case #" + str((i+1)//2) + ": " + t)

def getTranspose(s):
    l = list(s)
    for i in range(0,len(l)):
        if l[i] == "S":
            l[i] = "E"
        else:
            l[i] = "S"
    output = ""
    return output.join(l)

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile) -1):
        inputFile[i] = inputFile[i][:-1]
    num = int(inputFile[0])
    inputFile = inputFile[1:]
    printTranspose(num, inputFile)



