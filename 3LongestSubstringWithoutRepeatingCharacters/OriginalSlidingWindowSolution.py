class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = 0
        seen = set()
        l = 0
        for r in range(len(s)):
            newc = s[r]
            while newc in seen:
                seen.remove(s[l])
                l += 1
            seen.add(newc)
            ls = max(ls, len(seen))
        return ls

""" s = zxabaf
ls = 4
seen = {b, a, f}
l = 3
r = 6
newc = f

"""