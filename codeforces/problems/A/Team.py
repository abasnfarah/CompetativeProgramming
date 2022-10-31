"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def solve(n, arr):
    output = 0
    for i in range(n):
        if arr[i] >= 2:
            output+=1
    print(output)


def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    n = int(inputLines[0])
    arr = []
    for i in range(1, n+1):
        arr.append(sum(sti(inputLines[i])))
    solve(n, arr)

if __name__ == "__main__":
    main()
