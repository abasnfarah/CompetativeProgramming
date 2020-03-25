# Abas Farah
# UMN.CPP Kattis Contest 
# A Vicious Pikeman (Easy)
import sys

def getPikeMan(inputFile):
    line1= list(map(int, inputFile[0].split()))
    num = line1[0]
    limit = line1[1]

    line2 = list(map(int, inputFile[1].split()))
    A = line2[0]
    B = line2[1]
    C = line2[2]
    t0 = line2[3]

    t = [0] * num
    t[0] = t0
    for i in range(1,len(t)):

        t[i] = (A*t[i-1] + B)%C + 1

    t.sort()
    j = 0
    maxProb = 0
    time = 0
    pen = 0
    while((j+1) <= num and (time + t[j] <= limit)):
        pen += t[j] + time
        pen = pen % 1000000007
        time += t[j]
        maxProb += 1
        j+=1
    print(str(maxProb) + " " + str(pen))

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i][:-1]

    getPikeMan(inputFile)