from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.pointers(height)

    # O(n^2)
    def naive(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(1, len(height)):
                h = min(height[i], height[j])
                w = j - i
                max_area = max(max_area, h * w)
        return max_area

    # we are always limited by the shorter height
    # we take a gamble and say that reducing length with the shorter height might be beneficial
    # proof by contradiction:
    # Suppose result is not optimal, so there is an l and r that are optimal.
    # Since we only stop when two pointers meet, we must have visited one of them but not the other.
    # let's say we visited l but not r.
    # the pointer at l stops and won't move until
    # the other pointer  is pointing to l, in which case iteration ends and we must have visited r.
    # there is a better rr which caused l to move. But that means l and r are not optimal.
    # both cases arrive at contradiction
    # O(n) time complexity
    def pointers(self, height: List[int]) -> int:
        def area(l, r):
            return min(height[l], height[r]) * (r - l)

        l = 0
        r = len(height) - 1
        max_area = 0
        while l != r:
            max_area = max(max_area, area(l, r))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height))
