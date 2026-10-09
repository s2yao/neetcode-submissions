class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_arr = [(pos, speed) for pos, speed in zip(position, speed)]
        new_arr.sort()
        curr_time = float("-inf")
        ret = 0
        for car_pos, car_speed in reversed(new_arr):
            time = (target - car_pos) / car_speed
            if time > curr_time:
                curr_time = time
                ret += 1

        return ret