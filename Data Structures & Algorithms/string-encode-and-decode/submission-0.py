class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''

        for str_item in strs:
            encoded_string += str(len(str_item)) + '#' + str_item

        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_list = []

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length_of_current_string = int(s[i:j])
            decoded_list.append(s[j+1: j+1+length_of_current_string])
            i = j+1+length_of_current_string
            
        return decoded_list



