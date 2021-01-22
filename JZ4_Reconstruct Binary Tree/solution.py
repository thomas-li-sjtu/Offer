# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        lon = len(pre)
        if lon == 0:
            return None
        elif lon == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            # 这一步看似稍微写的有点复杂，但其实只是省了一些中间变量，pre[0]是读取的根节点，tin.index将根节点定位，那么根节点的左子树从1开始，到tin.index+1结束，建议自己在纸上将这部分框出来，就好理解的多了。
            root.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0]) + 1], tin[:tin.index(pre[0])])
            root.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
            return root

# 前序遍历，每次读取的第一个值一定是根节点，可以在中序遍历的序列中找到当前的根节点的位置
# 中序遍历，确定定了一个根节点后，其左边序列就是这个根节点的左子树，右边序列就是其右子树
