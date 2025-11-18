class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        - make winDictionary to keep track of the number of t characters we have in our window X
        - make t dictionary to track number of each character in t X
        - have = 0 to track correct # of characters we have in our window
        - need = len(t)
        - nested loop outer loop is l, inner loop is r.
        -X if this char == tDict[char]
            if true, update have += 1
        - if have == need:
            - if false then we keep expanding our window until we hit the end
            - if true then we have a potential new min substring
                - if true, update min sub string, and update tracked indices for min substring
                    - then break from inner loop to cause outer loop to shift forward a character
                    -X check if this char that outer loop, l, points to is in our winDict, if not we skip this iteration using continue statement, and if it is in our winDict we will continue executing the code within this iteration.
                    -X inside inner loop reset the dictionary values to be 0
        - once end of input string s, slice s and return that slice.
        """
        winDict, tDict = {}, {}
        for char in t:
            winDict[char] = 0
            tDict[char] = tDict.get(char, 0) + 1
        # built our winDict and tDict
        have, need = 0, len(t)
        minSub = [-1, -1]
        minSeen = float("inf")
        for l in range(len(s)):
            outerChar = s[l]
            if outerChar not in tDict:
                continue
            for r in range(l, len(s)):
                char = s[r]
                winDict[char] = 1 + winDict.get(char, 0)
                if char in tDict:
                    if tDict[char] == winDict[char]:
                        have += 1
                        if have == need:
                            winSize = r - l + 1
                            minSeen = min(winSize, minSeen)
                            if minSeen == winSize:
                                minSub = [l, r]
                            winDict = {}
                            for char in tDict:
                                winDict[char] = 0
                            break
        return s[minSub[0]: minSub[1] + 1] if minSeen != float("inf") else ""


"""

"""

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
x = sol.minWindow(s, t)
print(x)