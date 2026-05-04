class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for s in strs:
            key_array = [0] * 26
            for i in s:
                key_array[ord(i) - ord('a')] += 1
            if tuple(key_array) not in str_dict:
                str_dict[tuple(key_array)] = [s]
            else:
                str_dict[tuple(key_array)].append(s)

        return list(str_dict.values())

