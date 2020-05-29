class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_char = {"(", "{", "["}
        for s_str in s:
            if s_str in open_char:
                stack.append(s_str)
            else:
                if stack == []:
                    return False
                last = stack[-1]
                if (last == "(" and s_str == ")") or (last == "{" and s_str == "}") or (last == "[" and s_str == "]"):
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False