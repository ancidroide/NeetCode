class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        j = 0

        while i < len(s):
            j = s.find('#', i)
            len_word = int(s[i:j])
            start = j + 1 
            end = start + len_word
            strs.append(s[start:end])
            i = end

        return strs