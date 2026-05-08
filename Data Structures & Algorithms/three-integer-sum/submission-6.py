class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        len_nums = len(nums)
        triplet_list = []

        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len_nums - 1
            while l < r:
                if val + nums[l] + nums[r] > 0:
                    r -= 1
                elif val + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    triplet_list.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            
        return triplet_list

        