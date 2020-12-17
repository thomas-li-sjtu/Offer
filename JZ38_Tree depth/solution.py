# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preOrderRecursion(self, root: TreeNode, depth: int, data: list):
        if not root:
            data.append(depth)
            depth -= 1
            return
        depth += 1
        self.preOrderRecursion(root.left, depth, data)
        self.preOrderRecursion(root.right, depth, data)

    def TreeDepth(self, pRoot: TreeNode):
        # write code here
        if not pRoot:  # special case
            return 0

        data = []
        self.preOrderRecursion(pRoot, depth=0, data=data)
        return max(data)
