class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self, pHead, k):
        # write code herep
        if not pHead:
            return pHead
        if k <= 0:
            node = ListNode(0)
            return node.next
        last_node = pHead
        for i in range(k - 1):
            if last_node.next is not None:
                last_node = last_node.next
            else:
                return last_node.next
        while last_node.next is not None:
            last_node = last_node.next
            pHead = pHead.next
        return pHead
