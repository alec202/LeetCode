class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ls = 0
        seen = {}
        for r in range(len(s)):
            new_let = s[r]
            if new_let in seen and seen[new_let] >= l:
                l = seen[new_let] + 1
            seen[new_let] = r
            ls = max(ls, r - l + 1)
        return ls
