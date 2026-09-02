class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l = 0 
        r = row * col - 1 

        while l <= r:
            m = l + (r - l) // 2
            val = matrix[m // col][m % col]  # ← the key line

            if val == target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        return False


        