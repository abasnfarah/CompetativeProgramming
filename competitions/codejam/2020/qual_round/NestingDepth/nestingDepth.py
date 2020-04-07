import sys

def solve(num, l):

    for i in range(num):
        depth = 0
        s = l[i]
        sl = []
        for j in range(len(s)):
            val = int(s[j])
            if val == depth:
                sl.append(s[j])
            elif val > depth:
                for x in range(val-depth):
                    sl.append('(')
                sl.append(s[j])
                depth = val
            else:
                for y in range(depth-val):
                    sl.append(')')
                sl.append(s[j])
                depth = val

        while(depth > 0):
            sl.append(')')
            depth -= 1

        newS = ''.join(sl)
        print("Case #" + str(i+1) + ": " + newS)


if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i].rstrip()
    num = int(inputFile[0])
    inputFile = inputFile[1:]

    solve(num,inputFile)


