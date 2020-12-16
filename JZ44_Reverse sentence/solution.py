# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        string = s.split(" ")
        return " ".join(string[::-1])