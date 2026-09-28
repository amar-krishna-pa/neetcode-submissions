class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_dict = {}
        for i in range(len(nums)):
            other_num = target - nums[i]
            if other_num in num_index_dict:
                return [num_index_dict[other_num], i]
            else:
                num_index_dict[nums[i]] = i
            
        