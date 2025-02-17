class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub = 0
        sub = {}
        l, r = 0, 0
        for i, char in enumerate(s):
            r = i
            if char in sub:
                sub_len = r - l
                if sub_len > longest_sub:
                    longest_sub = sub_len
                new_l = sub[char] + 1
                for j in range(l, sub[char]):
                    del sub[s[j]]
                sub[char] = i
                l = new_l
            else:
                sub[char] = i

        if len(sub) > longest_sub:
            return len(sub)
        else:
            return longest_sub
"""
s = "abcabcbb"
longest_sub = 3
sub = {w: 5,  }
char = w
i = 5
l = 5
r = 5
new_l = 3
sub_len = 3
"""
s = Solution()
x = s.lengthOfLongestSubstring("abcabcbb")
print(x)