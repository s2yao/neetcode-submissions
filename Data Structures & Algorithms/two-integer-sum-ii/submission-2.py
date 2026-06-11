class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers

        ptr1 = 0
        ptr2 = len(numbers) - 1

        while ptr1 < ptr2:
            ans = numbers[ptr1] + numbers[ptr2]
            if ans == target:
                return [ptr1 + 1, ptr2 + 1]
            elif ans < target:
                ptr1 += 1
            else:
                ptr2 -= 1
        
        return []