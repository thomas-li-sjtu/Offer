# -*- coding:utf-8 -*-
class Solution:
    # 二分查找
    def GetNumberOfK(self, data, k):
        right = len(data)
        left = 0
        for i in range(len(data)):
            mid = int((right+left)/2)
            if data[mid] == k:
                result = 1
                for j in data[mid+1:]:
                    if j == k:
                        result += 1
                    else:
                        break
                for j in data[:mid][::-1]:
                    if j == k:
                        result += 1
                    else:
                        break
                return result
            elif data[mid] < k:
                left = mid
            elif data[mid] > k:
                right = mid
        return 0  # 没有找到
    # 直接遍历
    # def GetNumberOfK(self, data, k):
    #     # write code here
    #     result = 0
    #     for i in data:
    #         if i == k:
    #             result += 1
    #     return result
