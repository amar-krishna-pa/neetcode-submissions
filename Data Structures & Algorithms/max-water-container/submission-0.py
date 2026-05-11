class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len_heights = len(heights)
        l = 0
        r = len_heights - 1
        max_water_capacity = 0

        while l < r:
            water_capacity = (r-l) * min(heights[l], heights[r])

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1

            max_water_capacity = max(water_capacity, max_water_capacity)

        return max_water_capacity
            

        