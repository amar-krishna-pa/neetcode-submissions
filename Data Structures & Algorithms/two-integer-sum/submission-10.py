class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            required_number =  target - nums[i]

            if required_number in nums_dict:
                return [min(nums_dict[required_number], i), max(nums_dict[required_number], i)]
            
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = i


            
            




        