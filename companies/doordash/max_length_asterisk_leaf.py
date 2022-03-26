"""
      2
     /  \
    5    7
   /    /  \
 *25   14  *15
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None, is_alive=False):
        self.val = val
        self.left = left
        self.right = right
        self.is_alive = is_alive
        
class Solution:
    def maxPathSum(self, root) -> int:
        self.max = float('-inf')
        self.helper(root)
        return self.max
        
    def helper(self, root):
        if root is None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.max = max(root.val + left + right, self.max)
        
        if root.is_alive:
            return root.val
        elif not root.is_alive and root.left is None and root.right is None:
            return 0
        else:    
            return max(left, right) + root.val

n25 = TreeNode(25, None, None, is_alive=True)
n5  = TreeNode(5,  n25,  None, is_alive=False)
n14 = TreeNode(14, None, None, is_alive=False)
n15 = TreeNode(15, None, None, is_alive=True)
n7  = TreeNode(7,  n14,  n15, False)
n2  = TreeNode(2,  n5,   n7, False)

Solution().maxPathSum(root=n2)
