class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        min_stack = []
        res_array = [0 for i in range(n)]

        for i in range(n):
            if i == 0:
                min_stack.append(i)
            
            else:
                while min_stack and temperatures[i] > temperatures[min_stack[-1]]:
                    res_array[min_stack[-1]] = i - min_stack[-1]
                    min_stack.pop()
                min_stack.append(i)

        return res_array


        