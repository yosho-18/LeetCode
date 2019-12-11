class Solution:  # O(N^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]


import bisect
import copy
class Solution:  # O(NlogN)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        copy_nums = copy.copy(nums)
        nums.sort()
        for i in range(n):
            x = target - nums[i]
            P = bisect.bisect_left(nums, x)
            Q = bisect.bisect_right(nums, x) - 1
            if P == n:
                continue
            if nums[P] == x:
                if P != i:
                    if nums[i] != nums[P]:
                        return [copy_nums.index(nums[i]), copy_nums.index(nums[P])]
                    else:
                        ans = [m for m, x in enumerate(copy_nums) if x == nums[i]]
                        return ans[:2]
                elif Q != i:
                    if nums[i] != nums[Q]:
                        return [copy_nums.index(nums[i]), copy_nums.index(nums[Q])]
                    else:
                        ans = [m for m, x in enumerate(copy_nums) if x == nums[i]]
                        return ans[:2]


class Solution:   # O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, x in enumerate(nums):
            n = target - x
            if n not in hash:  # O(1)
                hash[x] = i  # 要素xの番号はiであることを格納する
            else:  # nがhに存在する
                return [hash[n], i]