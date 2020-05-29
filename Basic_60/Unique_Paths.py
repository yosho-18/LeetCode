class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        def comb(n, r):
            return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

        return comb(m + n - 2, m - 1)