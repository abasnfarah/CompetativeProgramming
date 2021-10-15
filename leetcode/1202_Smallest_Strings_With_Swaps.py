"""
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.



Example 1:

  Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Input: s = "dcaeb", pairs = [[0,1], [0,4],[1,2]]
"bcad" --> "bacd" --> "abcd"
"bcad" --> "bacd" --> "abcd"

        d-->c-->a    d->c->b->a
        |               ->e
        |
        v
        b
        "a"
     d c a b e
root[0,1,2,3,4]
root[1,2,2,3,0]
rset = {2,3}
3set = [3]
3arr = [b] = [b]
output = ['a','c','d','b','e'] = 'acdbe'
x = set{}
output[0,1,2,3,4] = "acdb" --> "abcd" --> "acbd" --> "dcbd"

Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
"""
from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        root = [i for i in range(len(s))]
        def find(x):
            if(root[x] == x): return x
            root[x] = find(root[x])
            return root[x]
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if(s[rootX] < s[rootY]): root[rootY] = rootX
            else: root[rootX] = rootY
        for pair in pairs:
            union(pair[0], pair[1])

        roots = defaultdict(list)
        output = [c for c in s]
        for i in range(len(root)):
            val = find(i)
            roots[val].append(i)

        for key,val in roots.items():
            # pop a root and find all there roots
            sortedStr = [s[i] for i in val]
            sortedStr.sort()
            print(sortedStr)
            for i in range(len(sortedStr)):
                output[val[i]] = sortedStr[i]

        return "".join(output)

if __name__ == "__main__":
    pairs = [[0,3],[1,2],[0,2]]
    s = "dcab"
    sol = Solution()
    print(sol.smallestStringWithSwaps(s,pairs))
