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


