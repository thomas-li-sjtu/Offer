# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == [[]]:  # 考虑特殊情况
            return False
        first_num = [(array[i][0],i)  for i in range(len(array))]
        last_num = [(array[i][-1],i)  for i in range(len(array))]
        for i in zip(first_num, last_num):
            if i[0][0] <= target and target <= i[1][0]:
                for j in array[i[0][1]]:
                    if target == j:
                        print("true")
                        return True
        return False