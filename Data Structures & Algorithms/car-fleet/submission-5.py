class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Two arrays of position and speed, destination at target
        """
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        stack = []
        for p, s in cars:
            time_to_target = (target - p) / s
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
        return len(stack)