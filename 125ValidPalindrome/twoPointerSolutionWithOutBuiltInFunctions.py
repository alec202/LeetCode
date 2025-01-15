class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlNumeric(char: str):
            asciiChar = ord(char)
            if asciiChar in range(48, 58):
                return True
            elif asciiChar in range(65, 91):
                return True
            elif asciiChar in range(97, 123):
                return True
            else:
                return False

        def lowerChar(char):
            asciiChar = ord(char)
            if asciiChar in range(65, 91):
                return chr(asciiChar + 32)
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