# -*- coding:utf-8 -*-
class Solution:
    # 自底向上
    def jumpFloor(self, number):
        a = 1
        b = 2
        for i in range(3, number):
            if i % 2 == 1:
                a += b
            else:
                b += a
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return a+b
    # 时间复杂度太高
    # def jumpFloor(self, number):
    #     # write code here
    #     if number == 1:
    #         return 1
    #     elif number == 2:
    #         return 2
    #     elif number <= 0:
    #         return -1
    #     else:
    #         return self.jumpFloor(number-1) + self.jumpFloor(number-2)


s = Solution()
print(s.jumpFloor(2))