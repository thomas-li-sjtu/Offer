# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True

        stack, result = [pRoot], []
        while stack:
            tmp = stack.pop(0)
            result.append(tmp)
            if tmp:
                stack.append(tmp.left)
                stack.append(tmp.right)

        mirror_stack, mirror_result = [pRoot], []
        while mirror_stack:
            tmp = mirror_stack.pop(0)
            mirror_result.append(tmp)
            if tmp:
                mirror_stack.append(tmp.right)
                mirror_stack.append(tmp.left)
        for i, j in zip(mirror_result, result):
            if i and not j:
                return False
            if j and not i:
                return False
            if not i and not j:
                continue
            if i.val != j.val:
                return False
        return True


