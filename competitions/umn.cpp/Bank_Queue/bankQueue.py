# Kattis Solution 
# Bank Queue

# Greedy Choice:  remove root and remove 
#                 any negative quetimes
#                 maintaining heapq invariant
# O(Nlgn) runtime
import sys
import heapq

# Greedy Choice routine
def bankQueue(num, tl, queue):

    #given queue in heap format
    counter = 0 # keep track of time
    output = 0
    # Remove root then heapify worst
#    i = 0
    print(str(tl) + ' | ' + str(num))
    while((counter <= tl) and (len(queue) > 0)):
        print(queue)
        root = heapq.heappop(queue)
        if(root[0] >= counter):
            print("--")
            print(root)
            print("--")
            output += abs(root[1])
            counter += 1
    print(output)



if __name__=="__main__":
    inputFile = sys.stdin.readlines()
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i][:-1]
    num = int(inputFile[0].split()[0])
    tl = int(inputFile[0].split()[1])
    queue = []
    for i in range(0,num):
        l = inputFile[i+1].split()

        # foramting input
        t = l[0]
        l[0] = l[1]
        l[1] = t
        vals = tuple(map(int, l))
        vals = (vals[0], vals[1]*-1) # Min-Heap so need to negate values

        # Creating Heap
        heapq.heappush(queue,vals)

    bankQueue(num, tl, queue)


