# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        nodes = []
        data = []
        _root = root
        nodes.append(_root)
        while nodes:
            data.append(nodes[0].val)
            if nodes[0].left:
                nodes.append(nodes[0].left)
            if nodes[0].right:
                nodes.append(nodes[0].right)
            nodes.pop(0)
        return data