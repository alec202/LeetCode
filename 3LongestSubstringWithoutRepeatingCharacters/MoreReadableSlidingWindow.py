class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = 0
        l = 0
        pos = {}
        for r in range(len(s)):
            newc = s[r]
            if newc in pos and l <= pos[newc] < r:
                l = pos[newc] + 1
            pos[newc] = r
            ls = max(ls, r - l + 1)
        return ls

""" s = nabaf
ls = 3
l = 1
pos = {a: 2, b: 1, f: 3}
r = 3
newc = f 
"""
