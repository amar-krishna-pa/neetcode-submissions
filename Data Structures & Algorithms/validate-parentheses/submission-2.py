class Solution:
    def isValid(self, s: str) -> bool:
        close_bracket_dict = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i not in close_bracket_dict:
                stack.append(i)
            else:
                if stack and close_bracket_dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False

        