class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        for char_s in s:
            if char_s not in seen_s:
                seen_s[char_s] = 1
            else:
                seen_s[char_s] += 1

        seen_t = {}
        for char_t in t:
            if char_t not in seen_t:
                seen_t[char_t] = 1
            else:
                seen_t[char_t] += 1
        
        if len(seen_s) != len(seen_t):
            return False

        for char in seen_s:
            if char not in seen_t or seen_s[char] != seen_t[char]:
                return False

        return True