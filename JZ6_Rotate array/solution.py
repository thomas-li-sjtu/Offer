# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        return min(rotateArray)

    def minNumberInRotateArray_2(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        if len(rotateArray) == 1:
            return rotateArray[0]
        print(rotateArray)
        cmp = rotateArray[0]
        for j in range(len(rotateArray)-1, -1, -1):
            if rotateArray[j] <= cmp:
                if rotateArray[j-1] <= rotateArray[j]:
                    continue
                else:
                    print(rotateArray[j])
                    return rotateArray[j]

