class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        valid_set = set(chars)

        while L <= R:
            if s[L].lower() not in valid_set:
                L += 1
                
            elif s[R].lower() not in valid_set:
                R -= 1
                
            else:
                if s[L].lower() != s[R].lower():
                    return False
                
                L += 1
                R -= 1

        return True