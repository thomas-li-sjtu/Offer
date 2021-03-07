# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return None
        fast = pHead
        slow = pHead
        while True:
            fast = fast.next
            slow = slow.next
            if fast.next:
                fast = fast.next
            if not fast or fast == slow:
                fast = pHead
                break
        while True:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next

# 初始化：快指针fast指向头结点， 慢指针slow指向头结点
# 让fast一次走两步， slow一次走一步，第一次相遇在C处，停止
# 然后让fast指向头结点，slow原地不动，让后fast，slow每次走一步，当再次相遇，就是入口结点
