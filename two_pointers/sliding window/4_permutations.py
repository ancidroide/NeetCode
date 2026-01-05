class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # no permutation of s1 can be in n s2
        if len(s1) > len(s2):
            return False

        # occurrences freq array for s1
        count_s1 = [0] * 26
        for char in s1:
            count_s1[ord(char) - ord("a")] += 1
        
        # dynamic occurrence hashmap for s2
        count_s2 = [0] * 26
        L = 0
        for R in range(len(s2)):
            # if window len < len(s1) increment R (window width)
            char = s2[R]
            count_s2[ord(char) - ord("a")] += 1
            
            if R - L + 1 > len(s1):
                char_l = s2[L]
                count_s2[ord(char_l) - ord("a")] -= 1
                L += 1
            
            # if window len reaches len(s1) check if count_s1 == count_s2
            if R - L + 1 == len(s1):
                if count_s1 == count_s2:
                    return True

        return False

            
            

        