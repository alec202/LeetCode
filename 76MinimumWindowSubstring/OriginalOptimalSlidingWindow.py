class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        min_seen = (0, 0)
        min_seen_len = float('inf')
        t_dict = Counter(t)
        t_dict = dict(t_dict)
        # now we have t dictionary
        s_dict = {}
        num_matches = 0
        l = 0
        for r in range(0, len(s)):
            char = s[r]
            if char in t_dict:
                s_dict[char] = s_dict.get(char, 0) + 1
                if s_dict[char] == t_dict[char]:
                    num_matches += 1
                    if num_matches == len(t_dict):
                        # we have substring
                        min_seen_len = min(min_seen_len, r - l + 1)
                        if min_seen_len == (r - l + 1):
                            min_seen = (l, r)
                    while num_matches == len(t_dict) or (l < len(s) and s[l] not in t_dict):
                        left_char = s[l]
                        if left_char in s_dict:
                            s_dict[left_char] = s_dict[left_char] - 1
                            if s_dict[left_char] < t_dict[left_char]:
                                num_matches -= 1
                        l += 1
                        if l < len(s) and num_matches == len(t_dict):
                            # we have substring
                            min_seen_len = min(min_seen_len, r - l + 1)
                            if min_seen_len == (r - l + 1):
                                min_seen = (l, r)
            else:
                continue
        return s[min_seen[0]: min_seen[1] + 1] if min_seen_len != float('inf') else ""
