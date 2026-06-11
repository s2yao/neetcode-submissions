class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()  # sort to enable two-pointer technique

        n = len(nums)

        for i in range(n):
            first = nums[i]

            # Since array is sorted, no valid triplet if first > 0
            if first > 0:
                break

            # Skip duplicate values for the first number
            if i > 0 and first == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = first + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    results.append([first, nums[left], nums[right]])

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                    # Skip duplicate values for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return results
