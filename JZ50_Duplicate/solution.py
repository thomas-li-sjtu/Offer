# -*- coding:utf-8 -*-
class Solution:

    def duplicate(self, numbers):
        # write code here
        trimmed = set([])
        for i in numbers:
            if i in trimmed:
                return i
            else:
                trimmed.add(i)
        return -1