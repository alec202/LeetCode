class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ls = 0
        for l in range(len(s)):
            count = {}
            for r in range(l, len(s)):
                char = s[r]
                count[char] = count.get(char, 0) + 1
                most_f = max(count.values())
                result = (r - l + 1) - most_f
                if not (result <= k):
                    r -= 1
                    break
            ls = max(ls, r - l + 1)
        return ls
"""
s = ABBA k = 0
ls = 1
l = 1
count = {B: 2 }
r = 2
char = B
most_f = 2
result = 0

"""
