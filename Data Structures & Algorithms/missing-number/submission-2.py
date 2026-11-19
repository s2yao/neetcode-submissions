# # 000
# 001
# 010
# 011
# 100
# 101

# # total = 5
# # 0: 4, 4, 4
# # 1, 2, 2, 3

# # 010

# 000



# and or xor



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        fuck = 0
        for i, num in enumerate(nums):
            fuck ^= i ^ num
        fuck ^= len(nums)
        return fuck