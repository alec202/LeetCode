class Solution:
    def isPalindrome(self, s: str) -> bool:
        phraseFixed = []
        for c in s:
            if c.isalnum():
                phraseFixed.append(c.lower())
        # we've built up our phrase array of only alpha numeric characters.
        phrase = "".join(phraseFixed)
        left = 0
        right = len(phrase) - 1
        while left < right:
            if phrase[left] != phrase[right]:
                return False
            left += 1
            right -= 1
        return True



"""
s = "A ma"
phrase = ama
left = 1
right = 1
"""