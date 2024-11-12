from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += f'{len(word)}_{word}'
        return encoded_string
        # we now have our encoded string
    # Need to finish bug with decode
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        list_of_word = []
        len_of_word = ""
        index = 0
        while s[index] != '_':
            len_of_word += s[index]
            index += 1
        len_of_word = int(len_of_word)
        curr_word = ''
        for i in range(1, len(s)):
            if len_of_word <= 0:
                len_of_word = int(s[i])
                list_of_word.append(curr_word)
                curr_word = ""
            else:
                curr_word += s[i]
                len_of_word -= 1
        list_of_word.append(curr_word)
        return list_of_word

# """
# Encode function:
# strs: ["neet","code","love","you"]
# encoded string: '4neet4code4love3you'
# """

# """
# Decode Function:
# string to decode: 4neet4code4love3you
# list_of_word: [neet, ]
# len_of_word: 4
# curr_word: 'c'
# i: 6

# """
input = ["we","say",":","yes","!@#$%^&*()"]
sol = Solution()
encoded = sol.encode(input)
print(encoded)
decoded = sol.decode(encoded)
print(decoded)








