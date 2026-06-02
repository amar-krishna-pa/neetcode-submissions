class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        if k == 1:
            return nums

        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])

        l = 0
        for j in range(k, len(nums)):
            if q[0] == l:
                q.popleft()
            l += 1
            
            while q and (nums[q[-1]] < nums[j]):
                q.pop()
            q.append(j)
            res.append(nums[q[0]])
        
        return res


        