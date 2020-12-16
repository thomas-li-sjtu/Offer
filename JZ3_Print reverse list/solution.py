# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        tmp = []
        if not listNode:  # 要考虑特殊情况!
            return []
        while listNode.next:
            tmp += [listNode.val]
            listNode = listNode.next
        tmp += [listNode.val]
        tmp = tmp[::-1]
        return tmp
