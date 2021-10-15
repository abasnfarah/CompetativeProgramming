class Solution:
    def countComponents(self, n, edges):
        root = [i for i in range(n)]
        rank = [1 for i in range(n)]
        count = n
        def find(x):
            if(x == root[x]): return x
            root[x] = find(root[x])
            return root[x]
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if(rootX != rootY):
                if(rank[rootX] > rank[rootY]):root[rootY] = rootX
                if(rank[rootX] < rank[rootY]):root[rootX] = rootY
                if(rank[rootX] == rank[rootY]):
                    root[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False

        for edge in edges:
            x = union(edge[0], edge[1])
            if(x): count -= 1
            #print(root,count)
        return count

if __name__ == "__main__":
    edges = [[0,1],[1,2],[3,4]]
    n = 5
    print(edges)
    sol = Solution()
    print(sol.countComponents(n, edges))
