class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key=lambda x: x[0])
        print(cars)
        cars = [(target-pos)/speed for pos, speed in cars]
        print(cars)
        cars_stack = deque()
        for time in cars: 
            while len(cars_stack) and cars_stack[-1]<=time:
                cars_stack.pop()
            cars_stack.append(time)
        return len(cars_stack)