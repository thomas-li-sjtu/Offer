# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        tmp = []
        for i in s:
            if i == " ":
                tmp.append("%20")
            else:
                tmp.append(i)
        return "".join(tmp)
