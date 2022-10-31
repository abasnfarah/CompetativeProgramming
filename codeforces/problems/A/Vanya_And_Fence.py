"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def solve(n, h, arr):
    w = 0
    for i in range(len(arr)):
        if arr[i] > h:
            w += 1
        w+=1
    print(w)

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    i = sti(inputLines[0])
    h = i[1]
    n = i[0]
    arr = sti(inputLines[1])
    solve(n, h, arr)

if __name__ == "__main__":
    main()
