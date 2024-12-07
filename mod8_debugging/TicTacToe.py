
import numpy as np
from enum import Enum
import random

class MoveType(Enum):
    top_left = (0,0)
    top_center = (0,1)
    top_right = (0,2)
    
    middle_left = (1,0)
    middle_center = (3,1)
    middle_right = (1,2)

    bottom_left = (2,0)
    bottom_center = (2,1)
    bottom_right = (2,2)

class CellStatus(Enum):
    EMPTY = 0
    USER = 1
    COMPUTER = 2
    
MARKERS = {0 : " ", 
           1 : "X", 
           2 : "O"}

class TicTacToe:
    """Class representing a game of Tic Tac Toe."""

    def __init__(self):
        """Init instance of Tic Tac Toe."""
        self.board = np.zeros([3,3])
        self.valid_moves = [move.value for move in MoveType]
        self.print_instrutions()
    
    def print_instructions(self):
        """Print instructions."""
        valid_moves_str = ', '.join([MoveType(moev).name for move in self.valid_moves])
        print(f"Welcome to Tic Tac Toe! \nUser input should be one of the moves below: \n{valid_moves_str}")
    
    def __update_valid_moves(self):
        """Update the list of valid moves remaining."""
        self.valid_moves = [tuple(valid_move) for valid_move in np.argwhere(self.board == 0)]

    def __print_game_board(self):
        """Print game board."""
        
        # display board with Xs and Os
        disp_board = np.reshape([MARKERS[n] for n in self.board.flatten()], [3,3])
        
        print('\n')
        print(disp_board)

    def __user_take_turn(self):
        """Prompt the user to take their turn."""
        user_move = input("Please take your turn: ")
        if MoveType[user_move].value in self.valid_moves:
            move_index = MoveType[user_move].value
            self.board[move_index] = CellStatus.USER.value
            self.__update_valid_moves()
            self.__print_game_board()
        else:
            print("Please enter a valid move.")
            self.__user_take_turn()
        
    def __computer_take_turn():
        """Automate the computer's turn."""
        move_index = random.choice(self.valid_moves)
        self.board[move_index] = CellStatus.COMPUTER.value
        self.__update_valid_moves()
        self.__print_game_board()

    def play_game(self):
        """Play a game of Tic Tac Toe until someone wins."""
        end_game = False
        while not end_game:
            self.__user_take_turn()
            end_game, message = self.__check_end_conditions("USER")
            if end_game:
                print(message)
            

            self.__computer_take_turn()
            end_game, message = self.__check_end_conditions("COMPUTER")
            if end_game:
                print(message)
                break

    def __check_end_conditions(self, player) -> tuple[bool, str]:
        """Check if the game should end."""
        # find player's moves on board
        [player_rows, player_cols] = np.where(self.board == CellStatus[player].value)
        unique_rows, row_counts = np.unique(player_rows, return_counts=True)
        unique_cols, col_counts = np.unique(player_cols, return_counts=True)

        # check win conditions
        row_win = any(row_counts >=3)
        col_win = any(col_counts >=3)
        diag_win = all(np.diagonal(self.board) == CellStatus["USER"].value) | all(np.diagonal(np.fliplr(self.board)) == CellStatus["USER"].value)
        end_game = any([row_win, col_win, diag_win])

        # if player has won
        if end_game:
            if player == "USER":
                message = "You win!" 
            elif player == "COMPUTER":
                message = "Computer wins!"

        # if there are valid moves remaining
        elif len(self.valid_moves) == 0:
            end_game = True
            message = "No valid moves remaining."

        # assign empty string if the game continues
        else:
            message = ""
        return end_game, message 