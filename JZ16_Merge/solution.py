# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1: ListNode, pHead2: ListNode):
        # write code here
        if not pHead1 or not pHead2:  # special cases
            if not pHead1 and not pHead2:
                return None
            elif not pHead1 and pHead2:
                return pHead2
            elif pHead1 and not pHead2:
                return pHead1

        head = newList = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                tmpNode = ListNode(pHead2.val)
                pHead2 = pHead2.next

                newList.next = tmpNode
                newList = tmpNode
            else:
                tmpNode = ListNode(pHead1.val)
                pHead1 = pHead1.next

                newList.next = tmpNode
                newList = tmpNode

        if not pHead2:
            tmpNode = pHead1
            newList.next = tmpNode
        else:
            tmpNode = pHead2
            newList.next = tmpNode

        return head.next
