# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.inorder_traversal_optimised(root, k)

    # O(n) time and space. We need to traverse all the elements and store them
    def inorder_traversal(self, root: TreeNode, k: int):
        # 1. do inorder traversal on the tree and put items into list
        elems = []

        def traverse(root: TreeNode):
            if root is None:
                return
            traverse(root.left)
            elems.append(root.val)
            traverse(root.right)

        traverse(root)
        # 2. pick kth element from the list
        return elems[k - 1]

    # O(k) time and space. We need to traverse all the elements and store them
    def inorder_traversal_optimised(self, root: TreeNode, k: int):
        # 1. do inorder traversal on the tree and put items into list
        # this time we terminate traversal as soon as we found kth element
        elems = []

        def traverse(root: TreeNode):
            if root is None:
                return
            traverse(root.left)
            # stop traversal once we found kth element
            if len(elems) == k:
                return
            elems.append(root.val)
            traverse(root.right)

        traverse(root)
        # 2. return last element
        return elems[-1]
