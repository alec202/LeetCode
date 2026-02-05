class Solution:
    def isValid(self, s: str) -> bool:
        close_c = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for c in s:
            if c in close_c:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if close_c[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False