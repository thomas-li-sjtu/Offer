# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)
        cols = len(matrix[0]) if matrix else 0

        threhold = min(rows / 2, cols / 2)
        result = []
        circle = 0
        if rows == 1:
            return matrix[0]
        while circle * 2 < rows and circle * 2 < cols:
            result += [matrix[circle][i] for i in range(circle, cols - circle)]
            if circle < rows - circle - 1:
                result += [matrix[i][cols - 1 - circle] for i in range(circle + 1, rows - circle)]
            if circle < rows - circle - 1 and circle < cols - circle - 1:
                result += reversed([matrix[rows - circle - 1][i] for i in range(circle, cols - 1 - circle)])
            if circle < rows - circle - 1 and circle < cols - circle - 1:
                result += reversed([matrix[i][circle] for i in range(circle + 1, rows - 1 - circle)])
            circle += 1
        return result

# # -*- coding:utf-8 -*-
# class Solution:
#     # matrix类型为二维列表，需要返回列表
#     def printMatrix(self, matrix):
#         """
#         :param matrix: [[]]
#         """
#         rows = len(matrix)
#         cols = len(matrix[0]) if matrix else 0
#         start = 0
#         ret = []
#         while start * 2 < rows and start * 2 < cols:
#             self.print_circle(matrix, start, rows, cols, ret)
#             start += 1
#         return ret
#
#
#     def print_circle(self, matrix, start, rows, cols, ret):
#         row = rows - start - 1  # 最后一行
#         col = cols - start - 1
#         # left->right
#         for c in range(start, col+1):
#             ret.append(matrix[start][c])
#         # top->bottom
#         if start < row:
#             for r in range(start+1, row+1):
#                 ret.append(matrix[r][col])
#         # right->left
#         if start < row and start < col:
#             for c in range(start, col)[::-1]:
#                 ret.append(matrix[row][c])
#         # bottom->top
#         if start < row and start < col:
#             for r in range(start+1, row)[::-1]:
#                 ret.append(matrix[r][start])
