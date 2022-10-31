"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def sts(arr):
    return list(map(int,arr.strip()))

def stt(arr):
    return tuple(map(int,arr.split()))[::-1]

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    arr = int(inputLines[0])
    solve(arr)

def solve(arr):
    # print(arr)
    hashset = set()
    count = 0
    while(arr >= 10):
        if arr in hashset: return -1
        else: hashset.add(arr)

        temp = 0
        s = str(arr)
        arr = sts(s)
        arr = sum(arr)
        count += 1
    print(count)


if __name__ == "__main__":
    main()


