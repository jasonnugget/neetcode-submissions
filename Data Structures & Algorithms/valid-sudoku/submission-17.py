class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        solRow = defaultdict(list)
        solCol = defaultdict(list)
        solGrid = defaultdict(list)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                if board[row][col] in solRow[row]:
                    return False

                if board[row][col] in solCol[col]:
                    return False

                if board[row][col] in solGrid[((row // 3),(col // 3))]:
                    return False

                solRow[row].append(board[row][col])
                solCol[col].append(board[row][col])
                solGrid[((row // 3),(col // 3))].append(board[row][col])

        return True