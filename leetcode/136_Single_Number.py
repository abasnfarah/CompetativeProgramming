class Solution:
    def singleNumber(self, nums):
        singleNumSet = set()
        
        for x in nums:
            if x in singleNumSet:
                singleNumSet.remove(x)
                continue
            singleNumSet.add(x)
        return singleNumSet.pop()

def main():
    nums = [4,1,2,1,2]
    sol = Solution()
    print(sol.singleNumber(nums))

if __name__ == "__main__":
    main()
