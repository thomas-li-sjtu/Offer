# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        trimmed = []
        for i in numbers:
            if i not in trimmed:
                trimmed.append(i)
        counter = [numbers.count(i) for i in trimmed]
        if sum(counter) > len(counter):
            for i in range(len(counter)):
                if counter[i] > 1:
                    duplication[0] = trimmed[i]
                    break
            return True
        else:
            return False