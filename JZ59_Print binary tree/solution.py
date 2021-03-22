# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        que = [(pRoot, 0)]
        result_dict = {}
        while que:
            tmp, layer = que.pop(0)
            if tmp.left:
                que.append((tmp.left, layer + 1))
            if tmp.right:
                que.append((tmp.right, layer + 1))

            if result_dict.get(layer):
                result_dict[layer].append(tmp.val)
            else:
                result_dict[layer] = [tmp.val]

        result = [list(value) if key % 2 == 0 else list(value)[::-1] for key, value in result_dict.items()]
        return result

