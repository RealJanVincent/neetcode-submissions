class Solution:
    def searchRow(self, matrix, target, row, start, end):
        if end <= start:
            return False
        elif end - start == 1:
            return matrix[row][start] == target
        else:
            mid = start + (end - start) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                return self.searchRow(matrix, target, row, start, mid)
            else:
                return self.searchRow(matrix, target, row, mid, end)

    def searchMatrixRec(self, matrix, target, start, end):
        if end <= start:
            return False
        elif end - start == 1:
            return self.searchRow(matrix, target, start, 0, len(matrix[start]))
        else:
            mid = start + (end - start) // 2
            if matrix[mid][0] > target:
                return self.searchMatrixRec(matrix, target, start, mid)
            elif matrix[mid][-1] < target:
                return self.searchMatrixRec(matrix, target, mid, end)
            else:
                return self.searchRow(matrix, target, mid, 0, len(matrix[start]))

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchMatrixRec(matrix, target, 0, len(matrix))