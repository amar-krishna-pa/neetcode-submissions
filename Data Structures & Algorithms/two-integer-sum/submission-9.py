class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            req_num = target - nums[i]
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = {i}
            else:
                nums_dict[nums[i]].add(i)

            if req_num in nums_dict:
                set_to_check = nums_dict[req_num] - {i}
                if set_to_check:
                    return [min(i, next(iter(set_to_check))), max(i, next(iter(set_to_check)))]
            
            




        