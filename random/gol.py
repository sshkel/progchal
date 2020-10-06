from copy import deepcopy
from pprint import pprint
from typing import List


class Solution:
    def count_neighbours(self, i: int, j: int, board: List[List[int]]):
        state = 0
        update_counter = 0
        row_limit = len(board)
        if row_limit > 0:
            column_limit = len(board[0])
            for x in range(max(0, i - 1), min(i + 2, row_limit)):
                for y in range(max(0, j - 1), min(j + 2, column_limit)):
                    if x != i or y != j:
                        state += board[x][y]
                        update_counter += 1

        return state

    def determine_state(self, current_state: int, num_neighbours: int):
        if current_state == 1:
            return 0 if num_neighbours < 2 or num_neighbours > 3 else 1
        else:
            return 0 if num_neighbours != 3 else 1

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        previous_state = deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                num_neighbours = self.count_neighbours(i, j, previous_state)
                new_state = self.determine_state(previous_state[i][j], num_neighbours)
                board[i][j] = new_state


board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
Solution().gameOfLife(board)
pprint(board)
