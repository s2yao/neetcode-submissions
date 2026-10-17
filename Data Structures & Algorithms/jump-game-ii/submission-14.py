class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        ret = 0
        can_reach = 0

        for i in range(len(nums) - 1):
            curr_reachable = nums[i] + i
            furthest = max(furthest, curr_reachable)

            if i >= can_reach:
                can_reach = furthest
                ret += 1

                if can_reach >= len(nums) - 1:
                    return ret
        
        return ret