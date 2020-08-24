from pprint import pprint
from typing import List


# Complexity
# Time: 2**n
# Space 2**n <- for holding all the arrays
class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.lexicographic_subsets(nums)

    # start with empty subset, at each step, take an int into consideration
    # and generate new subsets from the existing ones
    def cascading(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]

        for num in nums:
            power_set += [elem + [num] for elem in power_set]
        return power_set

    # iterate over all lengths
    def backtracking(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first: int, curr: List[int]):
            if len(curr) == k:
                power_set.append(curr[:])

            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        power_set = []
        n = len(nums)
        for k in range(n + 1):
            backtrack(0, [])
        return power_set

    # apparently originated from donald knuth
    # map each subset to a bitmask where 1 means that we take an element in the subset
    # generate 2**n bitmasks and thus the subsets as well
    def lexicographic_subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nth_bit = 1 << n
        power_set = []
        for i in range(2 ** n):
            # generate bitmask with zero padding on the left
            # e.g. for a n of 3 and i of 1 we end up with
            # 0b1001 and then we apply [3:] to slice off the start
            # alternatively we could just iterate between 2**n and 2**(n+1)
            # instead of nth_bit stuff
            bit_mask = bin(nth_bit | i)[3:]
            power_set.append([nums[j] for j in range(n) if bit_mask[j] == "1"])
        return power_set


nums = [1, 2, 3]
pprint(Solution().subsets(nums))
