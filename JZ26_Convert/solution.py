# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        nodes, node_list = [], []
        if not pRootOfTree:
            return None

        # 中序遍历，存储节点
        tmp_node = pRootOfTree
        while nodes or tmp_node:
            while tmp_node:
                nodes.append(tmp_node)
                tmp_node = tmp_node.left
            node = nodes.pop()
            node_list.append(node)
            tmp_node = node.right

        # 更改指针方向，注意每次迭代要更换 cur 为下一个节点
        cur = node_list[0]
        for i in range(1, len(node_list)):
            next_node = node_list[i]
            cur.right = next_node
            next_node.left = cur
            cur = next_node
        return node_list[0]
