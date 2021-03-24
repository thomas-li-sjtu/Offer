# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or not size:
            return []
        result = []
        length = len(num)-size+1
        for i in range(length):
            max_val = max(num[i:size+i])
            result.append(max_val)
        return result