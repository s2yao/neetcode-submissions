class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calculate time to destination
        car = []
        for i in range(len(position)):
            time = float(target - position[i]) / speed[i]
            car.append((position[i], time))
        
        # sort based on position
        car.sort()

        # compute return val
        ret = 0
        fleet_time = 0
        for pos, time in reversed(car):
            if time > fleet_time:
                ret += 1
                fleet_time = time

        return ret