class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fuck = sorted([[posn, s] for posn, s in zip(position, speed)])
        curr_fucker = 0
        ret = 0
        for bitch in reversed(range(len(fuck))):
            posn, curr_speed = fuck[bitch]
            time = (target - posn) / curr_speed
            if time > curr_fucker:
                ret += 1
                curr_fucker = time
        
        return ret