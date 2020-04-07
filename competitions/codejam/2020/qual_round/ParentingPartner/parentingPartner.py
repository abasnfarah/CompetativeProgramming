import sys
import heapq

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


def solve(num, l):
    # Build min-Heap with tuple key (time1, time2)
    matrixTable = buildMatrix(num, l)

    for i in range(len(matrixTable)):
        heap = list(matrixTable[i])
        indexTable = list(matrixTable[i])
        hashmap = {}

        for j in range(len(indexTable)):
            hashmap[tuple(indexTable[j])] = []


        cjtable = {"C" : (-1,-1),"J" : (-1,-1)}
        heapq.heapify(heap)
        outputString = ""

        # Compare top node to c and j
        # if node >= c and j end values then update 
        # output string and cjtable 
        # otherwise it's impossible

        while(heap):
            node = heapq.heappop(heap)
            if node[0] >= cjtable["C"][1]:
                hashmap[tuple(node)].append("C")
                cjtable["C"] = tuple(node)
            elif node[0] >= cjtable["J"][1]:
                hashmap[tuple(node)].append("J")
                cjtable["J"] = tuple(node)
            else:
                outputString = "IMPOSSIBLE"
                break
        if outputString != "IMPOSSIBLE":
            for x in range(len(indexTable)):
                outputString += hashmap[tuple(indexTable[x])].pop()

        print("Case #" + str(i+1) + ": " + outputString)

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i].rstrip()
    num = int(inputFile[0])
    inputFile = inputFile[1:]
    solve(num, inputFile)


