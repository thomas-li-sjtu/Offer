# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        if len(s) == 0 or \
                (len(s) == 1 and (str(s[0]) < '0' or str(s[0]) > '9')):
            return 0

        e = 0
        decimal = 0
        sign = 0
        for i in range(len(s)):
            if s[i] == "e" or s[i] == "E":
                # e后面一定要接数字
                if i == len(s) - 1:
                    return 0
                # 不能同时存在两个e
                if e == 1:
                    return 0
                else:
                    e = 1
            elif s[i] == '.':
                # e后面不能接小数点，小数点不能出现两次
                if decimal == 1 or \
                        decimal == 0 and e == 1:
                    return 0
                decimal = 1
            elif s[i] == '+' or s[i] == '-':
                if sign == 1 and (s[i - 1] != 'e' and s[i - 1] != "E"):
                    return 0
                elif sign == 0 and i != 0 and s[i - 1] != 'e' and s[i - 1] != "E":
                    return 0
                sign = 1
            elif '0' > s[i] or s[i] > '9':
                return 0

        return 1

    # 投机方法
    # def isNumeric(self, s):
    #     # write code here
    #     try:
    #         s = float(s)
    #         return True
    #     except:
    #         return False
s = Solution()
print(s.isNumeric("1a3.14"))
