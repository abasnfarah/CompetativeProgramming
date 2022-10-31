"""
AUTHOR: Abas Farah
"""

import sys
import math

def solve(n, arr):
    print(n,arr)
    # Find the minimum GCD where the cost is n - i + 1

    for i in range(n+1):


def sti(arr):
    return list(map(int,arr.split()))

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    t = int(inputLines[0])
    for i in range(1,t*2,2):
        print(t,inputLines)
        n = int(inputLines[i])
        arr = sti(inputLines[i+1])
        solve(n,arr)

if __name__ == "__main__":
    main()
