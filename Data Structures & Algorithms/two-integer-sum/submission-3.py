class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] =  [i]
            else:
                nums_dict[nums[i]].append(i)

        for j in range(len(nums)):
            req_num = target - nums[j]
            if req_num in nums_dict:
                if len(nums_dict[req_num]) == 1 and nums_dict[req_num][0] != j:
                    return [min(nums_dict[req_num][0], j), max(nums_dict[req_num][0], j)]
                elif len(nums_dict[req_num]) > 1 and nums_dict[req_num][1] != j:
                    return [min(nums_dict[req_num][1], j), max(nums_dict[req_num][1], j)]


        