class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row: int, column: int, index: int) -> bool:
            if (row < 0 or row >= len(board) or column < 0 or column >= len(board[0])) or board[row][column] != word[index]:
                return False
            
            if index == len(word) - 1:
                return True

            board[row][column] = '#'
            itog = (
                dfs(row + 1, column, index + 1) or
                dfs(row - 1, column, index + 1) or
                dfs(row, column + 1, index + 1) or
                dfs(row, column - 1, index + 1)
            )
            board[row][column] = word[index]

            return itog


        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0]:
                    itog = dfs(row, column, 0)
                    if itog:
                        return True
        return False


        