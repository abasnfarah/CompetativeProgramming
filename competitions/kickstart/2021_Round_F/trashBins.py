import sys

# This function updates the surrounding 1's with distances from a 1. Only updates if current distance is > newDistance
def propagate(caseNum, arr):
    distanceArr = [float('inf')] * len(arr)
    
    # Left Pass
    count = float('inf')
    for i in range(len(arr)):
        if arr[i] == 1:
            distanceArr[i] = 0
            count = 1
        else:
            distanceArr[i] = min(distanceArr[i], count)
            count+=1

    # Right Pass
    count = float('inf')
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 1:
            distanceArr[i] = 0
            count = 1
        else:
            distanceArr[i] = min(distanceArr[i], count)
            count+=1


    output = 0
    for val in distanceArr:
        if val == float('inf'): continue
        output += val
    # print("------------")
    print("Case #" + str(caseNum) + ": " + str(output))
    # 100100
    # 0, 1, 2, 0, 1, 2
    # 0, 1, 1, 0, 1, 2 1 + 1+ 1+ 2 = 5
    # print(arr, distanceArr, output)
    # print("------------")

def trashBins(inputFile):
    # print(inputFile)
    N = int(inputFile[0])
    for i in range(1,N+1):
        # print(inputFile[(i*2)-1],inputFile[(i*2-1)+1])
        propagate(i, list(map(int,list(inputFile[(i*2-1)+1]))))

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i].rstrip()

    trashBins(inputFile)


