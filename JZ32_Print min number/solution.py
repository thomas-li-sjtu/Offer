# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        for i in range(len(numbers)-1):
            for j in range(len(numbers)-1-i):
                if str(numbers[j]) + str(numbers[j+1]) > str(numbers[j+1]) + str(numbers[j]):
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

        return "".join([str(i) for i in numbers])

# 冒泡排序的应用
