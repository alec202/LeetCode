class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        longest = 0
        for i in range(0, len(s)):
            sub.add(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in sub:
                    if len(sub) > longest:
                        longest = len(sub)
                    sub = set()
                    break
                sub.add(s[j])
        return longest if longest > len(sub) else len(sub)


