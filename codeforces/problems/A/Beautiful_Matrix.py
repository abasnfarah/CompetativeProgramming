"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def solve(arr):
    # print(arr)
    # 1. Find 1
    # 2. Go to center
    I = 0
    J = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                I = i+1
                J = j+1
                print(abs(J-3) + abs(I-3))



def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    arr = []
    for i in range(5):
        arr.append(sti(inputLines[i]))
    solve(arr)

if __name__ == "__main__":
    main()
