"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def solve(n, arr):
    # print(n, arr)
    arr.sort()
    s = ' '.join(map(str,arr))
    print(s)

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    n = int(inputLines[0])
    arr = sti(inputLines[1])
    solve(n, arr)

if __name__ == "__main__":
    main()
