class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = 0
        for i in range(len(s)):
            lc = s[i]
            seen = set()
            seen.add(lc)
            for j in range(i + 1, len(s)):
                rc = s[j]
                if rc in seen:
                    break
                seen.add(rc)
            ls = max(ls, len(seen))
        return ls

""" s = abaf
ls = 3
i = 3
lc = f
seen = {f}
j = 4
rc = 
"""
