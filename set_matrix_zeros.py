class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        inter_map = [[],[]]

        for i,row in enumerate(matrix):
            for j,val in enumerate(row):
                if(val==0):
                    inter_map[0].append(i)
                    inter_map[1].append(j)
            
        for i in inter_map[0]:
            matrix[i] = [0] * m

        for i in range(0,n):
            for j in inter_map[1]:
                matrix[i][j] = 0
                
