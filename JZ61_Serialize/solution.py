# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.flag = -1

    def Serialize(self, root):  # 序列化
        # write code here
        if not root:
            return "#,"
        return str(root.val) + "," + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):  # 反序列化
        # write code here
        self.flag += 1
        l = s.split(",")
        if len(s) < self.flag:
            return
        root = None
        if l[self.flag] != "#":
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
