# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        n = 0
        k = []
        while True:
            k.append(root.val)
            root = root.left

        for node in range(n):
            tmp = 0
            son1 = 2 * node + 1
            son2 = 2 * node + 2
            if son1 == "null" and son2 == "null":
                tmp += root[node]
                while True:
                    node = (node - 1) // 2
                    tmp += root[node]
                    if node == 0:
                        if tmp == sum:
                            return True
                        tmp = 0
                        break
        return False