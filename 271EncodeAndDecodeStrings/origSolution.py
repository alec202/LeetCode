from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += f'{len(word)}_{word}'
        return encoded_string
        # we now have our encoded string

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        list_of_word = []
        len_of_word = ""
        curr_word = ''
        for i in range(0, len(s)):
            if isinstance(len_of_word, str):
                if s[i] == "_":
                    len_of_word = int(len_of_word)
                    continue
                    # we have the length of our word we're building as an int value
                else:
                    len_of_word += s[i]
                    continue
            # now we got the length of the word, we can solve the problem.
            if len_of_word <= 0:
                # at the curr index we have an integer.
                len_of_word = s[i]
                list_of_word.append(curr_word)
                curr_word = ""
            else:
                curr_word += s[i]
                len_of_word -= 1
        list_of_word.append(curr_word)
        return list_of_word

# """
# Encode function:
# strs: ["neet","code","love!@#$%^","you"]
# encoded string: '4_neet4_code10_love!@#$%^3_you'
# """

# """
# Decode Function:
# string to decode: 4_neet4_code10_love!@#$%^3_you
# list_of_word: [neet, ]
# len_of_word: 4
# curr_word: ''
# i: 1

# """
