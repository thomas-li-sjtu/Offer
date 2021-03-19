# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if (number < 4):
            return number - 1
        x = number / 3
        y = number % 3
        f = [1, 4 / 3.0, 2]
        return pow(3, x) * f[y]

# f(n) = (3 ^ (n / 3)) * f(n % 3) n > 4
# f(0) = 1
# f(1) = 4/3.0
# f(2) = 2