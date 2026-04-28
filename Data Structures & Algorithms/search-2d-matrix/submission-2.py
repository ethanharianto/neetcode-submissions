class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        
        while i <= j:
            row = (i + j) // 2
            if matrix[row][0] > target:
                j = row - 1
            elif matrix[row][len(matrix[row]) - 1] < target:
                i = row + 1
            else:
                break 

        row = (i + j) // 2
        row_i = 0
        row_j = len(matrix[row]) - 1
        while row_i <= row_j:
            mid = (row_i + row_j) // 2
            elem = matrix[row][mid]
            if elem < target:
                row_i = mid + 1
            elif elem > target:
                row_j = mid - 1
            else:
                return True
            
        return False

        