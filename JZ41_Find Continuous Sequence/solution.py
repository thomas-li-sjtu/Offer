# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        result = []
        front = 1
        end = 1
        sum = 0
        while front <= tsum / 2:
            if sum < tsum:
                sum += end
                end += 1
            elif sum > tsum:
                sum -= front
                front += 1
            else:
                tmp = [i for i in range(front, end)]
                result.append(tmp)
                sum -= front
                front += 1
        return result

# 初始化，i = 1, j = 1, 表示窗口大小为0
# 如果窗口中值的和小于目标值sum， 表示需要扩大窗口，j += 1
# 否则，如果狂口值和大于目标值sum，表示需要缩小窗口，i += 1
# 否则，等于目标值，存结果，缩小窗口，继续进行步骤2, 3, 4
