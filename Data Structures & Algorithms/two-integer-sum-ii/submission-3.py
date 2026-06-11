class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers
        ptr_left = 0
        ptr_right = len(numbers) - 1

        while ptr_left < ptr_right:
            # if hit, return
            if (numbers[ptr_left] + numbers[ptr_right]) == target:
                return [ptr_left + 1, ptr_right + 1]
            # if target bigger, increase
            elif (numbers[ptr_left] + numbers[ptr_right]) < target:
                ptr_left += 1
            else:
                ptr_right -= 1
        
        return []