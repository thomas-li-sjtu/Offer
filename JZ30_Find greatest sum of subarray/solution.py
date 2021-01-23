# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        res = len(array) and max(array)
        temp = 0
        for i in array:
            temp = max(i, temp + i)
            res = max(res, temp)
        return res

# dp[i]表示前i个元素的连续子数组的最大和
# dp[i] = max(array[i], dp[i-1]+array[i]) dp[i]表示前i个元素的连续子数组的最大和
