# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.minStack or node <= self.minStack[-1]:
            self.minStack.append(node)

    def pop(self):
        # write code here
        node = self.stack.pop()
        if node == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minStack[-1]
