class Solution:
    def earliestAcq(self, logs, n):
        # Initilizing Disjoint set
        root = [i for i in range(n)]
        rank = [1 for i in range(n)]
        groupsOfFreinds = n
        def union(x, y):
            #Union using union-by-rank
            rootX, rootY = find(x), find(y)
            if(rootX != rootY):
                if(rank[rootX] > rank[rootY]): root[rootY] = rootX
                if(rank[rootX] < rank[rootY]): root[rootX] = rootY
                if(rank[rootX] == rank[rootY]):
                    root[rootX] = rootY
                    rank[rootX] +=1
                return True
            return False
        def find(x):
            #Find using path compression
            if(root[x] == x):return x
            root[x] = find(root[x])
            return root[x]

        # Sorts logs O(nlogn)
        logs.sort()
        currTimestamp = -1

        for log in logs:
            if(groupsOfFreinds <= 1): return currTimestamp

            val = union(log[1], log[2])

            if(val): groupsOfFreinds -=1
            currTimestamp = log[0]

        if(groupsOfFreinds <= 1): return currTimestamp

        return -1


if __name__ == "__main__":
    logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
    n = 6
    print(logs, n)
    sol = Solution()
    print(sol.earliestAcq(logs, n))
