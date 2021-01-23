# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        # 如果两者都为空，则匹配成功
        if len(s) == 0 and len(pattern) == 0:
            return True
        # 如果模式为空，字符串不为空，则匹配不成功
        if len(s) > 0 and len(pattern) == 0:
            return False

        if len(pattern) > 1 and pattern[1] == '*':
            if s and (pattern[0] == '.' or s[0] == pattern[0]):
                f1 = self.match(s[1:], pattern)  # 多个
                f2 = self.match(s[1:], pattern[2:])  # 一个
                f3 = self.match(s, pattern[2:])  # 零个
                if f1 or f2 or f3:
                    return True
                else:
                    return False
            else:
                return self.match(s, pattern[2:])
        elif s and (pattern[0] == '.' or s[0] == pattern[0]):
            return self.match(s[1:], pattern[1:])
            # 如果字符串为空，模式不为空，但模式长度等于1，或者模式长度大于1但第二个字符不为’*‘，则匹配不成功
        else:
            return False
