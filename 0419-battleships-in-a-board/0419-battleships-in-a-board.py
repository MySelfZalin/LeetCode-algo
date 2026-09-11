class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == 'X':
                    if column > 0 and board[row][column - 1] == 'X':
                        continue

                    if row > 0 and board[row - 1][column] == 'X':
                        continue
                    res += 1
        return res