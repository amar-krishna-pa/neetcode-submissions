class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_dict = {}
        for i in range(len(position)):
            position_speed_dict[position[i]] = speed[i]

        position.sort()
        fleet_count = 0
        time_stack = []
        for j in range(len(position)):
            time = float((target - position[j])/position_speed_dict[position[j]])
            time_stack.append(time)
        
        prev = float('-inf')
        fleet_count = 0
        while time_stack:
            current_time = time_stack.pop()
            if prev < current_time:
                fleet_count += 1
                prev = current_time


        return fleet_count
                 



            

            


        