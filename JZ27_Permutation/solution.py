# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        def join(str, char):
            arr = []
            for i in range(len(str), -1, -1):
                arr.append(str[:i] + char + str[i:])
            return arr

        if len(ss) < 2:  # 特殊情况
            return [ss]

        array = []  # 存储所有字符
        for char in ss:
            array.append(char)
        array.sort()
        ans = [array[0]]
        n = len(array)
        for i in range(1, n):  # ans：[a, [ab, ba], [abc, acb, cab, bac, bca, cba].....]
            array_new = []
            array_last = ans[-1]
            char = array[i]
            for str in array_last:  # array_new: [a], [ab, ba], [abc, acb, cab, bac, bca, cba]....
                array_new = array_new + join(str, char)
            array_new = list(set(array_new))
            array_new.sort()
            ans.append(array_new)
        return ans[-1]
