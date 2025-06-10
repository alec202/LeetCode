class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = 0
        left = 0
        right = 1
        if len(s) < 2:
            return max(ls, len(s))
        seen = {s[0]: 0}
        ls = 1
        while right < len(s):
            new_c = s[right]
            if new_c in seen:
                old_left = left
                last_seen_c = seen[new_c]
                for i in range(old_left, last_seen_c + 1):
                    seen.pop(s[i], "")
                    if new_c not in seen:
                        left = last_seen_c + 1
                        seen[new_c] = right
                        break
            else:
                seen[new_c] = right
                ls = max(ls, len(seen))
            right += 1
        return ls

"""
advdf
seen = {v: 2, d: 3, f:4}
ls = 3
left = 2
right = 5
new_c = f
old_left = 0
last_seen_c = 1
i = 1
"""