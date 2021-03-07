# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead: ListNode):
        # write code here
        if not pHead:
            return None
        data = []
        while pHead.next:
            data.append(pHead.val)
            pHead = pHead.next
        data.append(pHead.val)
        data = [i for i in data if data.count(i) == 1]
        if not data:  # special case：[1,1,1,1,1]
            return None

        tmp = ListNode(data[0])
        pHead = tmp
        for i in range(1, len(data)):
            tmpNode = ListNode(data[i])
            pHead.next = tmpNode
            pHead = pHead.next
        return tmp