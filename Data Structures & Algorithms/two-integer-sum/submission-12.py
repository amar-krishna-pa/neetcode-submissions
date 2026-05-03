class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            required_number =  target - nums[i]
            if required_number in nums_dict:
                return [nums_dict[required_number], i]
            
            nums_dict[nums[i]] = i


            
            




        