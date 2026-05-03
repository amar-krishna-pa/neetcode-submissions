class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            required_number =  target - num
            if required_number in nums_dict:
                return [nums_dict[required_number], i]
            
            nums_dict[nums[i]] = i


            
            




        