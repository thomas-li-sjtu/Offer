# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        result = 0
        carry = 0
        while True:  # 无限循环...
            result = (num1 ^ num2) & 0xffffffff  # 相加
            num2 = num2 & 0xffffffff
            carry = (num1 & num2) << 1  # 进位
            num1, num2 = result, carry
            if carry == 0:
                break
        return result if result <= 0x7fffffff else ~(result ^ 0xffffffff)  # 负数处理
