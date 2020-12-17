# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.array = []
        self.array2 = []

    def push(self, node):
        # write code here
        self.array.append(node)

    def pop(self):
        # return xx
        if self.array2:
            return self.array2.pop()
        while self.array:
            self.array2.append(self.array.pop())
        return self.array2.pop() if self.array2 else u'队列为空'