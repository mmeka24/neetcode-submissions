# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        if not root:
                return 0 
        
        res = 0
        

        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            res = max(res, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        '''
        
        if not root:
            return 0
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            res = max(res, depth)
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        return res

        '''
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max (left_depth, right_depth )
        '''
        return res

        
