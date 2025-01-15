class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlNumeric(char: str):
            asciiChar = ord(char)
            if ord('0') <= asciiChar <= ord('9'):
                return True
            elif ord('A') <= asciiChar <= ord('Z'):
                return True
            elif ord('a') <= asciiChar <= ord('z'):
                return True
            else:
                return False

        def lowerChar(char):
            asciiChar = ord(char)
            differenceFromUpperToLowerCase = ord('a') - ord('A')
            if ord('A') <= asciiChar <= ord('Z'):
                return chr(asciiChar + differenceFromUpperToLowerCase)
            else:
                return char

        left = 0
        right = len(s) - 1
        while left < right:
            if not isAlNumeric(s[left]):
                left += 1
                continue
            elif not isAlNumeric(s[right]):
                right -= 1
                continue
            # now it must be pointing at an alpha numeric character.
            if lowerChar(s[left]) != lowerChar(s[right]):
                return False
            left += 1
            right -= 1
        return True


"""
s = "?a.a/"
left = 2
right = 2
"""