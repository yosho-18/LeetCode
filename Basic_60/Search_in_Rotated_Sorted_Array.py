class Solution:
    def search(self, nums: List[int], target: int) -> int:
        last = len(nums) - 1

        def pivot_search(pre, now, cnt):
            while True:
                if pre > now:
                    pre = (pre + now) // 2
                else:
                    now =
                pre = now
                cnt += 1

        def binary_search():

        pivot = pivot_search(0, last, 0)
        idx = binary_search()

        return idx