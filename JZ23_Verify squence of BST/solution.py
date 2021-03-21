# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        tmp = len(sequence)-1
        count = 0
        while tmp:
            while sequence[count] < sequence[tmp]:
                count += 1
            while sequence[count] > sequence[tmp]:
                count += 1
            if count != tmp:
                return False
            count = 0
            tmp -= 1
        return True

# 遍历的时候，如果遇到比最后一个元素大的节点，就说明它的前面都比最后一个元素小，
# 该元素后面的所有值都必须大于最后一个值，这两个条件必须都要满足。否则就说明该序列不是二叉树后序遍历。
# 例子： 2 4 3 6 8 7 5 这是一个正确的后序遍历