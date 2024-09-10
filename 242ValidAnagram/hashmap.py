class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_hash = {}
            t_hash = {}
            for i in range(0, len(s)):
                vals = s_hash.get(s[i], 0) + 1
                s_hash[s[i]] = vals
                valt = t_hash.get(t[i], 0) + 1
                t_hash[t[i]] = valt
            # built-up our dictionaries with key of letter, value num-of-appearances
            for key in s_hash:
                t_lv = t_hash.get(key, 0)
                if t_lv == 0:
                    return False
                else:
                    if t_lv != s_hash[key]:
                        return False
            return True