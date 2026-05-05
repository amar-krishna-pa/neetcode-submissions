class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = []
        suffix_products = []
        final_list = []

        for i, v in enumerate(nums):
            if i==0:
                prefix_products.append(1)
            else:
                prefix_products.append(prefix_products[len(prefix_products) - 1] * nums[i-1])

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                suffix_products.append(1)
            else:
                suffix_products.append(suffix_products[len(suffix_products) - 1] * nums[j+1])

        for k in range(0, len(nums)):
            final_list.append(prefix_products[k] * suffix_products[len(suffix_products) - 1 - k])
            
            k += 1
        print(final_list)
        return final_list
        