import random
import time
from logo import logo


class TicTacToe:
    def __init__(self):
        self.board = []
        self.game_on = True
        self.player_1_name = input("Player 1 name is: ")
        self.player_2_name = input("Player 2 name is: ")
        self.players_names = [self.player_1_name, self.player_2_name]
        print("Drawing first player...")
        time.sleep(3)
        self.first_player = random.choice(self.players_names)
        for second_player in self.players_names:
            if second_player != self.first_player:
                self.second_player = second_player
                break
        self.actual_player = self.first_player

        signs = ["X", "O"]
        first_player_sign = input(f'{self.first_player} is starting! Type "X" or "O" to start: ').upper()
        while first_player_sign not in signs:
            first_player_sign = input('Only "X" and "O" signs are allowed. Please choose again: ').upper()

        for sign in signs:
            if sign != first_player_sign:
                second_player_sign = sign
                break
        self.players_signs = {self.first_player : first_player_sign, self.second_player : second_player_sign}

    def player_switch(self):
        for actual_player in self.players_names:
            if actual_player != self.actual_player:
                self.actual_player = actual_player
                break

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def player_move(self):
        column = input(f'{self.actual_player}, choose a place to put your "{self.players_signs[self.actual_player]}" '
                       f'sign. Type column number (1,2,3): ')
        row = input("and row number (1,2,3): ")
        return column, row

    def put_sign_on_board(self):
        coordinate = self.player_move()
        column_number = int(coordinate[0]) - 1
        row_number = int(coordinate[1]) - 1
        if self.board[row_number][column_number] == "-":
            self.board[row_number][column_number] = self.players_signs[self.actual_player]
            self.show_board()
            self.is_game_over()
            self.player_switch()
        else:
            print("This place is already taken. Chose another one.")
            self.put_sign_on_board()

    def is_game_over(self):
        # checking all possible winning variants and draw
        result = ""
        if self.board[0][0] != "-" and self.board[0][0] == self.board[0][1] == self.board[0][2]:
            result = self.actual_player
        elif self.board[1][0] != "-" and self.board[1][0] == self.board[1][1] == self.board[1][2]:
            result = self.actual_player
        elif self.board[2][0] != "-" and self.board[2][0] == self.board[2][1] == self.board[2][2]:
            result = self.actual_player
        elif self.board[0][0] != "-" and self.board[0][0] == self.board[1][0] == self.board[2][0]:
            result = self.actual_player
        elif self.board[0][1] != "-" and self.board[0][1] == self.board[1][1] == self.board[2][1]:
            result = self.actual_player
        elif self.board[0][2] != "-" and self.board[0][2] == self.board[1][2] == self.board[2][2]:
            result = self.actual_player
        elif self.board[0][0] != "-" and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            result = self.actual_player
        elif self.board[0][2] != "-" and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            result = self.actual_player
        elif "-" not in self.board[0] and "-" not in self.board[1] and "-" not in self.board[2]:
            result = "draw"

        if result != "":
            if result == "draw":
                print("It's a draw!")
            else:
                print(f"{result} have won!")
            self.player_switch()
            self.game_on = False
            start = input("Do you want to play again? Type y/n : ").lower()
            if start == "y":
                self.board = []
                print(logo)
                self.start_game()

        if not self.game_on:
            print("Thanks for playing. Bye.")

    def start_game(self):
        self.game_on = True
        self.create_board()
        self.show_board()
        while self.game_on:
            self.put_sign_on_board()


print("Welcome to the Tic Tac Toe Game!")
print(logo)
game = TicTacToe()
game.start_game()

