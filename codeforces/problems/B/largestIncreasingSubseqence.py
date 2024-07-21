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

    for i in range(1, n+1):
        arr = convertToLL(sti(inputLines[i]))
        solve(arr)

def solve(head):
    # printll(head)
    i = 0
    j = 0
    m = -1

    ptr = head
    start = head
    end = head
    temp = head
    prev = head

    while(ptr):
        if prev.data < ptr.data:
            if j - i  > m:
                end = prev
                start = temp
                temp = ptr
                m = j-i
            else:
                temp = ptr

            j = 0
            i = 0

        prev = ptr
        ptr = ptr.next
        j+=1

    if j- i > m:
        end = prev
        start = temp

    ptr = head

    while(ptr.next != start):
        ptr = ptr.next

    ptr.next = None
    end.next = None
    printll(start)




if __name__ == "__main__":
    main()


