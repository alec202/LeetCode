class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        temp_t = Counter(t)
        t_dict = dict(temp_t)
        s_dict = {}
        num_matches = 0
        l = 0
        l_string = 0
        r_string = 0
        min_seen_len = float('inf')
        for r in range(0, len(s)):
            c = s[r]
            if c in t_dict:
                s_dict[c] = s_dict.get(c, 0) + 1
                if s_dict[c] == t_dict[c]:
                    num_matches += 1
                # we updated min string
                while num_matches == len(t_dict):
                    # we have a valid substring
                    if min_seen_len > (r - l + 1):
                        l_string = l
                        r_string = r
                        min_seen_len = (r - l + 1)
                        # we updated min string
                    if s[l] in s_dict:
                        s_dict[s[l]] -= 1
                        if s_dict[s[l]] < t_dict[s[l]]:
                            num_matches -= 1
                    l += 1
        return s[l_string:r_string + 1] if min_seen_len != float('inf') else ""

