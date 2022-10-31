"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def solve(n, arr):
    # print(n, arr)

    output = 0
    # 1. For every input go to right and left till it's not monotomically decreasing
    for i in range(len(arr)):
        p = i+1
        r = i-1
        m = arr[i]
        n = arr[i]
        count = 1
        while(r > -1 or p < len(arr)):
            if r > -1:
                if arr[r] <= m:
                    count += 1
                    m = arr[r]
                    r-=1
                else:
                    r = -1
            if p < len(arr):
                if arr[p] <= n:
                    count += 1
                    n = arr[p]
                    p+=1
                else:
                    p = len(arr)
        output = max(count, output)
    print(output)


def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    n = int(inputLines[0])
    arr = sti(inputLines[1])
    solve(n, arr)

if __name__ == "__main__":
    main()
