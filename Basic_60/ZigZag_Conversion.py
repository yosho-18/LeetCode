class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        mod = 2 * numRows - 2
        all_len = len(s)
        output = [[] for _ in range(numRows)]
        for num, s_str in enumerate(s):
            k = min(mod - num % mod, num % mod)
            output[k].append(s_str)

        ans = ""
        for out in output:
            ans += "".join(out)

        return ans