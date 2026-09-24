# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.lca = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.hasPQ(root, p, q)
        return self.lca
    
    def hasPQ(self, root: TreeNode, p: TreeNode, q: TreeNode) -> dict:
        if not root:
            return { 'p': False, 'q': False }
        
        left_dict = self.hasPQ(root.left, p, q)
        right_dict = self.hasPQ(root.right, p, q)

        has_p = left_dict.get('p') or right_dict.get('p') or root == p
        has_q = left_dict.get('q') or right_dict.get('q') or root == q

        if has_p and has_q and self.lca == None:
            self.lca = root
        return { 'p': has_p, 'q': has_q }