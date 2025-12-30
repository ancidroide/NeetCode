class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in words_map:
                words_map[sorted_word] = [word]
            else:
                words_map[sorted_word].append(word)


        return list(words_map.values())
        