class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1

        sorted_nums_dict = sorted(nums_dict, key=lambda x: nums_dict[x], reverse=True)
        
        return sorted_nums_dict[0:k]
        