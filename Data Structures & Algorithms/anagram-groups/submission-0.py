class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_array = []
        for i in strs:
            sorted_array.append("".join(sorted(i)))
        
        str_dict = {}
        for j, sorted_string in enumerate(sorted_array):
            if sorted_string not in str_dict:
                str_dict[sorted_string] = [strs[j]]
            else:
                str_dict[sorted_string].append(strs[j])

        return list(str_dict.values())