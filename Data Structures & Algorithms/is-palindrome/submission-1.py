class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1

        modified_string = s.lower()

        while p1 <= p2:
            if not modified_string[p1].isalnum():
                p1 += 1
            elif not modified_string[p2].isalnum():
                p2 -= 1
            elif modified_string[p1] == modified_string[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False

        return True
        