class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ls = 0
        l = 0
        count = {}
        mfreq = 0
        for r in range(0, len(s)):
            char = s[r]
            count[char] = count.get(char, 0) + 1
            mfreq = max(mfreq, count[char])
            if (r - l + 1) - mfreq > k:
                count[s[l]] -= 1
                l += 1
            ls = max(ls, r - l + 1)
        return ls

"""
s = AVAf
k = 1
l = 1
ls = 3
seen {a: 1, v: 1, f: 1}
r = 3
c = f
freq_c = a
substring_size = 4
num_swaps = 2
"""
