#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
import collections


class Solution:
    def FindNumsAppearOnce(self, array):
        # write code here
        hash_dict = collections.defaultdict(int)
        for i in array:
            hash_dict[i] += 1
        result = [i for i in hash_dict.keys() if hash_dict[i] if hash_dict[i] == 1]
        return result
