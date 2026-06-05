class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = defaultdict(int)
        for i in nums:
            nums_dict[i] += 1
            if nums_dict[i] > 1:
                return True
            
        return False