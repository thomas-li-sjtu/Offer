# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# class Solution:
#     # 返回 RandomListNode
#     def Clone(self, pHead):
#         # write code here
#         import copy
#
#         return copy.deepcopy(pHead)

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        cur = pHead

        # 字典存储链表，以及链表节点之间的映射
        node_dict = {}
        while cur:
            node_dict[cur] = RandomListNode(cur.label)
            cur = cur.next

        # 连接新的链表
        cur = pHead
        while cur:
            node_dict[cur].next = node_dict.get(cur.next)
            node_dict[cur].random = node_dict.get(cur.random)

            cur = cur.next

        return node_dict[pHead]