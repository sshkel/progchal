from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# empty tree

class Solution:
    def find_height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.find_height(root.left), self.find_height(root.right))

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        # find the height of the tree so we know how many levels are
        # this allows us to create final list that will hold the result
        height = self.find_height(root)

        result = [[] for _ in range(height)]

        level = 0
        queue = deque()
        queue.append((root, level))
        while queue:
            # remove element
            elem, level = queue.popleft()
            # add element to the result list
            result[level].append(elem.val)
            # add children to the queue increasing level
            if elem.left:
                queue.append((elem.left, level + 1))
            if elem.right:
                queue.append((elem.right, level + 1))
        return result


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=-1)
    cur = root
    for i in range(10):
        cur.right = TreeNode(val=i)
        cur = cur.right

    assert sol.levelOrder(root) == [[-1], [0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    print("All done")
