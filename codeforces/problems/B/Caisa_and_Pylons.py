"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    n = int(inputLines[0])
    arr = sti(inputLines[1])
    solve(n, arr)

def solve(n, arr):
    # print(n, arr)
    e = 0
    m = 0
    p = 0
    prev=0
    while(p < len(arr)):
        # print(m,e,prev,arr[p])
        if e - (arr[p]-prev) < 0:
            m += (arr[p]-prev) - e
            e=0
        else:
            e += prev - arr[p]
        prev = arr[p]
        p+=1
    print(m)


if __name__ == "__main__":
    main()
