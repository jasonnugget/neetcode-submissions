class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        grid = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in grid[i//3, j//3]:
                        return False
                    else:
                        row[i].append(board[i][j])
                        col[j].append(board[i][j])
                        grid[i//3, j//3].append(board[i][j])


        return True