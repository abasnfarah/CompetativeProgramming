import sys

def gen(l, A, B):
    output = []
    val = 97
    a = int(A)
    b = int(B)
    for i in range(l):
        output.append(chr(val))
        print(str(a) + " - " + str(b))
        if(b > 1 and a > 1):
           b-=1
           a -= 1
           val += 1
        elif(a > 1):
           a -=1
        elif(a == 1):
           a = int(A)
           b = int(B)
    outputString = ""
    return outputString.join(output)

def solve(num, l):
    for val in l:
        l = val[0]
        a = val[1]
        b = val[2]
        s = gen(l,a,b)
        print(s)

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    num = int(inputFile[0])
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i].rstrip()
        inputFile[i] = inputFile[i].split()
        inputFile[i] = list(map(int, inputFile[i]))
    inputFile = inputFile[1:]

    solve(num,inputFile)



