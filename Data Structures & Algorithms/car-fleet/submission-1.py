class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time takes for each to arrive
        # (time_to_arrive, posn)
        cars = []
        for i in range(len(speed)):
            curr_time = (target - position[i]) / speed[i]
            cars.append((position[i], curr_time))
            

        # sort the cars so every element can find its consective idx
        cars.sort()

        # calculate fleet numer
        fleet = 0
        curr_fleet_time = 0
        for car in reversed(cars):
            curr_car_finishtime = car[1]
            # new fleet
            if curr_car_finishtime > curr_fleet_time:
                curr_fleet_time = curr_car_finishtime
                fleet += 1
        
        return fleet

