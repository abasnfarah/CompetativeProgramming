"""
AUTHOR: Abas Farah
"""

import heapq
import sys

def sti(arr):
    return list(map(int,arr.split()))

def sts(arr):
    return tuple(map(int,arr.split()))[::-1]


def heapSolution(n, m, arr):
    # print(n,m,arr)

    count = 0

    for i in range(len(arr)):
        arr[i] = (-1*arr[i][0],arr[i][1])

    heapq.heapify(arr)
    # print(arr)

    while(len(arr) and n):
        val = heapq.heappop(arr)
        # print(val, n)
        if n >= val[1]:
            count += (-1*val[0]) * val[1]
            n-=val[1]
            continue
        else:
            count += (-1*val[0]) * n
            n = 0
    print(count)

def greedy(n, m, arr):
    print(n,m,arr)

def solve(n, m, arr):
    # greedy(n, m, arr)
    heapSolution(n, m, arr)

def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    i = sti(inputLines[0])
    n = i[0]
    m = i[1]
    arr = []
    for i in range(1, len(inputLines)):
        arr.append(sts(inputLines[i]))
    solve(n, m, arr)

if __name__ == "__main__":
    main()
