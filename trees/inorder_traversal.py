# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Inorder traversal using multiple methods
# Inorder traversal is defined as left, root, right

class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.morris_traversal(root)

    @staticmethod
    # Time complexity O(n)
    # Space complexity O(n)
    def iterative(root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr is not None or len(stack) != 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

    # Time complexity O(n)
    # Space complexity O(n) for worst case, on average it's O(logn), with n being number of nodes
    @staticmethod
    def recursive(root: TreeNode) -> List[int]:
        nodes = []

        def go(root, nodes):
            if root is None:
                return

            go(root.left, nodes)
            nodes.append(root.val)
            go(root.right, nodes)
            return

        go(root, nodes)
        return nodes

    # while curr is not null
    #   if curr.left is null
    #      visitCurrent
    #      curr = curr.right
    #   else:
    #  // find right most node in the left subtree
    #   predecessor = findPredecessor(current)
    #   // if we haven't made this traversal yet
    #   if predecessor.right is null:
    #      # establish temp link to the curr
    #      predecessor.right = curr
    #      curr = curr.left
    #    // we have visited this node already. we are going to break temp link
    #    else:
    #    predecessor.right = null
    #    visitCurrent
    #    curr = curr.right
    # based on explanation from https://www.youtube.com/watch?v=wGXB9OWhPTg

    # Time complexity: O(n)
    # Space complexity O(1) for algorithm itself, if we include returned array it's O(n)

    @staticmethod
    def morris_traversal(root: TreeNode):
        nodes = []
        curr = root
        while curr is not None:
            if curr.left is None:
                nodes.append(curr.val)
                curr = curr.right
            else:
                # find predecessor aka rightmost node in left subtree
                predecessor = curr.left
                while predecessor.right is not None and predecessor.right is not curr:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = curr
                    curr = curr.left
                else:
                    predecessor.right = None
                    nodes.append(curr.val)
                    curr = curr.right
        return nodes
