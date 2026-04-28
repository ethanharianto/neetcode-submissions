class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first pair each car's position and speed
        cars = [(p, s) for p, s in zip(position, speed)]

        # since a car can not pass another car ahead of it, we sort by decreasing position
        cars.sort(reverse=True)

        # instantiate a stack
        stack = []

        # we add a car to the fleet (keep stack length the same) if its time to target is lower
        # or the same as the top of the stack
        for car in cars:
            p, s = car
            stack.append((target - p) / s)
            while len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)