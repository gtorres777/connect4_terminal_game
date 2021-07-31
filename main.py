
import sys
from termcolor import colored, cprint

current_board_positions = [
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
]



def build_board_for_connect4(board):
    for row in range(11):
        if row % 2 == 0:
            for column in range(13):
                if column == 12:
                    if board[row//2][column//2] == "X":
                        cprint(u'\u2B24', 'yellow', attrs=['bold'], file=sys.stderr)
                    print(board[row//2][column//2])
                elif column % 2 == 0:
                    print(board[row//2][column//2],end="")
                else:
                    print("|",end="")
        else:
            print("-"*13)


def check_if_empty_in_column(row,col):
    if current_board_positions[row][col] == " ":
        return True
    else:
        return False


def move_piece(column,player):
    for row in range(5,-1,-1):
        for col in range(1,8):
            if col == column and check_if_empty_in_column(row,col-1):
                if player == 1:
                    current_board_positions[row][col-1] = colored("O", 'red', attrs=['bold'])
                    return
                else:
                    current_board_positions[row][col-1] = colored("O", 'yellow', attrs=['bold'])
                    return



#### Validating

def check_diagonals_for_win(board,piece):

    #### check diagonal down left
    counter_piece_ddl = 0

    for col in range(3,7):
        for row in range(0,col+1):
            if row < len(board):
                if board[row][col-row] == piece:
                    if row <3 and col-row >=3 and col-row <=6:
                        for i in range(1,4):
                            if board[row+i][col-row-i] == piece:
                                counter_piece_ddl += 1
                            if counter_piece_ddl == 3:
                                return True
                        else:
                            counter_piece_ddl = 0

    start_ddl = 0
    for col in range(6,4,-1):
        col = 6
        start_ddl += 1
        for row in range(start_ddl,6):
            if board[row][col-row+start_ddl] == piece:
                if row <3 and col-row+start_ddl >=3 and col-row+start_ddl <=6:
                    for i in range(1,4):
                        if board[row+i][col-row+start_ddl-i] == piece:
                            counter_piece_ddl += 1
                        if counter_piece_ddl == 3:
                            return True
                    else:
                        counter_piece_ddl = 0

    #### check diagonal down right

    counter_piece_ddr = 0

    start_ddr = -1
    for col in range(0,3):
        start_ddr += 1
        for row in range(start_ddr,6):
            if board[row][-(col-row)] == piece:
                if row < 3 and -(col-row) <= 3:
                    for i in range(1,4):
                        if board[row+i][-(col-row)+i] == piece:
                            counter_piece_ddr += 1
                        if counter_piece_ddr == 3:
                            return True
                    else:
                        counter_piece_ddr = 0


    s_tmp = 0
    for row in range(0,3):
        s_tmp += 1
        r_tmp = 0-row
        for col in range(s_tmp,7):
            if board[row+r_tmp][col] == piece:
                if row+r_tmp < 3 and col <= 3:
                    for i in range(1,4):
                        if board[row+r_tmp+i][col+i] == piece:
                            counter_piece_ddr += 1
                        if counter_piece_ddr == 3:
                            return True
                    else:
                        counter_piece_ddr = 0
            r_tmp += 1


def check_rows_for_win(board,piece):

    counter_piece = 0

    for row in range(5,-1,-1):
        for col in range(4):
            if board[row][col] == piece:
                for i in range(1,4):
                    if board[row][col+i] == piece:
                        counter_piece += 1
                    if counter_piece == 3:
                        return True

                else:
                    counter_piece = 0


def check_cols_for_win (board,piece):

    counter_piece = 0

    for col in range(7):
        for row in range(3):
            if board[row][col] == piece:
                for i in range(1,4):
                    if board[row+i][col] == piece:
                        counter_piece += 1
                    if counter_piece == 3:
                        return True
                else:
                    counter_piece = 0


def check_if_someone_won(board,piece):

    if check_rows_for_win(board,piece) or check_cols_for_win(board,piece) or check_diagonals_for_win(board,piece):
        return True





print("------------> Welcome to Connect4 <------------")
print("PRESS ENTER TO START")
start = input()


if start == "":

    print("\n")

    print("1 2 3 4 5 6 7")
    build_board_for_connect4(current_board_positions)

    player = 1
    piece = colored("O", 'red', attrs=['bold'])

    while True:

        print("\n Players turn:",piece)

        if player == 1:
            move_player1 = int(input("Enter number of column: "))
            print("\n")
            move_piece(move_player1,player)

            print("1 2 3 4 5 6 7")
            build_board_for_connect4(current_board_positions)


            if check_if_someone_won(current_board_positions,piece):
                print(f"\n {piece} WINS!!!")
                exit()

            player = 2
            piece = colored("O", 'yellow', attrs=['bold'])

        else:
            move_player2 = int(input("Enter number of column: "))
            print("\n")
            move_piece(move_player2,player)

            print("1 2 3 4 5 6 7")

            build_board_for_connect4(current_board_positions)


            if check_if_someone_won(current_board_positions,piece):
                print(f"\n {piece} WINS!!!")
                exit()

            player = 1
            piece = colored("O", 'red', attrs=['bold'])
