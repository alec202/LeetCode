class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        min_seen = s + t
        min_seen_len = float('inf')
        t_dict = Counter(t)
        t_dict = dict(t_dict)
        # now we have t dictionary
        for i in range(0, len(s)):
            s_dict = {}
            num_matches = 0
            for j in range(i, len(s)):
                char = s[j]
                if char in t_dict:
                    s_dict[char] = s_dict.get(char, 0) + 1
                    if s_dict[char] == t_dict[char]:
                        num_matches += 1
                        if num_matches == len(t_dict):
                            # we have substring
                            min_seen_len = min(len(min_seen), j - i + 1)
                            if min_seen_len != len(min_seen):
                                min_seen = s[i:j + 1]
                else:
                    continue
        return min_seen if min_seen_len != float('inf') else ""
