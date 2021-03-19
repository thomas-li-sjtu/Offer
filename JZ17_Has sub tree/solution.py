# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False

        tree1 = [pRoot1]
        flag = 0

        while tree1:
            tmp = tree1.pop(0)
            if tmp.val == pRoot2.val:
                flag = self.subtree(tmp, pRoot2)
            if tmp.left:
                tree1.append(tmp.left)
            if tmp.right:
                tree1.append(tmp.right)
        if flag:
            return True
        else:
            return False

    def subtree(self, tmp, pRoot2):
        tree2 = [pRoot2]
        tree_tmp = [tmp]
        while tree2 and tree_tmp:
            tmp = tree2[0]
            tmp_tree1 = tree_tmp[0]
            if tmp.val != tmp_tree1.val:
                break
            tree2.pop(0)  # 先判别是否相等，再 pop
            tree_tmp.pop(0)  #
            if tmp.left:
                tree2.append(tmp.left)
                if tmp_tree1.left:
                    tree_tmp.append(tmp_tree1.left)
            if tmp.right:
                tree2.append(tmp.right)
                if tmp_tree1.right:
                    tree_tmp.append(tmp_tree1.right)

        if not tree2:
            return 1
        else:
            return 0
