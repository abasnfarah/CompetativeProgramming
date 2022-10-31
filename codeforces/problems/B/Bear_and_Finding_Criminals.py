"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def solve(n, a, arr):
    # print(n, a, arr)

    i = a-2
    j = a
    count = 0
    if arr[a-1] == 1:
        count += 1

    while(i>=0 and j<len(arr)):
        if arr[i] and arr[j] == 1:
            count += 2
        i-=1
        j+=1

    while(j < len(arr)):
        if arr[j] == 1:
            count += 1
        j+=1

    while(i >=0):
        # print(i)
        if arr[i] == 1:
            count += 1
        i-=1
    print(count)

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    i = sti(inputLines[0])
    n = i[0]
    a = i[1]
    arr = sti(inputLines[1])
    solve(n, a, arr)

if __name__ == "__main__":
    main()
