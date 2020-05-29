class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        front = -1
        back = len(nums)
        while abs(front - back) > 1:
            mid = (front + back) // 2
            if target <= nums[mid]:
                back = mid
            else:
                front = mid
        return back