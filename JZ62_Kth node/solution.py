# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return None
        stack = []
        tmp = pRoot
        while stack or tmp:  # 栈为空，或遍历到空节点
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            tmp = stack.pop()
            k -= 1
            if k == 0:
                return tmp
            tmp = tmp.right
        return None


# 二叉树的中序遍历就是节点值的递增顺序
# （1）访问节点P，并将节点P入栈
# （2）判断节点P的左孩子是否为空，若为空，则取栈顶节点并进行出栈操作，并将栈顶节点的右孩子置为当前的节点P,循环至1;
#     若不为空，则将P的左孩子置为当前的节点P
# （3）直到P为NULL并且栈为空，则遍历结束
