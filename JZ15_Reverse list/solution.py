# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead: ListNode):
        # write code here
        if not pHead:  # special case
            return None
        if not pHead.next:  # special case
            return pHead

        next_node = pHead.next
        pHead.next = None
        last_node = next_node.next
        next_node.next = pHead

        while last_node:
            pHead = next_node
            next_node = last_node
            last_node = last_node.next
            next_node.next = pHead

        return next_node
