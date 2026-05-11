class Solution:
    def trap(self, height: List[int]) -> int:
        left_max_array = []
        right_max_array = []
        current_max_left = 0
        current_max_right = 0
        total_capacity = 0

        for i in range(0, len(height)):
            left_max_array.append(current_max_left)
            current_max_left = max(current_max_left, height[i])

        for j in range(len(height) - 1, -1, -1):
            right_max_array.append(current_max_right)
            current_max_right = max(current_max_right, height[j])
        right_max_array = right_max_array[::-1]

        for k in range(len(height)):
            max_capacity = min(left_max_array[k], right_max_array[k])
            current_capacity = max_capacity - height[k]
            total_capacity += max(current_capacity, 0)

        return total_capacity



            

        