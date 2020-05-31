import sys

def solve(num, l):
    for v in l:
        if (v % 2 == 0):
            print((v//2 -1))
        else:
            print(v//2)

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i].rstrip()
    num = int(inputFile[0])
    inputFile = list(map(int, inputFile[1:]))
    solve(num,inputFile)



