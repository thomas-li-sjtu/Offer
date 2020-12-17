# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers: list):
        # write code here
        dict = {}
        if len(numbers) == 0:
            return 0
        elif len(numbers) == 1:
            return numbers[0]
        length = len(numbers)
        for i in numbers:
            if dict.get(i):
                dict[i] = dict[i] + 1
                if dict[i] > length / 2:
                    return i
            else:
                dict[i] = 1
        else:
            print(dict)
            return 0

