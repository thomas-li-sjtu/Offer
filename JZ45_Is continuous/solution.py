# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers: list):
        # write code here
        kings = numbers.count(0)
        numbers = [i for i in sorted(numbers) if i != 0]
        sub = [numbers[i + 1] - numbers[i] - 1 for i in range(len(numbers) - 1)]
        if len(numbers) == 0:  # special case
            return 0
        for i in sub:  # special case
            if i < 0:
                return 0
        if sum(sub) <= kings:
            return 1
        else:
            return 0
