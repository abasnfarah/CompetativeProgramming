"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def solve(a, b):

    y = 0
    while(a <= b):
        a*=3
        b*=2
        y+=1
    print(y)

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    arr = sti(inputLines[0])
    a = arr[0]
    b = arr[1]
    solve(a, b)

if __name__ == "__main__":
    main()
