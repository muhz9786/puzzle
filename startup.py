from main import Board, Chip
import time

if __name__ == "__main__":
    #'''
    board = Board([
        [0, 0, 0], 
        [0, 0, 0],
        [0, 0, 0]
        ])

    chip1 = Chip([
        [1]
    ])
    chip2 = Chip([
        [0, 1],
        [1, 1]
    ])
    chip3 = Chip([
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]
    ])

    '''
    board = Board([
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0]
        ])

    chip1 = Chip([
        [1, 0], 
        [1, 1]
    ])
    chip2 = Chip([
        [1, 1, 1], 
        [1, 1, 1], 
        [1, 0, 0]
    ])
    chip3 = Chip([
        [1, 0],
        [1, 1]
    ])
    chip4 = Chip([
        [1, 1, 1, 1], 
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ])
    chip5 = Chip([
        [1, 1], 
    ])
    chip6 = Chip([
        [0, 0, 1], 
        [1, 1, 1], 
        [1, 1, 1]
    ])
    chip7 = Chip([
        [1, 1, 1], 
        [1, 1, 1], 
        [0, 0, 1], 
    ])
    chip8 = Chip([
        [1],
        [1] 
    ])
    chip9 = Chip([
        [0, 0, 1], 
        [1, 1, 1],
        [1, 1, 1]
    ])
    '''

    #chipList = [chip1, chip2, chip3, chip4, chip5, chip6, chip7, chip8, chip9]
    chipList = [chip1, chip2, chip3]
    t1 = time.time()
    result = board.resolve(chipList)
    t2 = time.time()
    print("time:", t2-t1, "s")
    for (c, s) in result:
        print(c.get(s))
    #print(board.num)
    #print(board.sum)