# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0:
            return -1
        rings = [1] * n
        pointer = 0
        for i in range(n-1):
            for j in range(m-1):
                pointer += 1
                if pointer == n:
                    pointer = 0
                while rings[pointer] != 1:
                    pointer += 1
                    if pointer == n:
                        pointer = 0
            rings[pointer] = 0
            while rings[pointer] != 1:
                pointer += 1
                if pointer == n:
                    pointer = 0

        for i in range(len(rings)):
            if rings[i] != 0:
                return i

