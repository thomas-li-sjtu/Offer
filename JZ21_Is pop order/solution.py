# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []

    def IsPopOrder(self, pushV, popV):
        # write code here
        j = 0
        for i in range(len(pushV)):
            self.stack.append(pushV[i])
            while True:
                if j == len(pushV):
                    return 1
                if pushV[i] == popV[j]:
                    # 压入后马上弹出
                    self.stack.pop()
                    j += 1
                elif self.stack[-1] == popV[j]:
                    # 与栈顶相同
                    self.stack.pop()
                    j += 1
                else:
                    break
        return 0


s = Solution()
print(s.IsPopOrder([1, 2, 3, 4, 5],
                   [4, 5, 3, 2, 1]))
