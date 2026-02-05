class Solution:
    def isValid(self, s: str) -> bool:
        close_c = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in close_c:
                if stack and stack[-1] == close_c[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False
