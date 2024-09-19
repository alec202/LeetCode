from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        else:
            anagramed_words = {}
            for word in strs:
                num_letters = [0 for i in range(26)]
                for letter in word:
                    letter_index = (ord(letter) - ord("a"))
                    current_count = num_letters[letter_index]
                    num_letters[letter_index] = (current_count + 1)
                    # have num_letters built up
                joined_count = tuple(num_letters)
                if joined_count in anagramed_words:
                    anagramed_words[joined_count].append(word)
                else:
                    anagramed_words[joined_count] = [word]

            return anagramed_words.values()

s = Solution()

print(s.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))