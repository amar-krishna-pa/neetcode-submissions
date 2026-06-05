class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens) 
        number_stack = []

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for i in range(n):
            if tokens[i] not in operations:
                number_stack.append(int(tokens[i]))
            else:
                second = number_stack.pop()
                
                first = number_stack.pop()
                number_stack.append(operations[tokens[i]](first, second))

            
        return number_stack[-1]
                
    







        
        