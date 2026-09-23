# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.root = []

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        out = False
        self.findroot(root, subRoot)
        for node in self.root:
            out = out or self.isSameTree(node, subRoot)
        return out

    def findroot(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> None:
        if not root:
            return

        if root.val == subRoot.val:
            self.root.append(root)
        left = None
        if root.left:
            left = self.findroot(root.left, subRoot)

        right = None
        if root.right:
            right = self.findroot(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and not q:
            return False
        
        if q and not p:
            return False
        
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right
        