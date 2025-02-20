class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if i ==0 and j==0:
                    continue
                elif i==0:
                    self.matrix[i][j] = self.matrix[i][j-1] + self.matrix[i][j]
                elif j==0:
                    self.matrix[i][j] = self.matrix[i-1][j] + self.matrix[i][j]
                else:
                    self.matrix[i][j] = (self.matrix[i-1][j] + self.matrix[i][j-1] + self.matrix[i][j]) - self.matrix[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        end_sum = self.matrix[row2][col2]
        col_sum, row_sum, exc_sum = 0, 0, 0

        if col1==0 and row1==0:
            return end_sum
        if col1 > 0:
            col_sum = self.matrix[row2][col1-1]
#            return end_sum - col_sum
        
        if row1 > 0:
            row_sum = self.matrix[row1-1][col2]
        
        if col1>0 and row1>0:
            exc_sum = self.matrix[row1-1][col1-1]

        return (end_sum - col_sum) - (row_sum - exc_sum)

