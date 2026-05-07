class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers_set = set(nums)
        max_series_count = 0
        
        for i in nums:
            series_count = 0
            if i-1 in numbers_set:
                continue
            else:
                number_to_check = i+1
                series_count =+ 1
                while number_to_check in numbers_set:
                    series_count += 1
                    number_to_check += 1
                
                max_series_count = max(series_count, max_series_count)

        return max_series_count
                    

        

            
        