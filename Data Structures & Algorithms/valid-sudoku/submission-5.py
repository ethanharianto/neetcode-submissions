class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                elem = board[row][col]
                if elem == ".":
                    continue
                if elem in rows[row]:
                    return False
                rows[row].add(elem)

                if elem in cols[col]:
                    return False
                cols[col].add(elem)


                if elem in boxes[(row // 3, col // 3)]:
                    return False
                boxes[(row // 3, col // 3)].add(elem)
            
        return True


