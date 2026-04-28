class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = [[],[],[],[],[],[],[],[],[]]

        for i, j in enumerate(board):
            checker = defaultdict(int)
            for k, a in enumerate(j):
                column[k].append(a)
                if a != '.' and a != ',':
                    if checker[a] == 1:
                        return False
                checker[a] += 1

        for b, j in enumerate(column):
            checker1 = defaultdict(int)
            for a in j:
                if a != '.' and a != ',':
                    if checker1[a] == 1:
                        return False
                checker1[a] += 1

        grid = []

        grid1 = []
        for i in range(3):
            for l in range(3):
                grid1.append(board[i][l])
        grid.append(grid1)

        grid2 = []
        for i in range(3):
            for l in range(3):
                l+= 3
                grid2.append(board[i][l])
        grid.append(grid2)

        grid3 = []
        for i in range(3):
            for l in range(3):
                l+= 6
                grid3.append(board[i][l])
        grid.append(grid3)

        grid4 = []
        for i in range(3):
            i += 3
            for l in range(3):
                grid4.append(board[i][l])
        grid.append(grid4)

        grid5 = []
        for i in range(3):
            i += 3
            for l in range(3):
                l+= 3
                grid5.append(board[i][l])
        grid.append(grid5)

        grid6 = []
        for i in range(3):
            i += 3
            for l in range(3):
                l+= 6
                grid6.append(board[i][l])
        grid.append(grid6)

        grid7 = []
        for i in range(3):
            i += 6
            for l in range(3):
                grid7.append(board[i][l])
        grid.append(grid7)

        grid8 = []
        for i in range(3):
            i += 6
            for l in range(3):
                l+= 3
                grid8.append(board[i][l])
        grid.append(grid8)

        grid9 = []
        for i in range(3):
            i += 6
            for l in range(3):
                l+= 6
                grid9.append(board[i][l])
        grid.append(grid9)

        for b, j in enumerate(grid):
            checker2 = defaultdict(int)
            for a in j:
                if a != '.' and a != ',':
                    if checker2[a] == 1:
                        return False
                checker2[a] += 1

        return True







        
