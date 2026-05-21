class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_count  = defaultdict(int)
        s2_count = defaultdict(int)

        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1

        if s1_count == s2_count:
            return True

        for j in range(len(s1), len(s2)):
            s2_count[s2[j]] += 1
            s2_count[s2[j-len(s1)]] -= 1
            if s2_count[s2[j-len(s1)]] == 0:
                s2_count.pop(s2[j-len(s1)])
            
            if s1_count == s2_count:
                return True
            
        return False
        


        

        

                


        

        