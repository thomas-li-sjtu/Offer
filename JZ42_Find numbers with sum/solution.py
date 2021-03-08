# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        front = 0
        end = len(array) - 1
        if end < 0:  # 特殊情况
            return []
        result = [array[end], array[end]]
        while front < end:
            if array[front] + array[end] == tsum:
                if array[front] * array[end] < result[0] * result[1]:
                    result[0], result[1] = array[front], array[end]
                front += 1
                end -= 1
            elif array[front] + array[end] < tsum:
                front += 1
            elif array[front] + array[end] > tsum:
                end -= 1
        if result == [array[len(array) - 1], array[len(array) - 1]]:
            return []
        else:
            return result
    # 初始化：指针i指向数组首， 指针j指向数组尾部
    # 如果arr[i] + arr[j] == sum, 说明是可能解
    # 否则如果arr[i] + arr[j] > sum, 说明和太大，所以 - -j
    # 否则如果arr[i] + arr[j] < sum, 说明和太小，所以 + +i

    # def FindNumbersWithSum(self, array, tsum):
    #     # write code here
    #     array_dict = {i: i for i in array}
    #     result = []
    #     for i in array_dict.keys():
    #         if array_dict.get(tsum-i):
    #             result.append([min(i, tsum-i), max(i, tsum-i)])
    #     if len(result) == 0:
    #         return []
    #     tmp = result[0]
    #     for i in result:
    #         if i[0]*i[1] < tmp[0]*tmp[1]:
    #             tmp = i
    #     return tmp
    # # 要求a + b = sum, 如果已知a， 那么b = sum - a
    # # 可以先将b添加入哈希中，遍历一遍数组设为a， 在哈希中寻找是否存在sum-a，更新乘积最小值
