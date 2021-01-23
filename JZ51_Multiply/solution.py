# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        for i in range(len(A)):
            tmp = A[i]
            A[i] = 1
            result = 1
            for j in A:
                result *= j
            B.append(result)
            A[i] = tmp
        return B
