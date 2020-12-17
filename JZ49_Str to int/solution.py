# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s: str):
        # write code here
        try:
            f = float(s)
            if f == int(f):
                f = int(f)
            return f
        except:
            return 0
