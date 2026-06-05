class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        for j in range(len(nums)):
            req = target - nums[j]
            if req in nums_dict and j != nums_dict[req]:
                return [j, nums_dict[req]]

            
            




        