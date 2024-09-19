from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        else:
            anagramedWords = {}
            for word in strs:
                sorted_word = "".join(sorted(word))
                if sorted_word in anagramedWords:
                    anagramedWords[sorted_word].append(word)
                else:
                    anagramedWords[sorted_word] = [word]
            # built up our dictionary with key being sorted word: [original_word]
            return anagramedWords.values()



# strs = ["eat","tea","tan","ate","nat","bat"]
# anagramedWords = {aet: [eat, tea], }
# word = tea
# sorted_word = aet