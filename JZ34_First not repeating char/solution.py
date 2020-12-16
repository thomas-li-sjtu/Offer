# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        string = ''
        for i in s:
            if i not in string:
                string += i

        string_list = list([i for i in string])
        print(string_list)
        times = [s.count(i) for i in string_list]

        if 1 in times:
            char = string_list[times.index(1)]
            return s.index(char)
        else:
            return -1