# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput: list, k):
        # write code here
        if k > len(tinput):
            return []
        tmp = sorted(tinput)
        return tmp[:k]