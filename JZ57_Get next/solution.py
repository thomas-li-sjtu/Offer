# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        root = pNode
        while root.next:
            root = root.next

        # 中序遍历
        stack, node_list = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            node_list.append(root)
            root = root.right
        # print(node_list)
        for i in range(len(node_list)-1):
            if node_list[i] == pNode:
                return node_list[i+1]

        return None

s = Solution()
a = TreeLinkNode(8)
b = TreeLinkNode(6)
c = TreeLinkNode(10)
d = TreeLinkNode(5)
e = TreeLinkNode(7)
f = TreeLinkNode(9)
g = TreeLinkNode(11)
a.left, a.right = b, c
b.next, b.left, b.right = a, d, e
c.next, c.left, c.right = a, f, g
d.next, e.next = b, b
f.next, g.next = c, c

print(s.GetNext(pNode=a))