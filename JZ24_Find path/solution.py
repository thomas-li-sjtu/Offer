# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []

        paths = []
        tmp_route = [(root, [root.val])]
        while tmp_route:
            tmp_node, path = tmp_route.pop()
            if tmp_node.left:
                tmp_route.append((tmp_node.left, path + [tmp_node.left.val]))
            if tmp_node.right:
                tmp_route.append((tmp_node.right, path + [tmp_node.right.val]))
            if not tmp_node.left and not tmp_node.right and sum(path) == expectNumber:
                paths.append(path[:])

        paths = sorted(paths)
        return sorted(paths)