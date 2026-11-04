class Solution:
    def checker(self, data):
        data = self.removeDotsAndToInt(data)

        if not data:
            return True

        if max(data) > 9 or min(data) < 1:
            return False

        unique = set(data)
        return len(data) == len(unique)

    def removeDotsAndToInt(self, data):
        ret = [n for n in data if n != "."]
        return [int(n) for n in ret]

    def getSquare(self, board, i, j):
        res = []
        for k in range(3):
            for l in range(3):
                res.append(board[i * 3 + k][j * 3 + l])
        return res

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in board:
            if not self.checker(r):
                return False
        # check cols
        for i in range(9):
            col = []
            for r in board:
                col.append(r[i])
            if not self.checker(col):
                return False
        # check squares
        for i in range(3):
            for j in range(3):
                sq = self.getSquare(board, i, j)
                if not self.checker(sq):
                    return False
        
        return True