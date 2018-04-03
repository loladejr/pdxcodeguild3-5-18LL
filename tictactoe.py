import argparse, random

class Player:
    def __init__(self,name,token):
        self.name=name
        self.token=token

    def __repr__(self):
        return self.token.upper()

    # def __eq__(self, other):
    #     if type(other) is Piece:
    #         if self.color == other.color:
    #             return True


class GameBoard:
    DEPTH = 3
    WIDTH = 3



    def __init__(self):
        self.board = [[' ' for col in range(self.WIDTH)] for row in range(self.DEPTH)]

    def check_win(self):
        # check horizontal wins
        for i in range(self.DEPTH-1, -1, -1):
            for j in range(self.WIDTH-2):
                chunk = self.board[i][j:j+3]
                if all(item == self.board[i][j] and item != ' ' for item in chunk):
                    return self.board[i][j]

        # check vertical wins
        for j in range(self.WIDTH):
            for i in range(self.DEPTH-2):
                chunk = []
                chunk.append(self.board[i][j])
                chunk.append(self.board[i+1][j])
                chunk.append(self.board[i+2][j])
                if all(item == self.board[i][j] and item != ' ' for item in chunk):
                    return self.board[i][j]

        #check diagonal wins
        for i in range(self.DEPTH-2):
            for j in range(self.WIDTH-2):
                chunk = []
                chunk.append(self.board[i][j:j+3])
                chunk.append(self.board[i+1][j:j+3])
                chunk.append(self.board[i+2][j:j+3])
                #
                # for row in chunk:
                #     for cell in row:
                #         print(cell, end='|')
                #     print()
                # # print(chunk[0][0] , chunk[1][1] , chunk[2][2])
                # # print(chunk[2][0] , chunk[1][1] , chunk[0][2])
                # # print()
                if chunk[0][0] == chunk[1][1] == chunk[2][2] and chunk[0][0]!= ' ':
                    return chunk[0][0]
                elif chunk[2][0] == chunk[1][1] == chunk[0][2] and chunk[2][0] != ' ':
                    return chunk[2][0]


    def place_token(self, x,y,token):
    #this function is to define X and O token
        place = self.board[x][y]
        print(place)
        if place == 'X' or place == 'O':
            print('location full. Select another.')
            return False
        self.board[x][y]=token



    def print_board(self):
        #this  function is to print the board
        for row in range(len(self.board)):
            for cell in self.board[row]:
                print(cell, end='|')
            print()


    def calc_winner(self):                #this function is to calculate winner
        winner = board.checkwin()
        return winner


    # def is_full(self):            #this function is to check if the matrix is full
    #     return not any([item == ' ' for item in self.board[i]] for i in range(len(self.board)))
    def is_full(self):
        for row in self.board:
            if any(item==' ' for item in row):
                return False

    def game_over(self):
        return self.check_win() or self.is_full()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tic tac Toe module')
    parser.add_argument('-f', '--file',
                        help='File path of C Tic Tac toe you want to evaluate.')
    args = parser.parse_args()

    # File input version
    if args.file:
        with open(args.file, 'r') as f:
            moves = f.read().split()

        board = GameBoard()

        for i, move in enumerate(moves):
            current_turn = 'X' if i % 2 == 0 else 'O'
            board.place_piece(current_turn, int(move) - 1)

        board.print_board()
        print(board.check_win())

    # 2 player game version
    else:
        while True:
            board = GameBoard()
            player_one = Player('sam','X')
            player_two = Player('john','O')
            game_round = 1

            while not board.game_over():
                current_player = player_one if game_round % 2 else player_two

                while True:
                    move = input(f"{current_player}: Enter your move: ").strip().lower()
                    try:
                        move = int(move)
                        grid= {1:(0,0),2:(0,1),3:(0,2),
                            4:(1,0),5:(1,1),6:(1,2),
                            7:(2,0),8:(2,1),9:(2,2)}
                        if 1 <= move <= 9:
                            x,y = grid[move]
                            move = board.place_token(x,y,current_player.token)
                            if type(move) is bool:
                                raise IndexError('Invalid column.')
                            board.print_board()
                            game_round += 1
                            break
                        else:
                            raise IndexError('Invalid column.')
                    except (ValueError, IndexError):
                        print("Invalid move. Please choose a column [1-7] that isn't full.")

            if not board.is_full():
                print("test")
                print(f"Game over! Winner: {board.check_win()}")
            else:
                print("test")
                print(f"Game over! No one wins!")

            while True:
                play_ag = input("Do you want to play again: ").strip().lower()
                if play_ag in ['yes', 'y', 'no', 'n']:
                    break

            if play_ag in ['no', 'n']:
                break
