class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c_map = {}
        max_freq = 0
        L = 0
        longest_s = 0

        for R in range(len(s)):
            if s[R] not in c_map:
                c_map[s[R]] = 1
            else:
                c_map[s[R]] += 1
            
            max_freq = max(max_freq, c_map[s[R]])

            if R - L + 1 - max_freq > k:
                c_map[s[L]] -= 1 
                L += 1

            longest_s = max(longest_s, R - L + 1)

        return longest_s