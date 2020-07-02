'''
	Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]




'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        stack = [(root, 1)]
        while stack:
            node, lvl = stack.pop()
            if node:
                if len(ans) < lvl:
                    ans.append([])
                ans[lvl - 1].append(node.val)
                stack.append((node.right, lvl + 1))
                stack.append((node.left, lvl + 1))
                
        return reversed(ans)