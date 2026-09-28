class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        count_dict = {}
        for ch in s:
            if ch in count_dict:
                count_dict[ch] += 1
            else:
                count_dict[ch] = 1

        for ch in t:
            if ch in count_dict and count_dict[ch] > 0:
                count_dict[ch] -= 1
            else:
                return False

        return True
