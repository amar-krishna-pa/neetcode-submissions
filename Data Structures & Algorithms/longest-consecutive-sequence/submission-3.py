class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers_dict = {}
        for i in nums:
            numbers_dict[i] = []

        biggest_sequence = 0
        for j in nums:
            number_to_check = j + 1
            count = 1
            while True:
                if number_to_check in numbers_dict:
                    numbers_dict[j].append(number_to_check)
                    number_to_check += 1
                    count += 1

                if count > biggest_sequence:
                    biggest_sequence = count

                if number_to_check not in numbers_dict:
                    break
                    
        return biggest_sequence      
        