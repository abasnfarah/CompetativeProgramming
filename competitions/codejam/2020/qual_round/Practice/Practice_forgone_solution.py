# Abas Farah - CodeJam 2020
# Practice round

# Forgone Solution


import sys
import random

def forgone(num, l):
    # Brute Force find numbers from 1 + (val - 1) to 
    # (val//2) + (val//2)
    # O(n) runtime
    for i in range(num):

        pair = findPair(l[i])
        print("Case #" + str(i+1) + ": " + pair[0] + " " + pair[1])

def check4(num):
    s = str(num)
    for i in s:
        if i == '4':
            return True
    return False

def findPair(v):
    pair = ["-1","-1"]
    hashSet = set()
    for i in range(1, (v//2) + 1):
        j = random.randrange(1,v,1)
        if j not in hashSet:
            if not check4(j) and not check4(v-j):
                pair = [str(j),str(v-j)]
                break
    return pair

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i][:-1]
    num = int(inputFile[0])
    inputFile = list(map(int, inputFile[1:]))
    forgone(num, inputFile)
