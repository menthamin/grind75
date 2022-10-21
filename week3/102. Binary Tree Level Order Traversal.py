# 102. Binary Tree Level Order Traversal
# ref: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            level_values = []

            for _ in range(len(q)):
                node = q.popleft()
                level_values.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level_values)

        return ans
