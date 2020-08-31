import heapq
import itertools
import random
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.buckets(nums, k)

    # O(nlogn) time complexity
    def heaps(self, nums: List[int], k: int):
        if len(nums) == k:
            return nums

        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=counts.get)

    # O(n) time complexity on average. Worst case is O(n^2), though this only happens with bad
    # choice of pivot which we have addressed with random choice of pivot.
    # this is also a good solution for
    # "find kth something": kth smallest, kth largest, kth most frequent, kth less frequent, etc.
    def quick_select(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        keys = list(counts.keys())

        def partition(left: int, right: int, pivot: int) -> int:
            # lomuto's partition scheme
            pivot_freq = counts[keys[pivot]]
            # 1. move pivot to the end of the array
            keys[pivot], keys[right] = keys[right], keys[pivot]

            # 2. set pointer to the beginning of the list store_index = left
            store_index = left
            # 3. iterate over list and move more frequent elements to the left swap(store_index,i). Increment
            # store index after swap
            for i in range(left, right):
                if counts[keys[i]] > pivot_freq:
                    keys[store_index], keys[i] = keys[i], keys[store_index]
                    store_index += 1

            # 4. place pivot in place
            keys[store_index], keys[right] = keys[right], keys[store_index]
            # return store index for quick select to know which side to go
            return store_index

        def quick_select_go(left: int, right: int):
            if left == right:
                return
            # pick a random pivot, this alleviates possibility of consistently choosing bad pivot
            # and thus making this algo run in O(n^2)
            pivot = random.randint(left, right)
            index = partition(left, right, pivot)
            if index == k:
                return
            # need more elements.
            # since left part already contains elements greater pivot, we go right
            elif k > index:
                quick_select_go(index + 1, right)
            # need less elements, go left
            else:
                quick_select_go(left, index - 1)

        quick_select_go(0, len(keys) - 1)
        return keys[:k]

    # time and space: O(n)
    def buckets(self, nums: List[int], k: int):
        n = len(nums)
        # generate n buckets
        bucket = [[] for _ in range(n + 1)]
        # calculate frequencies
        counts = Counter(nums)
        # append keys according to frequency
        for key, freq in counts.items():
            bucket[freq].append(key)
        # flatten the list
        flat_list = list(itertools.chain.from_iterable(bucket))
        # select last k elements
        return flat_list[len(counts.keys()) - k:]


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(Solution().topKFrequent(nums, k))
