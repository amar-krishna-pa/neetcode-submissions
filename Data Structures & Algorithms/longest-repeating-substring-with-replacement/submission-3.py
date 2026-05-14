class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_dict = defaultdict(int)
        max_frequency = 0
        res = 0

        l = 0
        for r in range(len(s)):
            character_dict[s[r]] += 1
            max_frequency = max(character_dict.values())

            replacement_characters_needed = (r - l + 1) - max_frequency
            while replacement_characters_needed > k:
                character_dict[s[l]] -= 1
                max_frequency = max(character_dict.values())
                l += 1
                replacement_characters_needed = (r - l + 1) - max_frequency

            res = max(res, (r-l+1))
        
        return res

        



            


        
        