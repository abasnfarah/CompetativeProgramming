import sys
import heapq

def festival(val, arr):
    heap = []
    days = val[0]

    while(days):
        output = 0
        totalHapiness = []
        for i in range(len(arr)):
            if arr[i][1] <= days and days <= arr[i][2]:
                heapq.heappush(totalHapiness, arr[i][0] * -1)
        if len(totalHapiness) > 0:
            k = val[2]
            while(k and len(totalHapiness)):
                output += (heapq.heappop(totalHapiness) * -1)
                k-=1
        if output> 0:
            heapq.heappush(heap, output* -1)
        days-=1
    return heapq.heappop(heap)*-1



def festivalCases(inputFile):
    arr = []
    i = 1
    offset = 2
    while(i <= int(inputFile[0])):
        l = []
        values = list(map(int, inputFile[offset-1].split(" ")))

        for j in range(values[1]):
            l.append(list(map(int, inputFile[j+offset].split(" ")))) 

        offset += values[1] + 1 

        val = festival(values, l)
        print("Case #" + str(i) + ": " + str(val))
        i+=1

if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i].rstrip()

    festivalCases(inputFile)



