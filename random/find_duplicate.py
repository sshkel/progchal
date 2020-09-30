from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.sets(nums)

    # makes assumption that one duplicate always exists
    # O(nlogn) - time complexity
    def dumb_sort(self, nums: List[int]):
        nums_sorted = sorted(nums)
        for i in range(len(nums)):
            if nums_sorted[i] == nums_sorted[i + 1]:
                return nums_sorted[i]

    # python sets are implemented as hashtables
    # check whether set contains the element is done in O(1) on average
    # thus makes our solution O(N)
    def sets(self, nums: List[int]):
        result = set()
        for num in nums:
            if num in result:
                return num
            result.add(num)
    # O(n) time
    def difference(self, nums: List[int]):
        n = len(nums) - 1
        # find the sum of numbers using gauss's formula
        sum_without_dupes = n * (n + 1) // 2
        sum_with_dupes = sum(nums)
        return sum_with_dupes - sum_without_dupes


nums = [1, 3, 4, 2, 2]

print(Solution().findDuplicate(nums))
