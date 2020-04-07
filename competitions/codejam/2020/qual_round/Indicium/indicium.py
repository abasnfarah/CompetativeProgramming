import sys
from itertools import permutations

def trace(m):
    l = len(m)
    output = 0
    for i in range(l):
       output += m[i][i]
    return output


def countRow(m):
    output = 0
    for i in range(0,len(m)):
        hashset = set()
        for j in range(0,len(m[i])):
            hashset.add(m[i][j])

        if len(hashset) != len(m[i]):
            output += 1
    return output


def countCol(m):
    output = 0
    for i in range(0,len(m[0])):
        hashset = set()
        for j in range(0,len(m)):
            hashset.add(m[j][i])

        if len(hashset) != len(m):
            output += 1
    return output


def solve(num, l):

    rows = []
    matrix = []

    for i in range(len(l)):
        N = int(l[i].split(' ')[0])
        K = int(l[i].split(' ')[1])

        r = [ j for j in range(1,N+1)]
        rows = [list(p) for p in permutations(r)]
        tmatrix = list(map(list,list(permutations(rows, N))))
        matrix = removeM(tmatrix)
        isPossible = False
        outputMatrix = []
        for newM in matrix:
            t = trace(newM)
            if t == K:
                isPossible = True
                outputMatrix = newM
                break

        if isPossible:
            print("Case #" + str(i+1)+": " + "POSSIBLE")
            printM(outputMatrix)
        else:
            print("Case #" + str(i+1)+": " + "IMPOSSIBLE")




def removeM(m):
    output = []

    for i in range(len(m)):
        c = countCol(m[i])
        r = countRow(m[i])

        if c == 0 and r == 0:
            output.append(m[i])

    return output

def printM(m):
    for r in m:
        r = list(map(str,r))
        s = " "
        print(s.join(r))

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i].rstrip()
    num = int(inputFile[0])
    inputFile = inputFile[1:]

    solve(num, inputFile)

