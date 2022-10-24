class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.solve(board)

        #print(board)

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for val in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        if self.isValid(board, val, i, j):
                            board[i][j] = val
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    
                    return False


        return True

    def solveSudoku2(self, board):
        self.solve2(board, 0, 0)
        #print(board)

    def solve2(self, board, row, col):
        m = len(board)
        n = len(board[0])

        if col == n:
            return self.solve2(board, row+1, 0)

        if row == n:
            return True

        if board[row][col] != ".":
            return self.solve2(board, row, col+1)

        for val in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.isValid(board, val, row, col):
                board[row][col] = val

                if self.solve2(board, row, col+1):
                    return True
                else:
                    board[row][col] = "."

        
        return False


    def isValid(self, board, val, row, col):
        for i in range(len(board)):
            if val == board[i][col]:
                return False

        for i in range(len(board[0])):
            if val == board[row][i]:
                return False

        start_row = row

        temp = start_row % 3
        start_row -= temp

        start_col = col
        temp = start_col % 3
        start_col = start_col - temp

        for i in range(start_row, start_row+3):
            for j in range(start_col, start_col+3):
                if board[i][j] == val:
                    return False

        return True




solution = Solution()
solution.solveSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]])
solution.solveSudoku2([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]])