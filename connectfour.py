class Piece(object):

    def __init__(self, color, position,player1,player2):
        self.color = color
        self.position = position
        self.player1 = player1
        self.player2 = player2

    def __repr__(self):
        if self.color == 'red':
            return 'R'
        else:
            return 'Y'




class Connectfour(object):

    def __init__(self):
        self.board = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

        self.yellow_team = []
        self.red_team = []


    def checkloc(self):
        with open('connect-four-moves.txt', 'r') as connect:
            connect=connect.read().split()
        for num in connect:

            num=num.strip("")
            try:
                num=int(num)
            except ValueError:
                continue
            if num%2==0:
                piece='Y'
                self.yellow_team.append

            else:
                piece='R'
                self.red_team.append

            for i in range(len(self.board)-1,-1,-1):
                if self.board[i][num-1] =='O':
                        self.board[i][num-1]=piece
                        break
    def print_board(self):
        for row in range(len(self.board)):
            for cell in self.board[row]:
                print (cell, end='|')
            print()


    def __repr__(self):
        board=f"{self.board}"
        return board


if __name__ == '__main__':
    board = Connectfour()
    board.checkloc()
    print(board)
    board.print_board()
