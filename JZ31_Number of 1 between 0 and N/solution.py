# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        num = [str(i) for i in range(1, n+1)]
        return sum([i.count('1') for i in num])
# 数学统计问题
