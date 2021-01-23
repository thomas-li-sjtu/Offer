# -*- coding:utf-8 -*-
class Solution:
    # 堆排序
    def __init__(self):
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def Insert(self, num: int) -> None:
        import heapq
        self.count += 1
        # Python中的堆默认是小顶堆，要传入一个tuple，用于比较的元素需是相反数，以模拟出大顶堆的效果
        heapq.heappush(self.max_heap, (-num, num))
        _, max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))

    def GetMedian(self, a) -> float:
        if self.count & 1:
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return self.max_heap[0][1]
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (self.min_heap[0] + self.max_heap[0][1]) / 2


    # 暴力破解
    # def __init__(self):
    #     self.vals = []
    #
    # def Insert(self, num):
    #     # write code here
    #     self.vals.append(num)
    #     self.vals.sort()
    #
    # def GetMedian(self, a):
    #     # write code here
    #     length = len(self.vals)
    #     if length == 0:
    #         return 0
    #     if length % 2:
    #         return self.vals[int(length / 2)]
    #     return (self.vals[int(length / 2) - 1] + self.vals[int(length / 2)]) / 2
