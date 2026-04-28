class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first do a row-based search
        i = 0
        j = len(matrix) - 1

        row = 0
        while i <= j:
            row = (i + j) // 2
            if target < matrix[row][0]:
                j = row - 1
            elif target > matrix[row][-1]:
                i = row + 1
            else:
                break
        
        i = 0
        j = len(matrix[row]) - 1
        while i <= j:
            elem = (i + j) // 2
            if target < matrix[row][elem]:
                j = elem - 1
            elif target > matrix[row][elem]:
                i = elem + 1
            else:
                return True
        return False


        