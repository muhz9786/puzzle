from multiprocessing import Queue
import numpy as np
import time

class __PlaceError(ValueError):
    pass

class Board:
    def __init__(self, array2D):
        self.mat = np.array(array2D, dtype=np.uint8)
        self.shape = self.mat.shape
        self.__chips = []
        self.__result = None
        self.sum = 0
        self.num = 0

    def resolve(self, chips):
        if not self.__is_possible(chips):
            raise ValueError("Some chip is too big.")
        self.__chips = chips
        self.sum = np.math.factorial(len(self.__chips)) * 4**len(self.__chips)
        self.__search(self.__chips, self.mat)
        self.__result.reverse()
        return self.__result

    def __is_possible(self, chips):
        num = 0
        num += np.count_nonzero(self.mat)
        for chip in chips:
            if max(chip.shape) > max(self.shape) or min(chip.shape) > min(self.shape):
                return False
            num += np.count_nonzero(chip.mat)
        if num != self.shape[0] * self.shape[1]:
            return False
        return True

    def __search(self, chips, board):
        if self.__result != None:
            return
        if len(chips) == 0:
            self.num += 1
            self.__result = []
            return
        for index, c in enumerate(chips):
            for s in range(1,5):
                try:
                    board_ = self.__put(board, c, s)
                    chips_ = chips[0:index]+chips[index+1:]
                    self.__search(chips_, board_)
                    if self.__result != None:
                        self.__result.append((c, s))
                        return
                except __PlaceError:
                    n = len(chips) - 1
                    self.num += np.math.factorial(n) * 4**n

    def __put(self, board, chip, state):
        bh, bw = board.shape
        c = chip.get(state)
        ch, cw = c.shape
        for i in range(bh):
            for j in range(bw):
                if board[i][j] == 0:
                    for offset in range(cw):
                        if c[0, offset] == 1:
                            x = offset
                            break
                    if (j - x) < 0 or (cw - x) > (bw - j) or ch > (bh - i):
                        raise __PlaceError("Out of range.")
                    board[i: i+ch, j-x: j-x+cw] += c
                    if board.max() > 1:
                        raise __PlaceError("Overlapping.")
                    return board

class Chip:
    def __init__(self, array2D):
        self.mat = np.array(array2D, dtype=np.uint8)
        self.shape = self.mat.shape

    def get(self, state=1):
        if state > 4:
            state = state % 4
        if state == 1:
            return self.mat
        else:
            return np.rot90(self.mat, state-1)
