from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        ans = 1
        alphabet_dict = defaultdict(lambda: -2)
        alphabet_dict[s[0]] = 0
        last = -1
        cnt = 0

        for i, s_str in enumerate(s[1:], 1):
            if alphabet_dict[s_str] >= last:  # s_str in pre_str:
                # ans = max(ans, i - alphabet_dict[s_str], alphabet_dict[s_str] - last + 1)
                ans = max(ans, i - last - 1)
                last = alphabet_dict[s_str]
            elif i == len(s) - 1:
                ans = max(ans, i - last)
            alphabet_dict[s_str] = i

        return ans