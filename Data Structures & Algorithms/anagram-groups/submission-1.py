class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_array = []
        # Time complexity = O(n*mlog(m))
        # Space complexity = O(n*m)
        for i in strs:
            sorted_array.append("".join(sorted(i)))
        
        # Time complexity = O(n)
        # Space complexity = O(n*m)
        str_dict = {}
        for j, sorted_string in enumerate(sorted_array):
            if sorted_string not in str_dict:
                str_dict[sorted_string] = [strs[j]]
            else:
                str_dict[sorted_string].append(strs[j])


        # Time complexity = O(n)
        # Space complexity = O(n)
        return list(str_dict.values())