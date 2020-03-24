#!/usr/bin/python3

class TicTacToe:

    def __init__(self):
        self.P = [str(p) for p in range(1, 10)]

    def print_board(self):
        print("\n\t-------------")
        for v in range(0, 9, 3):
            print("\t| " + self.P[0 + v] + " | " + self.P[1 + v] + " | " + self.P[2 + v] + " |")
            print("\t-------------")

    def input_validator(self, position):
        if str(position) not in self.P:
            return True
        if self.P[position - 1] == "X" or self.P[position - 1] == "O":
            return True
        return False

    def player(self, pno, symb):
        while(True):
            try:
                position = int(input("\nPlayer " + str(pno) + "'s turn (" + symb + "), select a available position from the board: "))
            except ValueError:
                print("\n  \N{expressionless face} Invalid input, 1-9 values only \N{expressionless face}")
                continue
            if self.input_validator(position):
                print("\n  \N{unamused face} Invalid input or position not available \N{unamused face}")
                continue
            self.P[position - 1] = symb
            break

    def start(self):
        print("\n===========================")
        print(" +++    Tic Tac Toe    +++")
        print("===========================\n")
        win_sets = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]

        print("  ** Starting new game **")

        for p in range(1, 10):
            self.print_board()

            if p%2 != 0:
                pno, symb = 1, "X"
            else:
                pno, symb = 2, "O"

            self.player(pno, symb)
            for s in win_sets:
                if self.P[s[0] - 1] == self.P[s[1] - 1] == self.P[s[2] - 1] == symb:
                    self.print_board()
                    print("\n  *** P" + str(pno) + " wins!\N{grinning face} ***\n")
                    return
        self.print_board()
        print("  **** Draw!\N{smiling face with halo} **** \n")

board = TicTacToe()
board.start()
