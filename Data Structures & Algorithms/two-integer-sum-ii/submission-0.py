class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            added = numbers[i] + numbers[j]
            if added > target:
                j -= 1
            elif added < target:
                i += 1
            else:
                return [i + 1, j + 1]

