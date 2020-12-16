# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            tmp1 = 1
            tmp2 = 1
            for i in range(n-2):
                if i%2 == 0:
                    tmp1 = tmp1 + tmp2
                else:
                    tmp2 = tmp1 + tmp2
            if n % 2 == 0:
                return tmp2
            else:
                return tmp1