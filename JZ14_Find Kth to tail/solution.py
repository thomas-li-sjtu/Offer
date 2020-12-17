# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head: ListNode, k: int):
        # write code here
        pointer1 = head
        pointer2 = head
        counter = 1
        if k <= 0:  # special case
            return None
        if not head:  # special case
            return head
        while pointer1.next:
            counter += 1
            if counter >= k:
                pointer2 = pointer2.next
            pointer1 = pointer1.next
        if counter < k:  # special case
            return None

        return pointer2
