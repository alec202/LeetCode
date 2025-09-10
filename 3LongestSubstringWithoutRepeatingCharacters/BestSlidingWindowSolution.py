# this solution was only achieved after viewing the most optimal solution from neetcodes solutions:
#  https://neetcode.io/solutions/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = 0
        l = 0
        seen = {}
        for r in range(len(s)):
            newc = s[r]
            if newc in seen:
                l = max(l, seen[newc] + 1)
            seen[newc] = r
            ls = max(ls, r - l + 1)
        return ls

""" s = zxbxzf
ls = 3
seen = {z: 4, x: 3, b: 2}
l = 2
r = 4
newc = z

"""