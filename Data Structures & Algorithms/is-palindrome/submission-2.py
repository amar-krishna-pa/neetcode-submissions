class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_string = ''
        for i in range(len(s)):
            if s[i].isalnum():
                final_string += s[i].lower()
            
        l, r = 0, len(final_string) - 1
        while l<=r:
            if final_string[l] == final_string[r]:
                l += 1
                r -= 1
            else:
                return False

        return True

            

        