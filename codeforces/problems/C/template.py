"""
AUTHOR: Abas Farah
"""

import sys
from collections import defaultdict
from collections import Counter

cache = defaultdict(int)
cache[1] = 1
cache[0] = 1

def factorial(val):
    if val in cache:
        return cache[val]

    cache[val] = factorial(val-1) * val

    return cache[val]

def sti(arr):
    return list(map(int,arr.split()))

def sts(arr):
    return list(map(int,arr.strip()))

def stt(arr):
    return tuple(map(int,arr.split()))

def sttr(arr):
    return tuple(map(int,arr.split()))[::-1]

class LinkedList:
    def __init__(self, d = 0, n = None):
        self.data = d
        self.next = n

def convertToLL(arr):
    ll = LinkedList()
    ptr = ll

    for i in range(len(arr)):
        t = LinkedList(arr[i])
        ptr.next = t
        ptr = ptr.next
    return ll.next

def printll(ll):
    ptr = ll
    s = "head"
    while(ptr):
        s += " --> " + str(ptr.data)
        ptr = ptr.next
    print(s)

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    n = int(inputLines[0])
    arr = sti(inputLines[1])
    solve(n, arr)

def solve(n, arr):
    print(n, arr)

if __name__ == "__main__":
    main()


