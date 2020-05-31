import sys

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i].rstrip()
    num = int(inputFile[0])
    inputFile = list(map(int, inputFile[1:]))
   


