class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        count = []

        def all_less_than(arr, skip_idx):
            for idx in range(len(arr)):
                if idx == skip_idx:
                    continue
                if arr[idx] > target[idx]:
                    return False
            return True


        for idx in range(len(target)):
            tar = target[idx]
            found = False
            for triplet in triplets:
                if triplet[idx] == tar and all_less_than(triplet, idx):
                    found = True
                    break
            
            if not found:
                return False
        
        return True
                