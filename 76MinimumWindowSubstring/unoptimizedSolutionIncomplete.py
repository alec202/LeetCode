class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # turn t to dictionary for O(1) lookup & keeping track of number of times we see
        # each character

        # minSeen = -1
        # for l in range(len(s))
        # reset dictionary for keeping track of the character count
            # for r in 
        from collection import Counter
        cDict = Counter(s)
        tCount = dict(cDict)
        minSeen = -1
        for l in range(len(s)):
            windowCount = {}
            for r in range(l, len(s)):
                currChar = s[r]
                windowCount[currChar] = windowCount.get(currChar, 0) + 1
                if currChar in tCount and tCount[currChar] <= windowCount[currChar]:
                    allPresent = False
                    for char in tCount:
                        i
                    allPresent = True
                # if not correct amount in windowCount then break from check
                # do if statement to check if allPresent is True.
                # if allPresent is True then we will break out of the inner loop and update
                # the min window substring

                # if allPresent is false, then we just keep expanding our window like normal

                """
                for optimized version,
                we do sliding window, but rather than checking every character like done here, we'd start from the first character that we see in our s string that is in our t string. then expand our window from the right side until we get all characters from t with the correct amount, then once we do this, we update our minimum window seen so far. Then we will need to shift our left pointer:
                we will do this by first removing from our window dictionary what the left pointer is currently pointing to, then once it's removed from our windowDictionary, we shift our left pointer right by 1 character:
            l += 1 
            we will keep on removing from our window dictionary and shifting over out left pointer until we get to the next character in the string s that is also in t. Then we start expanding our window from here until we get all of the characters in t. Then we update min again, and resize our window again, and keep repeating. 
    
    If we hit the end of the string before we get all the characters in t (with the correct amounts), then we will return the empty string like asked. We could do a check on if our min seen window = -1 since -1 wouldn't make sense in this context and we know that we'd never update the minSeen variable to be -1. If we end the loop and minSeen = -1, we return ""
                """

