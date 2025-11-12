class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # turn t to dictionary for O(1) lookup & keeping track of number of times we see
        # each character

        # minSeen = -1
        # for l in range(len(s))
        # reset dictionary for keeping track of the character count
        # for r in
        from collections import Counter
        cDict = Counter(t)
        tCount = dict(cDict)
        minSeen = float("inf")
        l = 0
        windowCount = {}
        have = 0
        need = len(tCount)
        rMin = 0
        lMin = 0
        for r in range(0, len(s)):
            currChar = s[r]
            windowCount[currChar] = windowCount.get(currChar, 0) + 1
            if currChar in tCount and tCount[currChar] <= windowCount[currChar]:
                have += 1
                if have == need:
                    # If we have the correct amount of what we need, let's update our
                    # minSeen and minString
                    minSeen = min(minSeen, (r - l + 1))
                    if minSeen == (r - l + 1):
                        rMin = r
                        lMin = l
                    oldL = l
                    while s[l] not in tCount or oldL == l:
                        windowCount[s[l]] = windowCount[s[l]] - 1
                        if s[l] in tCount:
                            have -= 1
                        l += 1

        return s[lMin:rMin + 1] if minSeen != float('inf') else ""


"""
s = "ADBECODEBANC"
t = "ABC"
l = 2
oldL = 0
windowCount = {A: 0, D: 0}


"""

"""
                for optimized version,
                we do sliding window, but rather than checking every character like done here, we'd start from the first character that we see in our s string that is in our t string. then expand our window from the right side until we get all characters from t with the correct amount, then once we do this, we update our minimum window seen so far. Then we will need to shift our left pointer:
                we will do this by first removing from our window dictionary what the left pointer is currently pointing to, then once it's removed from our windowDictionary, we shift our left pointer right by 1 character:
            l += 1 
            we will keep on removing from our window dictionary and shifting over out left pointer until we get to the next character in the string s that is also in t. Then we start expanding our window from here until we get all of the characters in t. Then we update min again, and resize our window again, and keep repeating. 

    If we hit the end of the string before we get all the characters in t (with the correct amounts), then we will return the empty string like asked. We could do a check on if our min seen window = -1 since -1 wouldn't make sense in this context and we know that we'd never update the minSeen variable to be -1. If we end the loop and minSeen = -1, we return ""
"""

