class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        # mono deque
        max_idx = deque()
        
        # seed initial k
        for i in range(k):
            while max_idx and nums[max_idx[-1]] < nums[i]:
                max_idx.pop()
            max_idx.append(i)
        
        ret.append(nums[max_idx[0]])

        # atp max_idx in decreasing order

        for r in range(k, len(nums)):
            # discard left element if max is discard
            if max_idx[0] <= r - k:
                max_idx.popleft()
            
            # discard right element
            # always decreasing order to record the needed potential maxes
            while max_idx and nums[max_idx[-1]] < nums[r]:
                max_idx.pop()
            
            max_idx.append(r)

            ret.append(nums[max_idx[0]])
        
        return ret