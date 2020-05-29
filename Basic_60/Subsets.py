class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [[] for _ in range(2 ** n)]
        for i in range(2 ** n):
            for j in range(n):
                if (i >> j) & 1:
                    ans[i].append(nums[j])
        return ans