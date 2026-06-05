class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        number_stack = []

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for t in tokens:
            if t not in operations:
                number_stack.append(int(t))
            else:
                second = number_stack.pop()
                
                first = number_stack.pop()
                number_stack.append(operations[t](first, second))

            
        return number_stack[-1]
                
    







        
        