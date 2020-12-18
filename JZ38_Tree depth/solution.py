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


# class Node:
#     def __init__(self, id, anime):
#         self.id = id
#         self.anime = anime
#         self.left = None  # <Left node>
#         self.right = None  # <Right node>
#
#
# def DFS_iterative(node):
#     # Set up a list called nodes_list with `node` being the first and only entry.
#     nodes_list = [node]
#     while True:
#         # If there are no entries in nodes_list, break.
#         if len(nodes_list) == 0:
#             break
#
#         # node = last node in nodes_list.
#         node = nodes_list[-1]
#         # Remove the last node in nodes_list using slicing or list.pop().
#         nodes_list.pop()
#         # Print out the node's anime string.
#         print(node.anime)
#         # If node has a right node, append it to nodes_list.
#         if node.right:
#             nodes_list.append(node.right)
#         # If node has a left node, append it to nodes_list.
#         if node.left:
#             nodes_list.append(node.left)