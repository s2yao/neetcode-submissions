class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) <= 1:
            return [0] * len(temperatures)
        
        ret = []

        # brute force
        for day in range(len(temperatures)):
            i = day
            while i < len(temperatures):
                if temperatures[day] < temperatures[i]:
                    ret.append(i - day)
                    break
                i += 1
            if i == len(temperatures):
                ret.append(0)
        
        return ret

# [30, ]