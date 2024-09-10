class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            letter_tracker = [0] * 26
            for i in range(0, len(s)):
                letter_tracker[ord(s[i]) - ord("a")] += 1
                letter_tracker[ord(t[i]) - ord("a")] -= 1
            print(letter_tracker)
            for c in letter_tracker:
                if c != 0:
                    return False
            return True