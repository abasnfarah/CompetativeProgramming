
import sys

def solve(l):
    n = l[1]
    val = l[0]

    for i in range(n):
        if val % 10 == 0:
            val = val//10
        else:
            val -= 1

    return val

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i].rstrip()

    inputFile = inputFile[0].split()
    inputFile = list(map(int,inputFile))
    print(solve(inputFile))

