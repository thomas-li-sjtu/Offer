# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.data = []
        self.once = []
        self.dict = {}

    def FirstAppearingOnce(self):
        # write code here
        return self.once[0] if len(self.once) != 0 else '#'

    def Insert(self, char):
        # write code here
        if self.dict.get(char):
            self.dict[char] = self.dict[char] + 1
            if self.dict[char] == 2:
                self.once.remove(char)
        else:
            self.dict[char] = 1
            self.once.append(char)
        return self.FirstAppearingOnce()

# s = Solution()
# print(s.Insert('g'))
# print(s.Insert('o'))
# print(s.Insert('o'))
# print(s.Insert('g'))
# print(s.Insert('l'))
# print(s.Insert('e'))
