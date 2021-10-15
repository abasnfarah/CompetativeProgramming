class Solution:
    def findCircleNum(self, isConnected):
        #Disjoint Set Init
        root = []
        rank = []
        def find(x):
            # Find using path compression for QuickUnion
            if(x ==root[x]):
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            # Union find using union by rank for QuickUnion
            rootX = find(x)
            rootY = find(y)
            if(rootX != rootY):
                if(rank[rootX] > rank[rootY]):
                    root[rootY] = rootX
                elif(rank[rootY] > rank[rootX]):
                    root[rootX] = rootY
                else:
                    root[rootX] = rootY
                    rank[rootY] += 1
                return True
            return False



        N = len(isConnected)
        root = [i for i in range(N)]
        rank = [1 for i in range(N)]
        count = N
        for i in range(N):
            for j in range(N):
                if i == j: continue
                if(isConnected[i][j]):
                    if(union(i,j)):
                        count-=1

        return count

if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(isConnected)
    sol = Solution()
    print(sol.findCircleNum(isConnected))
