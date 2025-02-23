# this solution was only achieved after viewing the most optimal solution from neetcodes solutions:
#  https://neetcode.io/solutions/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {}
        longest = 0
        l = 0

        for r, char in enumerate(s):
            if char in sub:
                l = max(sub[char] + 1, l)
            sub[char] = r
            longest = max(longest, (r - l + 1))
        return longest

"""
s = "abbacabcbb"
longest = 2
l = 2
r = 3
char = a
sub = {a: 3, b: 2,}
"""
