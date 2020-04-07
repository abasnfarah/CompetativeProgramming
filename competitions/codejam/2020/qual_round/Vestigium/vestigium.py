import sys

def buildMatrix(num, l):
    matrix = [None]*num
    i = 0 
    while(i < num):

        subM = []
        m = int(l[0])
        for j in range(1, m+1):
            row = l[j].split(' ')
            row = list(map(int,row))
            subM.append(row)
        matrix[i] = subM
        i+= 1
        l = l[m+1:]
    return matrix

def repRow(r):
    hashSet = set()

    for i in range(0,len(r)):
        hashSet.add(r[i])

    if len(hashSet) != len(r):
        return 1

    return 0

def countCol(m):
    output = 0
    for i in range(0,len(m)):
        hashset = set()
        for j in range(0,len(m)):
            hashset.add(m[j][i])

        if len(hashset) != len(m):
            output += 1
    return output

def trace(m):
    l = len(m)
    output = 0
    for i in range(l):
       output += m[i][i]
    return output

def solve(num, l):
    ml = buildMatrix(num,l)
    for j in range(len(ml)):
        m = ml[j]
        r = 0
        t = trace(ml[j])
        for i in range(len(m)):
            r += repRow(m[i])
        c = countCol(m)
        print("Case #" + str(j+1)+": " + str(t) + " " +str(r) + " " +str(c))


if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i][:-1]
    num = int(inputFile[0])

    inputFile = inputFile[1:]

    solve(num, inputFile)

