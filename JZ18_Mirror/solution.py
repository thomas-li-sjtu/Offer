# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return TreeNode类
#
class Solution:
    def Mirror(self, pRoot):
        # write code here
        if not pRoot:
            return
        node_stack = [pRoot]
        while node_stack:
            tmp = node_stack.pop()
            if tmp.left:
                node_stack.append(tmp.left)
            if tmp.right:
                node_stack.append(tmp.right)
            tmp.left, tmp.right = tmp.right, tmp.left
        return pRoot

