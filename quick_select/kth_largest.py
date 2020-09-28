import heapq
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.heap(nums, k)

    # o(nlogn)
    def just_sort_it(self, nums: List[int], k: int):
        return sorted(nums)[len(nums) - k]

    def heap(self, nums: List[int], k: int):
        return heapq.nlargest(k, nums)[-1]

    # O(n) on average with worst case of O(n2) but random pivot armortises that
    def quickselect(self, nums: List[int], k: int):
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1
            nums[store_index], nums[right] = nums[right], nums[store_index]
            return store_index

        def quickselect_go(left: int, right: int):
            if left == right:
                return nums[left]
            index = random.randint(left, right)
            pivot_index = partition(left, right, index)

            if pivot_index == k:
                return nums[pivot_index]
            elif k < pivot_index:
                return quickselect_go(left, pivot_index - 1)
            else:
                return quickselect_go(pivot_index + 1, right)

        return quickselect_go(0, len(nums) - 1)


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().findKthLargest(nums, k))
