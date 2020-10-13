class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[0] * n for _ in range(n)]
        self.size = n

    def __check_row(self, row: int, player: int) -> bool:
        count = 0
        # check rows
        for i in range(self.size):
            if self.board[row][i] == player:
                count += 1
        return count == self.size

    def __check_col(self, col: int, player: int) -> bool:
        count = 0
        # check rows
        for i in range(self.size):
            if self.board[i][col] == player:
                count += 1
        return count == self.size

    # could check specific diagonal depending on pos, but I am lazy
    def __check_diagonals(self, player: int) -> bool:
        count = 0
        # check left diagonal
        for i in range(self.size):
            if self.board[i][i] == player:
                count += 1
        if count == self.size:
            return True
        count = 0
        # check right diagonal
        for i in range(self.size):
            if self.board[i][self.size - i - 1] == player:
                count += 1
        if count == self.size:
            return True

        return False

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player

        if self.__check_col(col, player) or self.__check_row(row, player) or self.__check_diagonals(player):
            return player
        return 0


calls = ["TicTacToe", "move", "move", "move"]
args = [[2], [0, 1, 2], [1, 0, 1], [1, 1, 2]]

class_inst = locals()[calls[0]](args[0][0])

for i in range(1, len(calls)):
    print(getattr(class_inst, calls[i])(*args[i]))
