class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_dict = {}
        if len(s) != len(t):
            return False
        
        for i in s:
            if i not in character_dict:
                character_dict[i] = 1
            else:
                character_dict[i] += 1
            
        for j in t:
            if j not in character_dict or character_dict[j] == 0:
                return False
            else:
                character_dict[j] -= 1
            
        return True
        