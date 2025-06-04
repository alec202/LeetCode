class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ls = 0
        for i in range(0, len(s)):
            seen.add(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
            ls = max(ls, len(seen))
            seen = set()
        return ls

