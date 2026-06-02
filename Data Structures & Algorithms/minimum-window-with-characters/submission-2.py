class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1
        t_count = len(t_dict)

        sub_dict = {}
        sub_count = 0
        res, res_count = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            character = s[r]
            
            if character in t_dict:
                sub_dict[character] = sub_dict.get(character, 0) + 1
                if sub_dict[character] == t_dict[character]:
                    sub_count += 1
            
            while sub_count == t_count:
                if (r-l+1) < res_count:
                    res = [l, r]
                    res_count = r-l+1

                character_l = s[l]
                if character_l in t_dict:
                    sub_dict[character_l] = sub_dict.get(character_l, 0) - 1
                    if sub_dict[character_l] < t_dict[character_l]:
                        sub_count -= 1
                l += 1
        
        print('Res: ')
        if res_count ==  float('inf'):
            return ''

        return s[res[0]:(res[1] + 1)]




        



        