class Solution:
    def isPalindrome(self, s: str) -> bool:
        phraseFixed = []
        for char in s:
            if char.isalnum():
                phraseFixed.append(char.lower())
        # now we built our array of only alpha numeric characters
        phrase = "".join(phraseFixed)
        # have our phrase as one word.
        return phrase == phrase[::-1]


"""
s = "A man, a plan, a canal: Panama"
char = 
phrase = amanaplanacanalpanama]

"""