"""
AUTHOR: Abas Farah
"""

import sys

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
    return ll

def printll(ll):
    ptr = LinkedList(0,ll)
    s = "head"
    while(ptr):
        s += " --> " + str(ptr.data)
    print(s)

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    n = int(inputLines[0])

    while(n):
        arr = convertToLL(sti(inputLines[1]))
        solve(arr)
        n-=1

def solve(head):
    print(head)

if __name__ == "__main__":
    main()


