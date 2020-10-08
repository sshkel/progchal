from heapq import heapify, heappop, heappush
from typing import List


# empty matrix?? doesn't seem to be implied by the prototype

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return self.heap_sol(matrix, k)

    # N^2 space complexity
    # N^2 time complexity
    def easiest_sol(self, matrix: List[List[int]], k: int) -> int:
        list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                list.append(matrix[i][j])
        result = sorted(list)[k - 1]
        return result
    # complexity: x = min(k,n), then it's X + klogx
    # x for heap construction and then we do k heap inserts logx each
    def heap_sol(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        # we can do this iteration either on every row or column
        # since the rows and cols are sorted we are guaranteed to find
        # the element in the first k items
        for i in range(min(k, n)):
            heap.append((matrix[0][i], 0, i))

        heapify(heap)

        while k:
            v, i, j = heappop(heap)
            if i < n - 1:
                heappush(heap, (matrix[i+1][j], i+1, j ))
            k -= 1
        return v


sol = Solution()
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
assert sol.kthSmallest(matrix, k) == 13
matrix = [[1, 2], [1, 3]]
k = 2
assert sol.kthSmallest(matrix, k) == 1
print("All done")
