class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = []
        suffix_products = []
        final_list = []
        length_of_nums = len(nums)

        for i in range(length_of_nums):
            if i==0:
                prefix_products.append(1)
            else:
                prefix_products.append(prefix_products[len(prefix_products) - 1] * nums[i-1])

        for j in range(length_of_nums - 1, -1, -1):
            if j == length_of_nums - 1:
                suffix_products.append(1)
            else:
                suffix_products.append(suffix_products[len(suffix_products) - 1] * nums[j+1])

        for k in range(0, length_of_nums):
            final_list.append(prefix_products[k] * suffix_products[length_of_nums - 1 - k])
            
            k += 1

        return final_list
        