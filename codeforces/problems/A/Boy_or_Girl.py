"""
AUTHOR: Abas Farah
"""

import sys

def sti(arr):
    return list(map(int,arr.split()))

def solve(arr):
    # print(arr)
    hashset = set(arr)
    if len(hashset) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


def main():
    inputLines = sys.stdin.readlines()
    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].rstrip()

    # for i in range(len(inputLines)):
        # solve(inputLines[i])

    solve(inputLines[0])

if __name__ == "__main__":
    main()
