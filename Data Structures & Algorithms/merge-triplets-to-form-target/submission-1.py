class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # unable to laote current indx
        # current idx have target, but have other idx containing. > other idxes

        found = [False] * len(target)
        # iterate through all the trips
        for triplet in triplets:
            valid = True
            for curr_val, target_val in zip(triplet, target):
                # if curr val bigger than target
                if curr_val > target_val:
                    valid = False
                    break
                
            if valid:
                for idx, (curr_val, target_val) in enumerate(zip(triplet, target)):
                    if curr_val == target_val:
                        found[idx] = True


        for result in found:
            if not result:
                return False
        
        return True