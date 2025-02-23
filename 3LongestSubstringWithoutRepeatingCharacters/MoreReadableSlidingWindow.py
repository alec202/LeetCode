class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub = 0
        sub = set()
        l = 0
        for r in range(0, len(s)):
            if s[r] in sub:
                while s[r] in sub:
                    sub.remove(s[l])
                    l += 1
            sub.add(s[r])
            longest_sub = max(longest_sub, len(sub))
        return longest_sub

"""
s = "dvdf"
longest = 2
sub = {v, d, f}
l = 1
r = 3

"""
