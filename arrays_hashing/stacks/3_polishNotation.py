class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for n in tokens:
            if n not in operators:
                stack.append(int(n))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if n == "+":
                    stack.append(b + a)
                
                elif n == "-":
                    stack.append(b - a)
                
                elif n == "*":
                    stack.append(b * a)

                elif n == "/":
                    stack.append(int(b / a))
        
        return stack[-1]
