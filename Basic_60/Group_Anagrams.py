class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        two_strs = [[] for _ in range(len(strs))]
        for two_part, part in zip(two_strs, strs):
            two_part.append(part)
            sort_part = sorted(part)
            two_part.append(sort_part)

        two_strs = sorted(two_strs, key=lambda x: x[1])

        anagram = two_strs[0][1]
        ans = [[]]
        for origin, sorting in two_strs:
            if sorting == anagram:
                ans[-1].append(origin)
            else:
                anagram = sorting
                ans.append([])
                ans[-1].append(origin)

        return ans