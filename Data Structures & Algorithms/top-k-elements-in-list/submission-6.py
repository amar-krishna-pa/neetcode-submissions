class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        frequency = [[] for _ in range(len(nums)+1)] 

        for n in nums:
            nums_dict[n] = 1 + nums_dict.get(n, 0)

        for num, count in nums_dict.items():
            frequency[count].append(num)

        output_array = []
        for i in range(len(frequency) - 1, -1, -1):
            for item in frequency[i]:
                if len(output_array) == k:
                    break
                output_array.append(item)
                

        return output_array
            

    