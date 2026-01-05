class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closing = {"}": "{", "]": "[", ")": "("}
        for c in s:
            if c in "{([":
                stack.append(c)
            elif c in closing:
                if not stack:
                    return False
                
                if closing[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0