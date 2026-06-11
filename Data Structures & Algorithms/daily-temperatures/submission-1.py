class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # mono stack storing index of days waiting
        ret = [0] * len(temperatures)
        stack = []

        for today in range(len(temperatures)):
            while stack and temperatures[today] > temperatures[stack[-1]]:
                # today is hotter than the day waitng
                ret[stack[-1]] = today - stack[-1]
                stack.pop()

            stack.append(today)
        
        return ret