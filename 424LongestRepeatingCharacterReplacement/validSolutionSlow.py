class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ls = 0
        l = 0
        count = {}
        for r in range(0, len(s)):
            char = s[r]
            count[char] = count.get(char, 0) + 1
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            ls = max(ls, r - l + 1)
        return ls
