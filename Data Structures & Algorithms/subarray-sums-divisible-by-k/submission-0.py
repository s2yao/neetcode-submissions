class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ret = 0
        
        for idx, ele in enumerate(nums):
            curr_sum = ele
            if curr_sum % k == 0:
                # print(idx, i, curr_sum)
                ret += 1
            for i in range(idx + 1, len(nums)):
                curr_sum += nums[i]
                if curr_sum % k == 0:
                    print(idx, i, curr_sum)
                    ret += 1

        return ret