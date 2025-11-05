class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        biggest = 0
        for i in range(0, len(s)):
            count = {s[i]: 1}
            biggest = max(biggest, 1)
            freq = 1
            for j in range(i+1, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                freq = max(freq, count[s[j]])
                if ((j - i + 1) - freq) > k:
                    break
                else:
                    biggest = max(biggest, j - i + 1)
        return biggest

"""
s = acadd 
k = 2
biggest = 4
i = 1
count = {c: 1,}
j = 2
freq = 2

"""


