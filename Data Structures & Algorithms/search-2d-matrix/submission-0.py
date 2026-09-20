class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1
        row = None

        while i <= j:
            row = (i + j) // 2
            if target > matrix[row][-1]:
                i = row + 1
            elif target < matrix[row][0]:
                j = row - 1
            else:
                break

        i, j = 0, len(matrix[0]) - 1

        while i <= j:
            column = (i + j) // 2
            if target > matrix[row][column]:
                i = column + 1
            elif target < matrix[row][column]:
                j = column - 1
            else:
                return True
        
        return False