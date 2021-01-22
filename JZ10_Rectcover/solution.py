# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        res = [0, 1, 2]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[-1]

# 依旧是斐波那契数列
