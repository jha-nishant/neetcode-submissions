import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if n == 1:
            return matrix
        self.swapVertically(matrix)
        print(matrix)
        self.swapDiagonally(matrix)
        print(matrix)
    
    def swapVertically(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        # n = len(matrix)
        # for row in matrix:
        #     half = math.floor(n / 2)
        #     for i in range(half):
        #         val = row[i]
        #         row[i] = row[n - 1 - i]
        #         row[n - 1 - i] = val
    
    def swapDiagonally(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                val = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = val
        count += 1


