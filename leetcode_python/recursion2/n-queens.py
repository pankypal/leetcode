class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [-1] * n
        return self.queens(0, n, board)

    def queens(self, curr, n, board):
        if curr == n:
            return 1

        total = 0
        for j in range(n):
            if self.isValidPos(curr, j, board):
                board[curr] = j
                total += self.queens(curr+1, n, board)
                board[curr] = -1

        return total
    
    def isValidPos(self, row, col, board):
        for i in range(row):
            if board[i] == col:
                return False

        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False

        return True

    def nQueens(self, n):
        output = []

        def isValidPosition(board, col):
            # row validation is not needed as we only add one Q per row

            # column validation
            for row in range(len(board)):
                if board[row][col] == 'Q':
                    return False

            # diagonal validation
            deviation = 1
            for row in range(len(board)-1, -1, -1):
                if (col+deviation < n) and board[row][col+deviation] == 'Q':
                    return False

                if (col - deviation >= 0) and board[row][col - deviation] == 'Q':
                    return False

                deviation += 1

            return True

        def dfs(row, board):
            if row == n:
                newBoard = []
                newBoard.extend(board)
                output.append(newBoard)
            else:
                for col in range(n):
                    if isValidPosition(board, col):
                        board.append("."*col + "Q" + "."*(n-col-1))
                        dfs(row+1, board)
                        # backtrack
                        board.pop()

        dfs(0, [])
        return output

        
        
solution = Solution()
print(solution.totalNQueens(4))
print(solution.nQueens(4))