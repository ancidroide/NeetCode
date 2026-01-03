class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        max_len = 0
        seen = set()

        for R in range(len(s)):
            if s[R] in seen:
                while s[R] in seen:
                    seen.remove(s[L])
                    L += 1
            
            seen.add(s[R])  
            current_len = R - L + 1
            if current_len > max_len:
                max_len = current_len

        return max_len