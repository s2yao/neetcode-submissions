class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = []
        ret = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while mono_stack and temperatures[mono_stack[-1]] < temp:
                ret_idx = mono_stack.pop()
                day_apart = idx - ret_idx
                ret[ret_idx] = day_apart
            
            mono_stack.append(idx)
        
        return ret