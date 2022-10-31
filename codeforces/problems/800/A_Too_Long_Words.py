"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def solve(arr):
    if len(arr) <= 10:
        print(arr)
    else:
        s = arr[0]
        l = len(arr) - 2
        s += str(l)
        s += arr[-1]
        print(s)

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    n = int(inputLines[0])
    for i in range(1, n+1):
        solve(inputLines[i])

if __name__ == "__main__":
    main()
