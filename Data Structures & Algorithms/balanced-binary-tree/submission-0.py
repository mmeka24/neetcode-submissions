# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)


            # its balanced if the left and right subtrees are balanced
            # AND the height between them is less than 
            balanced = (left[0] and right[0] and 
                    abs(left[1] - right[1]) <= 1)

            height = 1 + max(left[1], right[1])

            return [balanced, height]

        res = dfs(root)[0]
        return res

