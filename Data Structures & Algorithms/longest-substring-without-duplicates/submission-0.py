class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        character_dict = defaultdict(int) 
        left = 0
        max_length = 0

        for right in range(len(s)):
            character_dict[s[right]] += 1

            if character_dict[s[right]] > 1:
                while True:
                    character_dict[s[left]] -= 1
                    left += 1

                    if character_dict[s[right]] == 1:
                        break 

            current_sub_string_length = right - left + 1
            max_length = max(max_length, current_sub_string_length)

        return max_length 

            









        