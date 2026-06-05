class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        
        if len(s) != len(t):
            return False

        for i in s:
            s_dict[i] = 1 + s_dict.get(i, 0)
        
        for j in t:
            t_dict[j] = 1 + t_dict.get(j, 0)

        for k in s:
            if k not in t_dict:
                return False
            if s_dict[k] != t_dict[k]:
                return False

        return True
        