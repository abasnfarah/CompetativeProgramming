# Abas Farah
# UMN.CPP Kattis Contest
# Minimum Scalar Product

import sys

def getMinProduct(num, cases):
    for i in range(num):
        vector1 = list(map(int, cases[i*3 + 1].split()))
        vector2 = list(map(int, cases[i*3 + 2].split()))
        vector1.sort()
        vector2.sort(reverse=True)
        case = 0
        for j in range(0,len(vector1)):
            case += vector1[j] * vector2[j]
        print("Case #" + str(i+1) + ": " + str(case))

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i][:-1]

    num = int(inputFile[0])
    cases = inputFile[1:]
    getMinProduct(num,cases)
