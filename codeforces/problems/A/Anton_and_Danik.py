"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def solve(n, s):
    A = 0
    D = 0
    for c in s:
        if c == 'A': A+=1
        else: D+=1
    if A > D:
        print("Anton")
    elif A == D:
        print("Friendship")
    else:
        print("Danik")
    # print(n, s)

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    n = int(inputLines[0])
    s = inputLines[1]
    solve(n, s)

if __name__ == "__main__":
    main()
