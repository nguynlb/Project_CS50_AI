"""
Tic Tac Toe Player
"""
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def _count_none(board):
    total_none = 0
    for row in board:
        for cell in row:
            if cell is EMPTY: total_none += 1
    return total_none

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return O if _count_none(board) % 2 == 0 else X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = list(board)
    board_copy[action[0]][action[1]] = player(board_copy)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    possible_win = {(0, 1, 2), 
                    (3, 4, 5),
                    (6, 7, 8), 
                    (0, 3 ,6), 
                    (1, 4 ,7), 
                    (2, 5, 8), 
                    (0, 4, 8), 
                    (2, 4, 6)}
    
    check_line = lambda line: (board[line[0] // 3][line[0] % 3] == 
                               board[line[1] // 3][line[1] % 3] == 
                               board[line[2] // 3][line[2] % 3])  \
                               and board[line[0] // 3][line[0] % 3] is not EMPTY
    for line in possible_win:
        if check_line(line):
            return board[line[0] // 3][line[0] % 3]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or _count_none(board) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: return 1
    elif winner(board) == O: return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None
    print(board)

    tmp_board = board.copy()
    possible_actions = actions(tmp_board)
    action , _ = min_max_recursion(tmp_board, 0, possible_actions)
    print(board)
    return action
  
def min_max_recursion(list_board, i, possible_actions):
        # Check win or draw
        score = utility(list_board)
        if score != 0: return (None, score)
        # Check draw
        if _count_none(list_board) == 0: return (None, 0)

        child_board = []
        for action in possible_actions:
            result_board = result(copy.deepcopy(list_board), action)
            child_board.append((action , min_max_recursion(result_board, 
                                            i + 1, 
                                            possible_actions - {action})[1]))
        print(child_board)
        if i % 2 == 0:
            return max(child_board, key=lambda ele: ele[1])
        return min(child_board, key=lambda ele: ele[1])
