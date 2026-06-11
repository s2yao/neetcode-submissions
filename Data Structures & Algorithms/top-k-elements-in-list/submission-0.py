class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using a dictionary to wrap it 
        element_dict = defaultdict(int)

        for ele in nums:
            element_dict[ele] += 1

        
        # sorting the element_dict based on second element
        new_dict = dict(sorted(element_dict.items(), key = lambda x: x[1]))

        return list(new_dict.keys())[-k:]
        