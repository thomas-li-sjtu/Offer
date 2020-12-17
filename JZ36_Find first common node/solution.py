# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1: ListNode, pHead2: ListNode):
        # write code here
        length1 = length2 = 0
        _pHead1 = pHead1
        _pHead2 = pHead2
        while _pHead1:
            length1 += 1
            _pHead1 = _pHead1.next
        while _pHead2:
            length2 += 1
            _pHead2 = _pHead2.next

        if length1 > length2:
            tmpHead = pHead1
            for i in range(abs(length1 - length2)):
                tmpHead = tmpHead.next
            for i in range(min(length1, length2)):
                if tmpHead == pHead2:
                    return tmpHead
                else:
                    tmpHead = tmpHead.next
                    pHead2 = pHead2.next
        else:
            tmpHead = pHead2
            for i in range(abs(length1 - length2)):
                tmpHead = tmpHead.next
            for i in range(min(length1, length2)):
                if tmpHead == pHead1:
                    return tmpHead
                else:
                    tmpHead = tmpHead.next
                    pHead1 = pHead1.next
