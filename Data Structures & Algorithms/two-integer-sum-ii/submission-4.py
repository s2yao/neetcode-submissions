class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_val = numbers[left] + numbers[right]
            if curr_val == target:
                return [left + 1, right + 1]
            elif curr_val > target:
                right -= 1
            else:
                left += 1
        
        return "fuck"