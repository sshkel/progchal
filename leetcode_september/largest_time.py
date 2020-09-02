# Given an array of 4 digits, return the largest 24 hour time that can be made.
#
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
#
# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
from itertools import permutations
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        return self.permutations(A)

    def permutations(self, nums: List[int]) -> str:
        max_time = -1
        for h, i, j, k in permutations(nums):
            hour = h * 10 + i
            minute = j * 10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)

        if max_time == -1:
            return ""
        else:
            return f"{max_time // 60:02d}:{max_time % 60:02d}"


nums = [1, 2, 3, 4]
print(Solution().largestTimeFromDigits(nums))
